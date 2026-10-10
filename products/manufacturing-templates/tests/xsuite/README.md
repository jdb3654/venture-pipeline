# Cross-app test suite (Excel, Google Sheets, OpenOffice/LibreOffice)

One set of scenarios, checked the same way in every spreadsheet app. Claude and Codex both use it. We only claim
an app is supported on the listings when its latest run passes in full, and the result is recorded below.

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

**Excel for the web (free with a Microsoft account; we use takttools.shop@gmail.com).**
1. Upload the `<in>` files to a OneDrive folder.
2. Open each file in Excel for the web. If it opens read-only or in Protected View, choose Edit. Wait until the
   formulas finish calculating.
3. File > Save As > Download a Copy. Save it into `<out>` with the same file name.

**Google Sheets.**
1. Upload the `<in>` files to a Google Drive folder. Open each with Google Sheets (this converts it).
2. File > Download > Microsoft Excel (.xlsx) into `<out>` with the same file name.

Steps 1–3 for the web apps can be done by hand or by Claude through the owner's browser.

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
| `pm_rules` | Latest completion, earlier date, undated completion, blank/zero/negative frequency, duplicate rows, wildcard asset names, status counts (#18, #20, #30, #31) |

## Results

| Date | App and version | Who ran it | Result |
|---|---|---|---|
| 2026-10-10 | LibreOffice 24.2 (Linux, headless) | Claude | 147/147 pass |
| | Apache OpenOffice 4.1.7 (Windows) | Codex | pending |
| | Excel for the web | | pending |
| | Google Sheets | | pending |
