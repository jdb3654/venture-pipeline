"""Compare an app's recalculated scenario files with expected.json.

    python3 check.py <expected.json> <dir with recalculated .xlsx files> [--app NAME] [--json out.json]

Reads the values each app saved (cached results), so it works for Excel, Google Sheets, OpenOffice or
LibreOffice output alike. Numbers match within 0.0005; text must match exactly; "" means the cell is blank.
"""
import argparse
import json
from pathlib import Path

from openpyxl import load_workbook

TOL = 5e-4


def norm(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return float(v)
    return str(v).strip()


def same(actual, expected):
    a, e = norm(actual), norm(expected)
    if isinstance(e, float) and isinstance(a, float):
        return abs(a - e) <= TOL
    if isinstance(e, float) and a == "":
        return False
    return a == e


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("expected")
    ap.add_argument("results")
    ap.add_argument("--app", default="unknown")
    ap.add_argument("--json")
    ap.add_argument("--native-readback", help="Fresh run_native.py UNO results after saving/reopening ODS (AOO has no XLSX export)")
    a = ap.parse_args()
    expected = json.loads(Path(a.expected).read_text())
    native = {r["id"]: r for r in json.loads(Path(a.native_readback).read_text())} if a.native_readback else None
    report, fails, total = [], 0, 0
    formula_error_scenarios = []
    for scen, checks in expected.items():
        path = Path(a.results) / f"{scen}.xlsx"
        if native is not None and (scen not in native or "error" in native[scen]):
            report.append({"scenario": scen, "status": "BLOCKED", "error": native.get(scen, {})})
            fails += len(checks)
            total += len(checks)
            continue
        if native is None and not path.exists():
            report.append({"scenario": scen, "status": "MISSING"})
            print(f"MISSING  {scen}")
            fails += len(checks)
            total += len(checks)
            continue
        wb = load_workbook(path, data_only=True) if native is None else None
        bad, observations = [], []
        for c in checks:
            total += 1
            v = (wb[c["sheet"]][c["cell"]].value if native is None
                 else native[scen]["data"][c["sheet"]][c["cell"]][0][0])
            observations.append({"sheet": c["sheet"], "cell": c["cell"], "expected": c["value"], "actual": v})
            if not same(v, c["value"]):
                bad.append({**c, "actual": v})
        fails += len(bad)
        if native is not None and any(native[scen]["errors"].values()):
            formula_error_scenarios.append(scen)
        status = "PASS" if not bad and scen not in formula_error_scenarios else "FAIL"
        report.append({"scenario": scen, "status": status, "checks": len(checks), "failures": bad,
                       "observations": observations,
                       "formula_errors": native[scen]["errors"] if native is not None else "not scanned"})
        print(f"{status:7}  {scen}  ({len(checks) - len(bad)}/{len(checks)})")
        for b in bad[:8]:
            print(f"         {b['sheet']}!{b['cell']}: expected {b['value']!r}, got {b['actual']!r}")
    print(f"\n{a.app}: {total - fails}/{total} checks passed")
    if a.json:
        Path(a.json).write_text(json.dumps({"app": a.app, "passed": total - fails, "total": total,
                                            "formula_error_scenarios": formula_error_scenarios,
                                            "scenarios": report}, indent=1, default=str))
    raise SystemExit(1 if fails or formula_error_scenarios else 0)


if __name__ == "__main__":
    main()
