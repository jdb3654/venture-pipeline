# Manufacturing templates (Validate stage)

Product assets for [the manufacturing templates opportunity](../../opportunities/manufacturing-templates.md). These live here only while the idea is being validated; if it moves to Build or Operate, it gets its own repository, per `AGENTS.md`.

- `dist/`: the three workbooks to upload.
- `build.py`: generates the workbooks. Change the template here, not by hand, so the files stay reproducible.
- `preview.py`: renders one PNG per sheet for listing images.
- `previews/`: current screenshots.
- `LISTING.md`: Etsy listing copy, prices and tags.
- `guides/`: step-by-step PDF guides for buyers, one per template plus a combined bundle guide. Built by `build_guides.py` from screenshots made with `preview.py ... 220`. Rebuild them whenever a workbook changes; every limit, column and message in them comes from `build.py`.

## Rebuild and check

```sh
python3 build.py
python3 <xlsx skill>/scripts/recalc.py dist/<file>.xlsx      # must report zero errors
python3 preview.py <xlsx skill>/scripts/office/soffice.py <output dir>
```

## Verified on 2026-10-10

- All three files recalculate in LibreOffice with zero formula errors.
- Example-row OEE values per shift and per machine, the all-machines total, and the date filter match an independent Python calculation.
- Downtime: overnight stop (23:40–00:25 = 45 min), typed-minutes override, Pareto ranking and cumulative %, date + machine filter, and per-machine totals match hand calculation.
- PM schedule: completions in the log update last-completed and next-due dates; statuses and counts are correct for the example rows.

Not yet verified: opening the files in Microsoft Excel itself (built with Excel 2007-era functions only) and in Google Sheets.
