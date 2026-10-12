"""Check PIPELINE.md and opportunities/ for the evidence rules CI can see.

    python scripts/check_opportunities.py      exit 1 on any failure not listed in the exemptions file

Fails when:
- a relative link in PIPELINE.md points to a missing file;
- an opportunity file whose Stage line starts with "Screen" has an empty score
  (or no Scores table), or a score justification whose only label is [assume]
  and that has no link.

Known failures are listed, one per line, in scripts/check_opportunities_exemptions.txt
(the exact text this script prints). Fix the file and delete its line in the
same PR: a leftover line also fails, so it can't hide a later regression.
Standard library only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXEMPTIONS = ROOT / "scripts" / "check_opportunities_exemptions.txt"
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
LABEL = re.compile(r"\[([a-z][^\]]*)\](?!\()")
STAGE = re.compile(r"^\s*-\s*\*\*Stage:\*\*\s*(.*)$", re.M)


def pipeline_links():
    failures = []
    for target in LINK.findall((ROOT / "PIPELINE.md").read_text(encoding="utf-8")):
        if re.match(r"[a-z][a-z0-9+.-]*:", target, re.I) or target.startswith("#"):
            continue
        path = target.split("#")[0]
        if path and not (ROOT / path).exists():
            failures.append("PIPELINE.md: missing link target %s" % path)
    return failures


def scores(text):
    """Yield (factor, score, justification) rows of the ## Scores table, or None if absent."""
    m = re.search(r"^##\s+Scores\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    if not m:
        return None
    rows = []
    for line in m.group(1).splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or cells[0].lower() == "factor" or set(cells[0]) <= set("-: "):
            continue
        rows.append((cells[0], cells[1], "|".join(cells[2:])))
    return rows


def screen_files():
    failures = []
    for f in sorted((ROOT / "opportunities").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        stage = STAGE.search(text)
        if not stage or not stage.group(1).startswith("Screen"):
            continue
        name = f.relative_to(ROOT).as_posix()
        rows = scores(text)
        if not rows:
            failures.append("%s: no Scores table" % name)
            continue
        for factor, score, why in rows:
            if not score:
                failures.append("%s: empty score: %s" % (name, factor))
            labels = {re.match(r"[a-z]+", l).group(0) for l in LABEL.findall(why)}
            if labels == {"assume"} and not (LINK.search(why) or "http" in why):
                failures.append("%s: [assume] only, no link: %s" % (name, factor))
    return failures


def main():
    failures = pipeline_links() + screen_files()
    exempt = set()
    if EXEMPTIONS.exists():
        exempt = {l.strip() for l in EXEMPTIONS.read_text(encoding="utf-8").splitlines()
                  if l.strip() and not l.startswith("#")}
    new = [f for f in failures if f not in exempt]
    new += ["exemption no longer needed, delete its line: %s" % stale
            for stale in sorted(exempt - set(failures))]
    if new:
        print("FAILED:\n- " + "\n- ".join(new))
        return 1
    print("OK: %d checks failed but are exempted" % len(failures) if failures else "OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
