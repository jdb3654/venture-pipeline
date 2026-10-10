"""Regenerate the report's complete result tables from dated evidence files."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPORT = HERE.parent / "REVIEW-2026-10.md"


def escape(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def main():
    native = json.loads((HERE / "results.json").read_text())
    static = json.loads((HERE / "static-checks.json").read_text())
    documents = json.loads((HERE / "document-results.json").read_text())
    groups = [("Shipped-formula native tests", [t for t in native["tests"] if not t["scenario"].startswith("diagnostic_")], "results.json"),
              ("TEST-ONLY OEE compatibility substitutions", [t for t in native["tests"] if t["scenario"].startswith("diagnostic_")], "results.json"),
              ("Structural checks (not native Excel execution)", static["tests"], "static-checks.json"),
              ("New buyer-guide checks", documents["tests"], "document-results.json")]
    output = []
    total = {s: 0 for s in ("PASS", "FAIL", "BLOCKED")}
    for title, tests, filename in groups:
        counts = {s: sum(t["status"] == s for t in tests) for s in total}
        for s in total:
            total[s] += counts[s]
        output += ["### " + title, "", "%d assertions: %d PASS, %d FAIL, %d BLOCKED. [Detailed evidence](tests/%s)." %
                   (len(tests), counts["PASS"], counts["FAIL"], counts["BLOCKED"], filename), "",
                   "| Scenario | Every assertion | Result |", "|---|---|---|"]
        output += ["| %s | %s | **%s** |" % (escape(t.get("scenario", "static/document")),
                    escape(t["test"]), t["status"]) for t in tests]
        output += [""]
    header = ["**Total: %d assertions — %d PASS, %d FAIL, %d BLOCKED.**" %
              (sum(total.values()), total["PASS"], total["FAIL"], total["BLOCKED"]), "",
              "Native suite: %d scenarios, %.2f seconds summed load/calculate/save/read time. "
              "Formula calculation timings are reported separately below." %
              (len(native["scenarios"]), native["native_elapsed_seconds"]), ""]
    output += ["### Capacity timing (native OpenOffice 4.1.7)", "",
               "| Scenario | calculateAll seconds | Load/calculate/save/read seconds |", "|---|---:|---:|"]
    for scenario in native["scenarios"]:
        if "capacity" in scenario["id"]:
            output.append("| %s | %.3f | %.3f |" % (scenario["id"], scenario["calculate_seconds"], scenario["load_calculate_save_read_seconds"]))
    output += ["", "The fast calculateAll call follows import calculation; full-operation timing includes import, ODS serialization and reopening. Raw OEE calculation speed is not evidence of correct output.", ""]
    text = REPORT.read_text(encoding="utf-8")
    before, rest = text.split("<!-- BEGIN GENERATED RESULTS -->")
    _, after = rest.split("<!-- END GENERATED RESULTS -->")
    REPORT.write_text(before + "<!-- BEGIN GENERATED RESULTS -->\n" + "\n".join(header + output) +
                      "\n<!-- END GENERATED RESULTS -->" + after, encoding="utf-8")
    print(total)


if __name__ == "__main__":
    main()
