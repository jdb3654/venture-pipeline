"""Render one PNG per sheet from the built workbooks, for listing images.

Run after build.py and a LibreOffice recalc: python3 preview.py <soffice.py path> <out dir> [dpi, default 110]
Works on copies, so the files in dist/ are left untouched.
"""
import shutil
import subprocess
import sys
from pathlib import Path

from openpyxl import load_workbook

AREAS = {
    "OEE-Tracker.xlsx": {"How to use": "A1:B30", "Setup": "A1:C10", "Production Log": "A1:T12",
                         "Dashboard": "A1:L48"},
    "Downtime-Log-and-Pareto.xlsx": {"How to use": "A1:B25", "Setup": "A1:E18", "Downtime Log": "A1:K13",
                                     "Pareto": "A1:Z24", "By Machine": "A1:E9"},
    "Preventive-Maintenance-Schedule.xlsx": {"How to use": "A1:B25", "PM Plan": "A1:L11",
                                             "Completion Log": "A1:F7"},
}

soffice, out = sys.argv[1], Path(sys.argv[2])
dpi = sys.argv[3] if len(sys.argv) > 3 else "110"
out.mkdir(parents=True, exist_ok=True)
dist = Path(__file__).parent / "dist"
for name, areas in AREAS.items():
    copy = out / name
    shutil.copy(dist / name, copy)
    wb = load_workbook(copy)
    for ws in wb.worksheets:
        ws.print_area = areas[ws.title]
        ws.page_setup.orientation = "landscape"
        ws.page_setup.fitToWidth = ws.page_setup.fitToHeight = 1
        ws.sheet_properties.pageSetUpPr.fitToPage = True
    wb.save(copy)
    subprocess.run([sys.executable, soffice, "--headless", "--convert-to", "pdf", "--outdir", str(out), str(copy)],
                   check=True, capture_output=True)
    pdf = copy.with_suffix(".pdf")
    subprocess.run(["pdftoppm", "-png", "-r", dpi, str(pdf), str(out / copy.stem)], check=True)
    print("rendered", name)
