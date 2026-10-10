# Native visual evidence — 2026-10-10

These PNGs render bounded test-only PDF exports from the owner's Apache
OpenOffice 4.1.7. They are not replacement product previews. Print areas were
limited for inspection; these images do not audit original workbook pagination.

- `original_oee`, `original_down`, `original_pm`: byte-for-byte shipped XLSX
  copies, recalculated in soffice. Observe raw errors/blank Pareto and PM colours.
- `diagnostic_oee_target_0.95`, `diagnostic_oee_target_0.5`: **test-only IFERROR
  substitution**, 95% target yields amber and 50% yields green. Passing colours
  do not establish compatibility of the shipped OEE workbook.
- `down_ranking`: selected M1; 30 configured reasons, a zero-minute reason,
  stable 100-minute ties, top 12 bars and cumulative line on the right axis.
  Chart ends below 100% because it shows only the top 12 of 29 positive reasons.

Reproduce with run_review.py/probe_visuals.py and inspect_images.py as described
in the parent README. These images were inspected at full size. Generic AOO
Pareto legend labels and sparse OEE category labels remain readability issues.
