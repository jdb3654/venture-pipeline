"""Recalculate scenario files with an installed OpenOffice or LibreOffice and save them as .xlsx.

    python3 run_soffice.py <soffice executable> <scenario dir> <out dir>

Uses headless conversion, which loads each file, recalculates every formula and writes the results.
On Windows, point it at e.g. "C:\\Program Files (x86)\\OpenOffice 4\\program\\soffice.exe".
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

soffice, src, out = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)
profile = Path(tempfile.mkdtemp(prefix="xsuite-profile-"))
for f in sorted(src.glob("*.xlsx")):
    subprocess.run([soffice, f"-env:UserInstallation={profile.as_uri()}", "--headless", "--calc",
                    "--convert-to", "xlsx:Calc MS Excel 2007 XML", "--outdir", str(out), str(f)],
                   check=True, capture_output=True, timeout=600)
    print("recalculated", f.name)
shutil.rmtree(profile, ignore_errors=True)
