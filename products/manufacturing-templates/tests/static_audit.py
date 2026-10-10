"""Inventory originals without changing them; no compatibility claims from XML alone."""
import hashlib
import json
from pathlib import Path
import re
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from openpyxl import load_workbook

PRODUCT = Path(__file__).resolve().parents[1]


def audit():
    result = {"workbooks": {}, "listings": [], "previews": []}
    for path in sorted((PRODUCT / "dist").glob("*.xlsx")):
        wb = load_workbook(path)
        info = {"sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                "functions": set(), "sheets": {}, "metadata": {}, "external_links": [],
                "suspicious_metadata": [], "macros": False, "formulas_with_new_prefix": []}
        for ws in wb:
            formulas = [c.value for row in ws for c in row if c.data_type == "f"]
            for formula in formulas:
                info["functions"].update(re.findall(r"([A-Z][A-Z0-9_.]*)\s*\(", formula.upper()))
                if "_xlfn." in formula or "_xlws." in formula:
                    info["formulas_with_new_prefix"].append(formula)
            cf = []
            for entry, rules in ws.conditional_formatting._cf_rules.items():
                for rule in rules:
                    cf.append({"range": str(entry.sqref), "type": rule.type,
                        "formula": rule.formula, "priority": rule.priority,
                        "fill_foreground": rule.dxf.fill.fgColor.rgb if rule.dxf and rule.dxf.fill else None,
                        "fill_background": rule.dxf.fill.bgColor.rgb if rule.dxf and rule.dxf.fill else None})
            dvs = [{"ranges": str(d.sqref), "type": d.type, "formula1": d.formula1,
                    "operator": d.operator, "showErrorMessage": d.showErrorMessage,
                    "showDropDown": d.showDropDown, "allowBlank": d.allowBlank}
                   for d in ws.data_validations.dataValidation]
            info["sheets"][ws.title] = {"formula_count": len(formulas), "freeze_panes": ws.freeze_panes,
                "conditional_formats": cf, "data_validation": dvs,
                "instructions": [c.value for row in ws for c in row if c.data_type == "s"] if ws.title == "How to use" else []}
        info["functions"] = sorted(info["functions"])
        with ZipFile(path) as z:
            for name in z.namelist():
                if "vbaProject" in name:
                    info["macros"] = True
                if name.endswith(".rels"):
                    xml = ET.fromstring(z.read(name))
                    info["external_links"] += [{"part": name, **e.attrib} for e in xml if e.attrib.get("TargetMode") == "External"]
                if name.startswith("docProps/") and name.endswith(".xml"):
                    info["metadata"][name] = z.read(name).decode("utf-8")
                if name.endswith(".xml") or name.endswith(".rels"):
                    xml = z.read(name).decode("utf-8")
                    # Exclude namespace URLs (e.g. http:) from Windows drive detection.
                    hits = re.findall(r"(?:\b[A-Z]:[\\](?![\\])[^<\"]+|file:///[^<\"]+|\b(?:Joey|jdb3654|Claude|OpenAI|employer)\b)", xml, re.I)
                    if hits:
                        info["suspicious_metadata"].append({"part": name, "hits": sorted(set(hits))})
            info["chart_xml"] = {n: z.read(n).decode("utf-8") for n in z.namelist() if re.match(r"xl/charts/chart\d+\.xml$", n)}
        result["workbooks"][path.name] = info
    text = (PRODUCT / "LISTING.md").read_text(encoding="utf-8")
    sections = [("bundle", text.split("## Bundle listing")[1].split("## Single listings")[0])]
    for name, marker in [("oee", "### OEE tracker"), ("downtime", "### Downtime log"), ("pm", "### Preventive maintenance")]:
        sections.append((name, text.split(marker)[1].split("\n### ")[0].split("\n## Images")[0]))
    for name, section in sections:
        title = re.search(r"\*\*Title[^\n]*?\*\*\s*(?:\n)?([^\n]+)", section).group(1).strip()
        tags = re.search(r"\*\*Tags[^\n]*?\*\*\s*(?:\n)?([^\n]+)", section).group(1).strip().split(", ")
        result["listings"].append({"name": name, "title": title, "title_characters": len(title),
            "title_words": len(title.split()), "tags": [{"text": t, "characters": len(t)} for t in tags],
            "within_limits": len(title) <= 140 and len(tags) <= 13 and all(len(t) <= 20 for t in tags)})
    try:
        from PIL import Image
        for path in sorted((PRODUCT / "previews").glob("*.png")):
            with Image.open(path) as im:
                result["previews"].append({"name": path.name, "size": list(im.size), "metadata": im.info})
    except ImportError:
        result["previews"] = "Pillow unavailable; inspect images manually"
    return result


if __name__ == "__main__":
    output = Path(__file__).with_name("static-results.json")
    output.write_text(json.dumps(audit(), indent=2), encoding="utf-8")
    print(output)
