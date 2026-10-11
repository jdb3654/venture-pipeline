"""Bounded native visual retest from an already prepared review run.

Run after run_review.py has prepared inputs; uses a new listener/profile/work folder.
Never overwrites the main run's native results or any product artifact.
"""
import argparse
import copy
import json
from pathlib import Path
import shutil
from run_review import run_office, heterogeneous_input, expand_iferror, Suite


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from-work-dir", type=Path, required=True)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--soffice", type=Path, default=Path(r"C:\Program Files (x86)\OpenOffice 4\program\soffice.exe"))
    parser.add_argument("--uno-python", type=Path, default=Path(r"C:\Program Files (x86)\OpenOffice 4\program\python.exe"))
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("visual-native-results.json"))
    args = parser.parse_args()
    if args.from_work_dir.resolve() == args.work_dir.resolve():
        parser.error("Visual work folder must differ from the original run")
    args.work_dir = args.work_dir.resolve()
    args.work_dir.mkdir(parents=True, exist_ok=True)
    old = json.loads((args.from_work_dir / "manifest.json").read_text())
    ids = {r["id"] for r in old}
    prefix = "diagnostic_" if "diagnostic_oee_target_0.95" in ids else ""
    chosen = {prefix + "oee_target_0.95", prefix + "oee_target_0.5", "down_ranking"}
    requests = []
    for original in old:
        if original["id"] not in chosen:
            continue
        request = copy.deepcopy(original)
        target = args.work_dir / Path(request["input"]).name
        shutil.copyfile(request["input"], target)
        request["input"] = str(target)
        request["pdf"] = {"Pareto": "A1:Z24"} if request["id"] == "down_ranking" else {"Dashboard": "A1:L48"}
        if request["id"] == "down_ranking":
            request["features"] = {"Pareto": ["B5"]}
        requests.append(request)
    if {r["id"] for r in requests} != chosen:
        parser.error("Original run does not contain all three visual cases")
    # A stronger valid-input heterogeneous counterexample, added during review.
    suite = Suite(args.work_dir)
    reads = {"Production Log": ["A5:R504"], "Dashboard": ["A9:L29"]}
    for id in ("oee_heterogeneous", "diagnostic_oee_heterogeneous"):
        wb = heterogeneous_input()
        if id.startswith("diagnostic_"):
            if not any(cell.data_type == "f" and "IFERROR(" in cell.value
                       for sheet in wb for row in sheet for cell in row):
                continue
            for sheet in wb:
                for row in sheet:
                    for cell in row:
                        if cell.data_type == "f" and "IFERROR(" in cell.value:
                            cell.value = expand_iferror(cell.value)
        suite.scenario(id, "oee", wb, reads)
    requests += suite.requests
    result = run_office(args, args.work_dir, requests)
    compact = [{k: v for k, v in r.items() if k != "data"} for r in result]
    args.output.write_text(json.dumps(compact, indent=2), encoding="utf-8")
    print("Native PDFs and full readback:", args.work_dir)
    return int(any("error" in r for r in result))


if __name__ == "__main__":
    raise SystemExit(main())
