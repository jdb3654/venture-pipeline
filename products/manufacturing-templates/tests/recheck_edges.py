"""Additional adversarial inputs for the fixed products; native results only."""
import argparse
import json
from pathlib import Path
from run_review import Suite, fresh, oee_row, down_row, pm_row, run_office, get


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--work-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--soffice", type=Path, default=Path(r"C:\Program Files (x86)\OpenOffice 4\program\soffice.exe"))
    ap.add_argument("--uno-python", type=Path, default=Path(r"C:\Program Files (x86)\OpenOffice 4\program\python.exe"))
    ap.add_argument("--timeout", type=int, default=3600)
    args = ap.parse_args()
    root = args.work_dir.resolve()
    root.mkdir(parents=True, exist_ok=True)
    s = Suite(root)
    for mode in ("missing_date", "duplicate_machine", "text_cycle", "low_target"):
        wb = fresh("oee")
        wb["Setup"]["A5"], wb["Setup"]["B5"] = "M1", 60
        oee_row(wb, shift=60, stops=0, down=0, parts=24, rejects=0)
        if mode == "missing_date":
            wb["Production Log"]["A5"] = None
        elif mode == "duplicate_machine":
            wb["Setup"]["A6"], wb["Setup"]["B6"] = "M1", 60
        elif mode == "text_cycle":
            wb["Setup"]["B5"] = "sixty"
        else:
            wb["Dashboard"]["B5"] = .3
        ident = s.scenario("edge_oee_" + mode, "oee", wb,
                           {"Production Log": ["K5:T5"], "Dashboard": ["A9:M29"]},
                           {"Dashboard": ["K9"]} if mode == "low_target" else None,
                           {"Dashboard": "A1:L30"} if mode == "low_target" else None)
        if mode in ("missing_date", "text_cycle"):
            s.non_ok(ident, mode + " visibly warned", "Production Log", "R5")
        elif mode == "duplicate_machine":
            s.check(ident, "duplicate setup cannot silently double cycle and totals", lambda r: (
                get(r, "Dashboard", "K29") == .4 or "duplicate" in str(get(r, "Production Log", "R5")).lower(),
                {"expected": "40% or explicit duplicate warning", "cycle": get(r,"Production Log","K5"),
                 "check":get(r,"Production Log","R5"),"all_oee":get(r,"Dashboard","K29")}))
        else:
            s.equal(ident, "40% OEE exceeds 30% target", "Dashboard", "K9", .4)
    for mode in ("text_date_matching", "text_date_unrelated", "missing_key"):
        wb = fresh("pm")
        pm_row(wb)
        wb["Completion Log"]["A5"] = "yesterday" if mode != "missing_key" else "=TODAY()"
        if mode != "missing_key":
            wb["Completion Log"]["B5"] = "A1" if mode == "text_date_matching" else "A2"
            wb["Completion Log"]["C5"] = "T1"
        ident = s.scenario("edge_pm_" + mode, "pm", wb,
                           {"PM Plan": ["F5:I5"], "Completion Log": ["A5:F5"]})
        s.non_ok(ident, "invalid completion visibly warned", "Completion Log", "F5")
        s.equal(ident, "invalid completion leaves last-completed blank", "PM Plan", "F5", "")
    for mode in ("duplicate_reason", "duplicate_machine"):
        wb = fresh("down")
        wb["Setup"]["A5"], wb["Setup"]["D5"], wb["Setup"]["E5"] = "M1", "R1", "Cat"
        wb["Setup"]["D6" if mode == "duplicate_reason" else "A6"] = "R1" if mode == "duplicate_reason" else "M1"
        down_row(wb, minutes=10)
        ident = s.scenario("edge_down_" + mode, "down", wb,
                           {"Downtime Log": ["G5:K5"], "Pareto": ["B6:B7", "B9:F10"], "By Machine": ["A5:C36"]})
        if mode == "duplicate_reason":
            s.check(ident, "duplicate reason cannot silently create negative unclassified minutes", lambda r: (
                get(r,"Pareto","B7") >= 0,
                {"total":get(r,"Pareto","B6"),"unclassified":get(r,"Pareto","B7"),"cumulative":get(r,"Pareto","F10")}))
        else:
            s.check(ident, "duplicate machine cannot silently create negative other minutes", lambda r: (
                get(r,"By Machine","B35") >= 0,
                {"other":get(r,"By Machine","B35"),"all":get(r,"By Machine","B36")}))
    native = run_office(args, root, s.requests)
    by_id = {r["id"]: r for r in native}
    tests = []
    for req in s.requests:
        s.check(req["id"], "zero formula errors", lambda r: (not any(r["errors"].values()), r["errors"]))
    for ident, title, check in s.checks:
        result = by_id[ident]
        if "error" in result:
            status, evidence = "BLOCKED", result["error"]
        else:
            ok, evidence = check(result)
            status = "PASS" if ok else "FAIL"
        tests.append({"scenario":ident,"test":title,"status":status,"evidence":evidence})
    report = {"tests":tests,"scenarios":[{k:v for k,v in r.items() if k!="data"} for r in native],
              "summary":{state:sum(t["status"]==state for t in tests) for state in ("PASS","FAIL","BLOCKED")}}
    args.output.write_text(json.dumps(report,indent=2))
    print(json.dumps(report["summary"]))
    for test in tests:
        if test["status"] != "PASS":
            print(json.dumps(test))
    return int(report["summary"]["FAIL"] > 0 or report["summary"]["BLOCKED"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
