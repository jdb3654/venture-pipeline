# Re-run the adversarial review on Windows

Run from the repository root. The default program is Apache OpenOffice
`C:\Program Files (x86)\OpenOffice 4\program\soffice.exe`, using its bundled
UNO Python. Microsoft Excel is never invoked. No production files are edited.

Use Python 3.8 or later with `openpyxl`. On the review machine the already
installed Codex runtime supplied Python and openpyxl; nothing was installed.
If openpyxl is missing, the owner explicitly approved this repo-local option:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install openpyxl
.\.venv\Scripts\python.exe products/manufacturing-templates/tests/run_review.py
.\.venv\Scripts\python.exe products/manufacturing-templates/tests/static_audit.py
```

Use `--output <path>` to avoid replacing the committed dated evidence, or use
the default `tests/results.json` and review its diff. The default uses a
disposable OS temporary folder and removes it when the run completes. To
retain the inputs, recalculated ODS, raw native results, logs and PDF evidence:

```powershell
python products/manufacturing-templates/tests/run_review.py --work-dir "$env:TEMP\templates-review" --output "$env:TEMP\templates-review-results.json"
```

Allow up to an hour for the complete suite on this Windows/AOO installation.
Every scenario writes inputs with Python,
opens the copy in a separate headless soffice instance/profile, calls
`calculateAll`, saves as ODS, closes, reopens, and reads values using UNO. AOO
4.1.7 does not save XLSX; ODS is the read-back format. Original-baseline
scenarios use byte-for-byte copies, without an openpyxl save. A native formula
error scan uses the actual UNO `FormulaResult.ERROR` constant; empty
preallocated rows are included. Numeric assertions have an absolute tolerance
of 1e-8. The source XLSX SHA-256 values are recorded and checked after execution.

**Exit 1 is expected while product defects remain.** PASS and FAIL are
acceptance results, not a claim that the runner crashed. BLOCKED means a native
scenario could not be executed. Do not hide these failures behind expected-fail
decorators. Each assertion has an independent expected value or stated
acceptance condition and includes the actual native result. Date-dependent
tests compare with the actual office host date, recorded in the environment.
The dated report uses the owner's America/Chicago date.

`diagnostic_oee_*` scenarios expand only `IFERROR(expr, "")` into the equivalent
`IF(ISERROR(expr), "", expr)` **in temporary test copies** because AOO 4.1.7
does not recognize the shipped IFERROR formulas. They isolate deeper input and
aggregation bugs. Passing diagnostic tests do not establish compatibility of
the shipped product. No product fix is included in this PR. Original and
diagnostic assertion totals are reported separately.

`--only oee_capacity` (or another scenario prefix) runs a bounded retest.
`--reuse-inputs` is for bridge diagnostics using already prepared inputs in
`--work-dir`; omit it for a fresh acceptance run after product changes.
`--readback-results <office-results.json>` re-evaluates assertions on the same
run's actual UNO readback (use with `--reuse-inputs` and its retained work folder).
It is not a new native run and never reads XLSX cached values; do not use old
results as proof for changed product files or a different host date.

For LibreOffice, supply **both** paths:

```powershell
python products/manufacturing-templates/tests/run_review.py --soffice 'C:\Program Files\LibreOffice\program\soffice.exe' --uno-python '<Python executable with the matching LibreOffice pyuno module>' --output "$env:TEMP\libreoffice-results.json"
```

LibreOffice Windows installations do not necessarily bundle UNO Python. This
runner requires a matching UNO-enabled interpreter already available; a normal
Python/openpyxl environment alone is insufficient. Do not install another suite
or dependency to make that command work without the owner's authorization.
LibreOffice was not executed for this review. The report's LibreOffice and
Excel results are explicitly unverified.

If the agent sandbox prevents the local listener connection, run the authorized
test outside that sandbox; a normal Windows terminal has no agent sandbox.
The listener is bound only to 127.0.0.1 on a temporary port, uses its own
profile, disables macros/document updates, and is terminated at the end. The
runner never attaches to or closes the owner's open office session. If an
abnormal exit leaves a listener, identify its command line/profile before
stopping it; do not kill all soffice processes.

Optional visual diagnostics, using already installed Pillow/pypdfium2:

```powershell
python products/manufacturing-templates/tests/inspect_images.py "$env:TEMP\templates-review"
```

This renders native PDFs and creates 280-pixel square-crop/full-sheet-fit
contact sheets from all 12 existing previews. It edits no listing images.
The native feature inventory verifies imported list-validation definitions,
conditional rules/styles, chart series types/axes/data and frozen-pane
positions. Headless inspection cannot prove an interactive drop-down click;
that limit is explicit in the review.

Structural and new-guide checks (read-only, using already installed pypdf and
Poppler for the optional guide lane):

```powershell
python products/manufacturing-templates/tests/static_audit.py
python products/manufacturing-templates/tests/check_static.py
python products/manufacturing-templates/tests/review_documents.py --work-dir "$env:TEMP\guide-review"
python products/manufacturing-templates/tests/write_result_tables.py
```

The document audit compares local PDF bytes with committed Git blobs, checks
strict parsing and metadata, and renders all guide pages without repairing them.
The static wildcard checks are structural inferences from Microsoft docs, not
an Excel simulation; review alternatives if formulas are refactored. Etsy format
checks examine the delivery paragraph but do not authenticate or upload files.

For supplemental target-colour and populated Pareto PDF inspection after a
retained main run, use a different work folder:

```powershell
python products/manufacturing-templates/tests/probe_visuals.py --from-work-dir "$env:TEMP\templates-review" --work-dir "$env:TEMP\templates-visual-review"
python products/manufacturing-templates/tests/inspect_images.py "$env:TEMP\templates-visual-review"
```

Visual cases are additional observations, not counted a second time as the same
numeric assertions. Diagnostic OEE colour output remains test-only.
