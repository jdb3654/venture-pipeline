"""Run with the office suite's UNO-enabled Python (including AOO Python 2.7).

Only opens disposable inputs. calculateAll -> ODS save -> close -> reopen -> read.
The caller owns the isolated soffice listener/profile and its lifetime.
"""
from __future__ import print_function
import json
import os
import sys
import time
import traceback

sys.path.insert(0, os.path.dirname(sys.executable))
# AOO's launcher runs python-core-*/bin/python.exe; UNO lives two levels up.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(sys.executable), "..", "..")))
sys.path.insert(0, os.getcwd())
import uno
from com.sun.star.beans import PropertyValue


def prop(name, value):
    p = PropertyValue()
    p.Name, p.Value = name, value
    return p


def safely(fn):
    try:
        return fn()
    except Exception as exc:
        return {"unverified": str(exc)}


def sequence(value):
    # AOO 4.1.7's Python 2 bridge marshals an empty UNO sequence as ByteSequence.
    if isinstance(value, uno.ByteSequence) and len(value) == 0:
        return ()
    return value


def features(doc, request):
    result = {}
    controller = doc.getCurrentController()
    for sheetname, addresses in request.get("features", {}).items():
        sheet = doc.Sheets.getByName(sheetname)
        controller.setActiveSheet(sheet)
        item = {"freeze": safely(lambda: [controller.hasFrozenPanes(),
                    controller.getSplitColumn(), controller.getSplitRow()]), "cells": {}}
        for address in addresses:
            cell = sheet.getCellRangeByName(address)
            validation = cell.Validation
            rules = cell.ConditionalFormat
            cf = []
            for i in range(rules.Count):
                entry = rules.getByIndex(i)
                style = doc.StyleFamilies.getByName("CellStyles").getByName(entry.StyleName)
                cf.append({"formula1": entry.Formula1, "formula2": entry.Formula2,
                           "operator": entry.Operator.value,
                           "style": entry.StyleName, "background": style.CellBackColor})
            item["cells"][address] = {
                "validation_type": validation.Type.value,
                "formula1": validation.Formula1, "formula2": validation.Formula2,
                "show_error": validation.ShowErrorMessage,
                "show_list": safely(lambda: validation.ShowList),
                "conditional_rules": cf}
        charts = []
        collection = sheet.getCharts()
        for name in sequence(collection.getElementNames()):
            chart = collection.getByName(name).getEmbeddedObject()
            def chart_info():
                diagram = chart.getFirstDiagram()
                systems = []
                for cs in diagram.getCoordinateSystems():
                    types = []
                    for ct in cs.getChartTypes():
                        series = []
                        for ds in ct.getDataSeries():
                            series.append({"axis": ds.AttachedAxisIndex,
                                "data": [list(seq.Values.getData()) for seq in ds.getDataSequences()]})
                        types.append({"type": ct.getChartType(), "series": series})
                    systems.append(types)
                return {"name": name, "coordinate_systems": systems}
            charts.append(safely(chart_info))
        item["charts"] = charts
        result[sheetname] = item
    result["calculation_settings"] = safely(lambda: {
        "regular_expressions": doc.RegularExpressions,
        "whole_cell_matching": doc.MatchWholeCell})
    return result


def main():
    manifest, output, port = sys.argv[1:4]
    context = uno.getComponentContext()
    resolver = context.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", context)
    remote = None
    for _ in range(100):
        try:
            remote = resolver.resolve(
                "uno:socket,host=127.0.0.1,port=%s;urp;StarOffice.ComponentContext" % port)
            break
        except Exception:
            time.sleep(.2)
    if remote is None:
        raise RuntimeError("Could not connect to isolated headless soffice")
    desktop = remote.ServiceManager.createInstanceWithContext(
        "com.sun.star.frame.Desktop", remote)
    with open(manifest) as stream:
        requests = json.load(stream)
    results = []
    for req in requests:
        doc = None
        began = time.time()
        try:
            doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(req["input"]),
                "_blank", 0, (prop("Hidden", True), prop("ReadOnly", False),
                               prop("UpdateDocMode", 0), prop("MacroExecutionMode", 0)))
            if doc is None:
                raise RuntimeError("Office returned no document")
            calc_start = time.time()
            doc.calculateAll()
            calc_seconds = time.time() - calc_start
            imported_features = features(doc, req)
            ods = req["input"][:-5] + ".ods"
            doc.storeAsURL(uno.systemPathToFileUrl(ods),
                           (prop("FilterName", "calc8"), prop("Overwrite", True)))
            if req.get("pdf"):
                # Print only bounded ranges; pagination is not a listing image simulation.
                target_sheet = doc.Sheets.getByName(next(iter(req["pdf"])))
                doc.getCurrentController().setActiveSheet(target_sheet)
                for sheetname in doc.getSheets().getElementNames():
                    sheet = doc.Sheets.getByName(sheetname)
                    area = req["pdf"].get(sheetname)
                    sheet.IsVisible = bool(area)
                    sheet.setPrintAreas((sheet.getCellRangeByName(area).RangeAddress,) if area else ())
                    style = doc.StyleFamilies.getByName("PageStyles").getByName(sheet.PageStyle)
                    style.IsLandscape = True
                    style.ScaleToPagesX = 1
                    style.ScaleToPagesY = 1
                doc.storeToURL(uno.systemPathToFileUrl(req["input"][:-5] + ".pdf"),
                              (prop("FilterName", "calc_pdf_Export"), prop("Overwrite", True)))
            doc.close(True)
            doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(ods), "_blank", 0,
                                               (prop("Hidden", True), prop("ReadOnly", True)))
            data, errors = {}, {}
            for sheetname in doc.getSheets().getElementNames():
                sheet = doc.Sheets.getByName(sheetname)
                errors[sheetname] = sheet.queryFormulaCells(
                    uno.getConstantByName("com.sun.star.sheet.FormulaResult.ERROR")).getRangeAddressesAsString()
            for sheetname, ranges in req["read"].items():
                sheet = doc.Sheets.getByName(sheetname)
                data[sheetname] = {rng: sheet.getCellRangeByName(rng).getDataArray() for rng in ranges}
            diagnostics = {}
            for sheetname, ranges in req["read"].items():
                sheet = doc.Sheets.getByName(sheetname)
                # Read native formula text, display and error code at the first row.
                diagnostics[sheetname] = []
                for rng in ranges:
                    cells = sheet.getCellRangeByName(rng)
                    width = cells.RangeAddress.EndColumn - cells.RangeAddress.StartColumn + 1
                    for col in range(width):
                        cell = cells.getCellByPosition(col, 0)
                        diagnostics[sheetname].append({"formula": cell.getFormula(),
                            "display": cell.getString(), "error": cell.getError()})
            results.append({"id": req["id"], "data": data, "errors": errors, "diagnostics": diagnostics,
                "features": imported_features, "calculate_seconds": calc_seconds,
                "load_calculate_save_read_seconds": time.time() - began})
        except Exception as exc:
            results.append({"id": req["id"], "error": str(exc), "traceback": traceback.format_exc()})
        finally:
            if doc is not None:
                doc.close(True)
        with open(output, "w") as stream:
            json.dump(results, stream, indent=2)
        print(req["id"], "complete", flush=True) if sys.version_info[0] >= 3 else sys.stdout.write(req["id"] + " complete\n")
        sys.stdout.flush()
    desktop.terminate()


if __name__ == "__main__":
    main()
