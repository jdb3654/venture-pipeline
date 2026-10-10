"""Read-only buyer-guide integrity, metadata and rendering audit.

Uses preinstalled pypdf and Poppler. No PDF is generated or repaired. Git blob
comparison distinguishes a damaged Windows checkout from the committed bytes.
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
PRODUCT = HERE.parent
REPO = PRODUCT.parents[1]


def xref_ok(data):
    match = re.search(rb"startxref\s+(\d+)\s+%%EOF", data)
    if not match:
        return False, {"reason": "no startxref"}
    offset = int(match.group(1))
    return data[offset:offset + 4] == b"xref", {"offset": offset,
        "bytes_at_offset": repr(data[offset:offset + 20]),
        "actual_xref_offset": next((m.start() for m in re.finditer(rb"(?m)^xref\r?$", data)), -1)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--work-dir", type=Path, required=True)
    parser.add_argument("--pdftoppm", default=shutil.which("pdftoppm"))
    args = parser.parse_args()
    args.work_dir.mkdir(parents=True, exist_ok=True)
    tests, inventory = [], []

    def check(name, ok, evidence):
        tests.append({"test": name, "status": "PASS" if ok else "FAIL", "evidence": evidence})

    for path in sorted((PRODUCT / "guides").glob("*.pdf")):
        relative = path.relative_to(REPO).as_posix()
        data = path.read_bytes()
        blob = subprocess.check_output(["git", "show", "HEAD:" + relative], cwd=REPO)
        info = {"file": path.name, "checkout_sha256": hashlib.sha256(data).hexdigest(),
                "git_sha256": hashlib.sha256(blob).hexdigest(), "bytes": len(data)}
        for label, content in [("checkout", data), ("committed blob", blob)]:
            ok, evidence = xref_ok(content)
            check(path.name + " " + label + " cross-reference offset", ok, evidence)
            try:
                reader = PdfReader(io.BytesIO(content), strict=True)
                pages = len(reader.pages)
                check(path.name + " " + label + " strict PDF parse", True, {"pages": pages})
            except Exception as exc:
                check(path.name + " " + label + " strict PDF parse", False, str(exc))
        # Recovery parsing is intentionally separate from the strict acceptance test.
        reader = PdfReader(io.BytesIO(data), strict=False)
        info.update({"pages": len(reader.pages), "metadata": dict(reader.metadata or {})})
        text = "\n".join(p.extract_text() for p in reader.pages)
        info["text"] = text
        suspicious = re.findall(r"(?i)(?:[A-Z]:[\\/]|/home/|/Users/|Joey|jdb3654)",
                                json.dumps(info["metadata"]) + text)
        check(path.name + " no owner identifiers or local paths", not suspicious,
              {"suspicious": suspicious, "author": info["metadata"].get("/Author")})
        check(path.name + " explicitly clears yellow example cells only",
              "yellow" in text and "Don't delete whole rows" in text,
              "Guide instructs clearing yellow cells and retaining formula rows")
        if args.pdftoppm:
            prefix = args.work_dir / path.stem
            rendered = subprocess.run([args.pdftoppm, "-r", "80", "-png", str(path), str(prefix)],
                                      capture_output=True, text=True)
            pages = [p for p in args.work_dir.glob(path.stem + "-*.png")
                     if re.search(r"-\d+\.png$", p.name)]
            check(path.name + " recovery rendering of every page", rendered.returncode == 0 and
                  len(pages) == info["pages"], {"returncode": rendered.returncode,
                  "pages_rendered": len(pages), "stderr_first_1000_chars": rendered.stderr[:1000],
                  "stderr_line_count": len(rendered.stderr.splitlines())})
        else:
            tests.append({"test": path.name + " render", "status": "BLOCKED",
                          "evidence": "Poppler not installed; no installation attempted"})
        inventory.append(info)
    result = {"tests": tests, "guides": inventory,
              "summary": {s: sum(t["status"] == s for t in tests) for s in ("PASS", "FAIL", "BLOCKED")}}
    (HERE / "document-results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result["summary"]))
    for test in tests:
        if test["status"] != "PASS":
            print(test["test"], test["status"], test["evidence"])
    return int(result["summary"]["FAIL"] > 0 or result["summary"]["BLOCKED"] > 0)


if __name__ == "__main__":
    raise SystemExit(main())
