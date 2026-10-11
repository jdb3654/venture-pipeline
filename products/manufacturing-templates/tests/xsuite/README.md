# Cross-app test suite (Excel, Google Sheets, OpenOffice/LibreOffice)

One set of scenarios, checked the same way in every spreadsheet app. Claude and Codex both use it. We only claim
an app is supported on the listings when its latest run passes in full, the result is recorded below,
and broader review findings affecting that app have been resolved. A shared-suite pass covers these scenarios only.

## How it works

1. **Make the scenarios.** `python3 scenarios.py make <in>` copies each shipped workbook from `dist/`, types test
   data into the yellow cells, and writes `<in>/expected.json`. Expected values come from an independent Python model
   in `scenarios.py`, not from the workbooks' formulas.
2. **Let the app calculate.** Open every `<in>/*.xlsx` in the app and save or download it back as `.xlsx` into an
   output folder, keeping the file names. The app stores its own calculated results in each file.
3. **Check.** `python3 check.py <in>/expected.json <out> --app "<app and version>" --json <out>/results.json`.
   It reads the saved results, so it doesn't care which app produced them.

## Per app

**OpenOffice or LibreOffice (automatic).**
`python3 run_soffice.py <path to soffice> <in> <out>`. Example on Windows with Apache OpenOffice:
`python run_soffice.py "C:\Program Files (x86)\OpenOffice 4\program\soffice.exe" in out`

Apache OpenOffice 4.1.7 cannot export XLSX. Its native path uses the matching bundled UNO Python,
an isolated profile, and fresh copied inputs. It calls `calculateAll`, saves ODS, closes/reopens it,
then reads values and scans all sheets for formula errors. Run from the repository root:

```powershell
python products/manufacturing-templates/tests/xsuite/scenarios.py make <in>
python products/manufacturing-templates/tests/xsuite/run_native.py <in> <out>
python products/manufacturing-templates/tests/xsuite/check.py <in>/expected.json <out> --app "Apache OpenOffice 4.1.7" --native-readback <out>/office-results.json --json <out>/results.json
```

The same independent cell expectations are checked; this does not emulate Excel or claim an XLSX save
round trip in AOO. Do not use an old native JSON after changing inputs/products. `provenance.json` records
input hashes, preservation and installed version. Both default executable paths are for installed AOO4;
`--soffice` and `--uno-python` accept matching alternatives. If a sandbox blocks local UNO, run the authorized
test outside it. Nothing is installed and the owner's office session is never attached to or terminated.

**Excel for the web (free with a Microsoft account; we use takttools.shop@gmail.com).**
1. Upload the `<in>` files to a OneDrive folder.
2. Open each file in Excel for the web. If it opens read-only or in Protected View, choose Edit. Wait until the
   formulas finish calculating.
3. File > Save As > Download a Copy. Save it into `<out>` with the same file name.

**Google Sheets.**
1. Upload the `<in>` files to a Google Drive folder. Open each with Google Sheets (this converts it).
2. File > Download > Microsoft Excel (.xlsx) into `<out>` with the same file name.

Steps 1–3 for the web apps can be done by hand or by Claude through the owner's browser.

Note: opening an uploaded .xlsx in Sheets without converting ("Office editing" mode) and downloading it returns the original file unchanged, with no recalculated values. Always convert first.

## What the scenarios cover

| Scenario | Checks |
|---|---|
| `oee_examples` | Shipped example rows: per-shift OEE, per-machine and all-machine totals |
| `oee_mixed_cycle_times` | All-machine total with different cycle times and rejects (correct answer 50%; #24) |
| `oee_bad_inputs` | Rejects > total, text in a number cell, zero shift, unknown machine, negative values, performance above 100% (#25) |
| `oee_wildcard_names` | Machine names with `*` and `?` stay separate (#18) |
| `oee_date_filter` | From/To dates are inclusive |
| `down_examples` | Overnight stop, typed minutes, Pareto and By Machine totals |
| `down_machine_filter` | Blank filter includes all machines; a chosen machine includes only that one (#26) |
| `down_unknown_negative_zero` | Unknown reason shown as unclassified, negative minutes rejected, zero minutes not a stop, missing end time, blank machine (#19, #28, #29) |
| `down_wildcard_names` | Machine and reason names with `*` and `~` (#18) |
| `down_dates` | Date filter; rows without a date are left out |
| `oee_setup_duplicates_and_dates` | Repeated Setup machine: first row wins, no doubled totals; undated log row flagged and excluded (#37, #25) |
| `down_setup_duplicates` | Repeated machine and reason in Setup: no negative totals, no doubled Pareto rows (#39, #40) |
| `pm_incomplete_completion` | Completion rows missing asset or task are flagged, not OK (#38) |
| `pm_rules` | Latest completion, earlier date, undated completion, blank/zero/negative frequency, duplicate rows, wildcard asset names, status counts (#18, #20, #30, #31) |

## Results

| Date | App and version | Who ran it | Result |
|---|---|---|---|
| 2026-10-10 | LibreOffice 24.2 (Linux, headless) | Claude | 147/147 pass |
| 2026-10-10 | Apache OpenOffice 4.1.7 (Windows; native UNO/ODS) | Codex | 147/147 pass; no formula errors in any scenario. See results-aoo-4.1.7.json and the broader recheck report for additional defects. |
| 2026-10-10 | LibreOffice 24.2 (Linux, headless), after #37–#40 fixes | Claude | 188/188 pass |
| | Apache OpenOffice 4.1.7, after #37–#40 fixes | Codex | pending re-run |
| 2026-10-11 | Excel for the web (Microsoft 365 personal) | Claude | 188/188 pass; no formula errors. Copies saved with File > Create a Copy > Download a Copy (results-excel-web.json). Visual check: Pareto cumulative line dropped to 0 over empty rows; fixed with a carry-forward helper column and re-checked in Excel. |
| 2026-10-10 | Google Sheets (web; uploaded .xlsx, File > Save as Google Sheets) | Claude | 188/188 pass; no formula errors. Values read from Google's own .xlsx export of each converted sheet (results-google-sheets.json, check.py --native-readback). Visual check found the Production Log OEE colours missing (cross-sheet colour rule); fixed by a hidden same-sheet copy of the target and re-checked in Sheets. |
