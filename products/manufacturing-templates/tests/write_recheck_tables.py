"""Generate every-assertion tables from the dated post-fix evidence."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def read(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def cell(value):
    s = json.dumps(value, ensure_ascii=True) if not isinstance(value, str) else value
    return s[:500].replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def main():
    broad, edges, static, docs, shared = [read(name) for name in (
        "recheck-results.json", "recheck-edge-results.json", "recheck-static-checks.json",
        "recheck-document-results.json", "xsuite/results-aoo-4.1.7.json")]
    lanes = [("Broad native", broad), ("New native edges", edges),
             ("Structural / documentation agreement", static), ("Guide integrity/rendering", docs)]
    lines = ["| Lane | PASS | FAIL | BLOCKED |", "|---|---:|---:|---:|"]
    for name, data in lanes:
        summary = data["summary"]
        lines.append("| %s | %d | %d | %d |" % (name, summary["PASS"], summary["FAIL"], summary.get("BLOCKED", 0)))
    lines.append("| Shared native expected cells | %d | %d | 0 |" % (shared["passed"], shared["total"]-shared["passed"]))
    lines += ["", "Formula scans are included in broad/edge assertion totals; shared scans are additional observations, not counted twice.",
              "The structural failure is the qualified Etsy format-documentation discrepancy. Pane getter failures are API observations, not proven bad scrolling.", ""]
    lines += ["| Capacity scenario | calculateAll seconds | Load/calculate/save/read seconds |", "|---|---:|---:|"]
    for scenario in broad["scenarios"]:
        if scenario["id"] in ("oee_capacity", "down_capacity", "pm_examples"):
            lines.append("| %s | %.3f | %.3f |" % (scenario["id"], scenario["calculate_seconds"], scenario["load_calculate_save_read_seconds"]))
    lines += ["", "These stage measurements come from this native run; include import/export/readback rather than claiming instantaneous buyer opening. PM examples are not a full-capacity benchmark.", ""]
    for name, data in lanes:
        lines += ["### " + name, "", "| Scenario | Assertion | Result | Expected / actual evidence |", "|---|---|---|---|"]
        for test in data["tests"]:
            lines.append("| %s | %s | %s | %s |" % (cell(test.get("scenario", "—")), cell(test["test"]), test["status"], cell(test.get("evidence", "source hashes preserved"))))
        lines += ["", "Full evidence (including long formulas/rule inventories) is in the corresponding JSON; table cells are bounded to500 characters.", ""]
    lines += ["### Shared native cell expectations", "", "| Scenario | Cell | Expected | Native actual | Result |", "|---|---|---|---|---|"]
    for scenario in shared["scenarios"]:
        bad = {(v["sheet"],v["cell"]) for v in scenario.get("failures", [])}
        for item in scenario.get("observations", []):
            lines.append("| %s | %s!%s | %s | %s | %s |" % (scenario["scenario"], item["sheet"], item["cell"], cell(item["expected"]), cell(item["actual"]), "FAIL" if (item["sheet"],item["cell"]) in bad else "PASS"))
    report = HERE.parent / "RECHECK-2026-10.md"
    source = report.read_text(encoding="utf-8")
    before, tail = source.split("<!-- RECHECK_TABLES_START -->", 1)
    _, after = tail.split("<!-- RECHECK_TABLES_END -->", 1)
    report.write_text(before + "<!-- RECHECK_TABLES_START -->\n" + "\n".join(lines) + "\n<!-- RECHECK_TABLES_END -->" + after, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
