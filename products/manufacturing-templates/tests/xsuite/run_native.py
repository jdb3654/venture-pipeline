"""Run the shared scenarios using matching UNO; AOO 4.1 cannot export XLSX.

Inputs remain unchanged. calculateAll -> ODS -> close/reopen -> UNO values.
Use check.py --native-readback <out>/office-results.json to check those values.
"""
import argparse
import json
from pathlib import Path
import shutil
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from run_review import run_office, sha


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("inputs", type=Path)
    ap.add_argument("outputs", type=Path)
    ap.add_argument("--soffice", type=Path, default=Path(r"C:\Program Files (x86)\OpenOffice 4\program\soffice.exe"))
    ap.add_argument("--uno-python", type=Path, default=Path(r"C:\Program Files (x86)\OpenOffice 4\program\python.exe"))
    ap.add_argument("--timeout", type=int, default=3600)
    args = ap.parse_args()
    root = args.outputs.resolve()
    root.mkdir(parents=True, exist_ok=True)
    expected = json.loads((args.inputs / "expected.json").read_text())
    requests, hashes = [], {}
    for scenario, checks in expected.items():
        source = args.inputs / (scenario + ".xlsx")
        target = root / source.name
        if source.resolve() == target:
            raise ValueError("Use different input and output folders")
        hashes[source.name] = sha(source)
        shutil.copyfile(source, target)
        reads = {}
        for check in checks:
            reads.setdefault(check["sheet"], []).append(check["cell"])
        requests.append({"id": scenario, "input": str(target), "read": reads})
    run_office(args, root, requests)
    unchanged = all(sha(args.inputs / name) == digest for name, digest in hashes.items())
    (root / "provenance.json").write_text(json.dumps({
        "soffice": str(args.soffice), "version_ini": (args.soffice.parent / "version.ini").read_text(),
        "input_sha256": hashes, "inputs_unchanged": unchanged,
        "protocol": "calculateAll; store ODS; close; reopen; read UNO; scan all formulas for errors"
    }, indent=2))
    if not unchanged:
        raise RuntimeError("Inputs changed")


if __name__ == "__main__":
    main()
