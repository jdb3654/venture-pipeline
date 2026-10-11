# Manufacturing templates: verification after fixes — 2026-10-10

Recheck requested by the owner and [#36](https://github.com/jdb3654/venture-pipeline/issues/36), following [#11](https://github.com/jdb3654/venture-pipeline/issues/11). Product baseline: main `0f5e59dfa366ba7bcb324215d259477af0a45a05`, including merged fixes [#34](https://github.com/jdb3654/venture-pipeline/pull/34) and [#35](https://github.com/jdb3654/venture-pipeline/pull/35). The original [review](REVIEW-2026-10.md) and JSON remain historical evidence. No product source, XLSX, guide, listing or preview is repaired in this recheck PR.

Most original defects have been fixed. The shared suite passes **147/147** expected cells in installed **Apache OpenOffice 4.1.7, Windows, build 417m1(Build:9800)**; none of its eleven scenarios has a formula error. All **28/28 PDF checks** pass, with every guide page rendered. Extra adversarial cases still find misleading OK messages and silently incorrect duplicate-key totals. Do not interpret the shared-suite pass as permission to publish or as complete OpenOffice support certification.

## Protocol and limitations

Python 3.12.14 / openpyxl 3.1.5 supplied by the existing Codex runtime, matching OpenOffice bundled Python 2.7 / UNO, installed soffice at `C:\Program Files (x86)\OpenOffice 4\program\soffice.exe`. No dependencies installed. Native tests operate on freshly generated copies in `.review-executed/recheck-main`, `recheck-xsuite` and `recheck-edges`; isolated profiles/listeners, macros and external updates disabled. `calculateAll` → save ODS → close → reopen → actual UNO values, plus formula-error scan of all sheets/empty rows. Product hashes are checked by the main suite. XLSX caches from the builder are never used as results.

AOO 4.1.7 cannot export XLSX, so the shared `run_soffice.py` XLSX-conversion path is unsuitable here. `xsuite/run_native.py` and `check.py --native-readback` check the **same independent 147 expectations**, using native ODS readback and retained provenance instead. No XLSX round trip, Excel execution or Google Sheets/LibreOffice execution is claimed. Claude's recorded LibreOffice 24.2 run is a separate agent's evidence.

Expectations were reconciled with #35 independently: aggregate Quality = ideal-good time / ideal-total time; zero output is a valid 0% OEE shift; performance >100% is a warning that retains the row; PM has a grey Needs-fixing colour. Removed IFERROR means no redundant test-only compatibility scenarios. Any assertion re-evaluation uses **this run's** freshly calculated UNO JSON, not older baseline data. Numerical tolerance remains 1e-8 in the broad suite and 0.0005 in the shared suite.

Interactive verification was attempted with disposable byte copies, separate profiles and the installed Windows Computer Use skill. The first OEE GUI window became unresponsive; a fresh read-only retry without accessibility scanning also became unresponsive, and window activation timed out. A third standalone retry after all headless tests stopped returned a ready dashboard screenshot, but its scroll call also timed out and the window then reported Not Responding. Only those identified disposable UI processes were stopped. The initial dashboard screenshot showed the boundary below row 8, but no successful scroll was established. **Frozen-header scrolling and interactive dropdown use remain unverified**; #27 stays open. This does not establish malformed OOXML or a reproducible standalone application bug, because automation/input failures could contribute; the standalone attempt removes concurrent headless testing as an explanation for that attempt. Headless pane getters, validation definitions and chart types are reported separately.

## Fix verification and remaining queue

| Issue | Current assessment |
|---|---|
| [#15](https://github.com/jdb3654/venture-pipeline/issues/15) PDF corruption | Fixed: all four working PDFs match Git blobs, binary attributes applied, strict parsing/xref and all 22 pages render. No forced delete needed for these fresh copies. |
| [#17](https://github.com/jdb3654/venture-pipeline/issues/17) IFERROR | Fixed: exact-equality SUMPRODUCT replaces unsupported IFERROR paths; native shared OEE/downtime scenarios pass. |
| [#18](https://github.com/jdb3654/venture-pipeline/issues/18) wildcards | Fixed in tested AOO cases; structural Excel defect removed by equality instead of wildcard criteria. Actual Excel execution still pending. |
| [#19](https://github.com/jdb3654/venture-pipeline/issues/19) unknown reason | Fixed: unknown minutes count in total and Unclassified. Duplicate Setup reasons are a new distinct problem, #39. |
| [#20](https://github.com/jdb3654/venture-pipeline/issues/20), [#30](https://github.com/jdb3654/venture-pipeline/issues/30), [#31](https://github.com/jdb3654/venture-pipeline/issues/31) PM | Original frequency/duplicate-plan/undated-completion cases fixed. Text completion dates also warn without errors. Date-only completion with blank names still says OK (#38). |
| [#21](https://github.com/jdb3654/venture-pipeline/issues/21) instructions | Reopened: Dashboard!A6 says every non-OK row is excluded, but performance warnings count. At 40% OEE/30% target cells are red while guide promises green at/above target. Explain aggregate time-weighted Quality separately from shift good/total Quality. |
| [#24](https://github.com/jdb3654/venture-pipeline/issues/24) mixed-cycle OEE | Fixed: the strong Slow/Fast counterexample is 50%, rather than 9.09%. |
| [#25](https://github.com/jdb3654/venture-pipeline/issues/25) OEE validation | Original numeric/time/reject checks and >100% warning fixed; reopened for missing Date: R5 says OK and Q5=40%, but row disappears from dashboard even with blank filters. |
| [#26](https://github.com/jdb3654/venture-pipeline/issues/26), [#28](https://github.com/jdb3654/venture-pipeline/issues/28), [#29](https://github.com/jdb3654/venture-pipeline/issues/29) downtime | Original blank machine filter, positive-duration stop counts and negative-minute rejection fixed. |
| [#27](https://github.com/jdb3654/venture-pipeline/issues/27) panes | Open: native getter results in the assertion table; interactive scrolling not established. Preserve valid XML rather than guessing at a repair. |
| [#16](https://github.com/jdb3654/venture-pipeline/issues/16) delivery format | Still a documentation/live-record conflict; no upload/buyer-flow test authorized. Current official list omits XLSX, management records say attached. |
| [#22](https://github.com/jdb3654/venture-pipeline/issues/22) thumbnails | Wording/tags corrected, limits pass; repository thumbnails still 1287×910, square crops cut titles/labels and results remain tiny. Separate canvas not reviewed. |
| [#23](https://github.com/jdb3654/venture-pipeline/issues/23) policy | Bounded draft now exists; approval remains owner work. Correct unavailable “digital-item return settings” instruction. |

New reproducible issues, labeled agent:claude/stage:validate:

| Issue / native scenario | Independent expectation | Actual fresh AOO result |
|---|---|---|
| [#37](https://github.com/jdb3654/venture-pipeline/issues/37) `edge_oee_duplicate_machine` | A60-second M1 cycle, 24 good parts / 60 planned minutes gives40%, or an explicit duplicate warning | M1 entered twice → 120-second cycle, Check = OK,80% OEE; dashboard duplicates counts/time. |
| [#38](https://github.com/jdb3654/venture-pipeline/issues/38) `edge_pm_missing_key` | Date without asset/task must warn | CompletionF5=OK because blank plan keys match; plan remains unchanged. |
| [#39](https://github.com/jdb3654/venture-pipeline/issues/39) `edge_down_duplicate_reason` | Unique allocation or explicit duplicate warning; nonnegative Unclassified | One 10-minute R1 stop, R1 listed twice → Unclassified −10 and cumulative 200%, Check = OK. |
| [#40](https://github.com/jdb3654/venture-pipeline/issues/40) `edge_down_duplicate_machine` | Unique allocation or explicit duplicate warning; nonnegative other minutes | One 10-minute M1 stop, M1 listed twice →No machine/not in Setup −10, Check = OK. |

## Documentation, listings and visual claims

All 22 PDF pages inspected after rendering: no missing pages/overlap detected. Yellow-cell clearing, day-based rather than calendar intervals, never-done tasks staying due today, new validation messages and Unclassified accounting are substantially improved. OEE Step2 heading is still orphaned on p1; formula table spans p3/p4; PM p3 and bundle p11 remain sparse. These layout items can wait behind calculation fixes. Screenshot captions are broadly accurate, but instructions/colour conflicts above must be corrected. Aggregate Quality deserves a clearly scoped explanation rather than a generic formula that applies only within one cycle time.

| Listing claim (applies to bundle and relevant singles) | Current verdict |
|---|---|
| Per-shift A/P/Q/OEE; date-range machine dashboard | True for tested valid numeric/date inputs; missing Date is a validation hole, not a date-filter failure. |
| Totals weighted correctly instead of averaged percentages | True for unique Setup names; mixed-cycle and unequal-shift scenarios pass. False without duplicate-key protection when users repeat a machine. |
| Custom target; colours follow target | Numeric gap and 95%/50% examples verified. Guide's universal green-at-target sentence false for a 30% target with40% OEE. |
| Common-entry Check column | Improved; misleading OK remains on undated OEE and incomplete PM completion rows. It must not imply comprehensive validation. |
| Overnight/typed downtime, dropdown lists, automatic Pareto/cumulative %, machine/date filters | Calculations and native list definitions pass for unique Setup lists. Duplicates can create impossible negative buckets/200% shares. Interactive dropdown clicking remains unverified. |
| PM latest completion/next due/status counts/colours | Core and original invalid-frequency/duplicate-plan cases pass; date-only blank-key completion warning is false. Native colour definitions and normal screenshots checked separately. |
| No macros or add-ins | True structurally; no external links/owner identifiers/paths detected. |
| Works in existing spreadsheet app | Overbroad standalone phrase; “Works in” placeholder correctly prevents publication until precise tested support is approved. Shared AOO pass does not resolve broader defects or GUI verification. |
| Instant download / files attached | Buyer delivery unverified; LISTING explicitly says Etsy drafts still carry old files/copy. No Etsy login, upload or publication performed. |
| Guide, examples and stated capacities | Present; guides intact.500 OEE/1000 downtime rows recalculated; PM300/2,000 capacity is a structural bound, not a new full-capacity timing test. |
| AI-designed and seller checked | Disclosure present. Seller expertise/personal checking is a firsthand owner/management assertion, not independently proved by this review. |
| Titles/tags | All 4 meet limits. Unsupported shift-report/work-order/root-cause and notification wording removed. Vocabulary relevance is an editorial hypothesis; search volume/conversion remains unverified. |

Fresh native exports: OEE95% target amber and50% target green; low-target 40%/30% red evidence retained at `tests/evidence/recheck-low-target.png`. Populated Pareto shows actual bars and cumulative line on right 0–100% axis; top 12 cumulative remains71.9% when additional reasons exist, correctly using all reasons as denominator. Generic legend names “Column C/F” and OEE chart showing only first machine label remain readability improvements (#22), not evidence of wrong underlying series values. Native print areas are bounded review exports, not promised product print pagination or new Etsy preview images.

Public primary sources rechecked 2026-10-10: [Etsy digital listings](https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Manage-Your-Digital-Listings) still lists ZIP/PDF, not XLSX, with5 files / 20MB each; this does not override the contradictory firsthand attachment record. [Etsy digital return policy guidance](https://help.etsy.com/hc/en-gb/articles/7869401615255-How-do-I-Set-Return-Policies-on-My-Listings) says digital return/exchange settings cannot be set; seller issue resolution is separate. POLICY should use appropriate approved copy locations, not promise nonexistent controls. No legal conclusion or money action is made here. Earlier primary-source title/tag/AI/image and Excel2010 support research remains in the historical review; no new authenticated SEO or cross-app evidence acquired.

## Excel2010 structural audit

The revised Excel2010 structural audit is separate from native AOO execution:

| Component | Current inventory / confidence |
|---|---|
| Functions | AND, COUNTIF, DATE, FALSE, IF, INDEX, ISNUMBER, LARGE, MATCH, MAX, MOD, N, NOT, OR, ROUND, ROW, SUM, SUMPRODUCT, TODAY, TRUE. All are established functions without post2010 markers in [Microsoft's catalogue](https://support.microsoft.com/en-us/excel/excel-functions-alphabetical), checked2026-10-10. Function availability is high-confidence; complete formula behavior is unverified in Excel. No newer-function prefixes in source. |
| Arrays / lookups | Exact equality in SUMPRODUCT removes wildcard criteria in changed lookups. Nested SUMPRODUCT(MAX(array)) PM/date and category-row selection still need actual Excel execution; AOO passing does not certify Excel array evaluation. Formula-text inventory now strips quoted warning messages instead of mistaking words like MORE/REASON for functions. |
| Conditional formatting | Legacy expression rules with numeric/Boolean/equality tests; OEE target reference across sheets, PM fourth grey invalid-status rule and OEE stopIfTrue priority. Structurally plausible in2010, with earlier cross-sheet source caveat; all native styles import. Low-target color contradiction remains a product issue. No claim that four rules imply Excel2003 compatibility. |
| Validation | Native imported list definitions, whole/decimal constraints and between/greater bounds, no new Excel function dependency. Same-workbook cross-sheet list references remain medium-confidence for2010 pending a real open/save; imported definitions alone do not prove dropdown interaction/enforcement. Several ShowErrorMessage flags remain false; Check/status logic is the validation defense. |
| Charts | Standard column OEE and column+line Pareto with secondary axis, structurally plausible in2010; native AOO series/axis assertions and populated exports pass. Actual Excel rendering remains unverified. |

No Excel2010/Excel-web/Sheets/LibreOffice test was substituted for the owner's installed soffice. The current listing placeholder correctly avoids a version claim based only on this structural assessment.

## Priority by practical impact

1. **Must fix before publishing:** missing-input OK gaps and duplicate-key corruption (#25/#37–#40), contradictory inclusion/colour instructions (#21), supported-app decision that accounts for broader checks, delivery verification/re-upload of current assets to all drafts, owner policy approval plus the incorrect settings sentence (#23).
2. **Soon:** verify scrolling/dropdown interaction (#27), readable crop-safe heroes and clear chart labels (#22), tighten guide pagination. These can improve trust/clickability without adding a new product platform.
3. **Later:** broader suite versions/platforms, additional templates and search hypotheses only after the 30-day demand test. No evidence here supports a revenue forecast.

## Every automated test

The following generated tables preserve all expected/actual assertions and separate structural policy agreement from executed product calculations. Shared-suite expectations and per-scenario outcomes are also retained in `tests/xsuite/results-aoo-4.1.7.json`; native protocol/input hashes in its provenance file. Historical494-assertion totals are not reused as current results.

<!-- RECHECK_TABLES_START -->
| Lane | PASS | FAIL | BLOCKED |
|---|---:|---:|---:|
| Broad native | 309 | 9 | 0 |
| New native edges | 16 | 5 | 0 |
| Structural / documentation agreement | 15 | 1 | 0 |
| Guide integrity/rendering | 28 | 0 | 0 |
| Shared native expected cells | 147 | 0 | 0 |

Formula scans are included in broad/edge assertion totals; shared scans are additional observations, not counted twice.
The structural failure is the qualified Etsy format-documentation discrepancy. Pane getter failures are API observations, not proven bad scrolling.

| Capacity scenario | calculateAll seconds | Load/calculate/save/read seconds |
|---|---:|---:|
| oee_capacity | 0.309 | 17.983 |
| down_capacity | 0.676 | 28.873 |
| pm_examples | 0.035 | 105.959 |

These stage measurements come from this native run; include import/export/readback rather than claiming instantaneous buyer opening. PM examples are not a full-capacity benchmark.

### Broad native

| Scenario | Assertion | Result | Expected / actual evidence |
|---|---|---|---|
| oee_examples | example shift 5 N | PASS | {"cell": "Production Log!N5", "expected": 0.9204545454545454, "actual": 0.9204545454545454} |
| oee_examples | example shift 5 O | PASS | {"cell": "Production Log!O5", "expected": 0.9382716049382716, "actual": 0.9382716049382716} |
| oee_examples | example shift 5 P | PASS | {"cell": "Production Log!P5", "expected": 0.988421052631579, "actual": 0.988421052631579} |
| oee_examples | example shift 5 Q | PASS | {"cell": "Production Log!Q5", "expected": 0.8536363636363635, "actual": 0.8536363636363636} |
| oee_examples | example shift 6 N | PASS | {"cell": "Production Log!N6", "expected": 0.8636363636363636, "actual": 0.8636363636363636} |
| oee_examples | example shift 6 O | PASS | {"cell": "Production Log!O6", "expected": 0.875, "actual": 0.875} |
| oee_examples | example shift 6 P | PASS | {"cell": "Production Log!P6", "expected": 0.980952380952381, "actual": 0.9809523809523809} |
| oee_examples | example shift 6 Q | PASS | {"cell": "Production Log!Q6", "expected": 0.7412878787878789, "actual": 0.7412878787878788} |
| oee_examples | example shift 7 N | PASS | {"cell": "Production Log!N7", "expected": 0.9431818181818182, "actual": 0.9431818181818182} |
| oee_examples | example shift 7 O | PASS | {"cell": "Production Log!O7", "expected": 0.9236947791164658, "actual": 0.9236947791164658} |
| oee_examples | example shift 7 P | PASS | {"cell": "Production Log!P7", "expected": 0.9836956521739131, "actual": 0.9836956521739131} |
| oee_examples | example shift 7 Q | PASS | {"cell": "Production Log!Q7", "expected": 0.8570075757575758, "actual": 0.8570075757575757} |
| oee_examples | example shift 8 N | PASS | {"cell": "Production Log!N8", "expected": 0.7954545454545454, "actual": 0.7954545454545454} |
| oee_examples | example shift 8 O | PASS | {"cell": "Production Log!O8", "expected": 0.8571428571428571, "actual": 0.8571428571428571} |
| oee_examples | example shift 8 P | PASS | {"cell": "Production Log!P8", "expected": 0.98, "actual": 0.98} |
| oee_examples | example shift 8 Q | PASS | {"cell": "Production Log!Q8", "expected": 0.6681818181818181, "actual": 0.6681818181818182} |
| oee_examples | example shift 9 N | PASS | {"cell": "Production Log!N9", "expected": 0.9545454545454546, "actual": 0.9545454545454546} |
| oee_examples | example shift 9 O | PASS | {"cell": "Production Log!O9", "expected": 0.9047619047619048, "actual": 0.9047619047619048} |
| oee_examples | example shift 9 P | PASS | {"cell": "Production Log!P9", "expected": 0.9916666666666666, "actual": 0.9916666666666667} |
| oee_examples | example shift 9 Q | PASS | {"cell": "Production Log!Q9", "expected": 0.8564393939393938, "actual": 0.856439393939394} |
| oee_examples | example shift 10 N | PASS | {"cell": "Production Log!N10", "expected": 0.875, "actual": 0.875} |
| oee_examples | example shift 10 O | PASS | {"cell": "Production Log!O10", "expected": 0.9090909090909091, "actual": 0.9090909090909091} |
| oee_examples | example shift 10 P | PASS | {"cell": "Production Log!P10", "expected": 0.9886904761904762, "actual": 0.9886904761904762} |
| oee_examples | example shift 10 Q | PASS | {"cell": "Production Log!Q10", "expected": 0.7864583333333334, "actual": 0.7864583333333334} |
| oee_examples | machine Press 01 B | PASS | {"cell": "Dashboard!B9", "expected": 880, "actual": 880.0} |
| oee_examples | machine Press 01 C | PASS | {"cell": "Dashboard!C9", "expected": 755, "actual": 755.0} |
| oee_examples | machine Press 01 D | PASS | {"cell": "Dashboard!D9", "expected": 125, "actual": 125.0} |
| oee_examples | machine Press 01 E | PASS | {"cell": "Dashboard!E9", "expected": 3400, "actual": 3400.0} |
| oee_examples | machine Press 01 F | PASS | {"cell": "Dashboard!F9", "expected": 3348, "actual": 3348.0} |
| oee_examples | machine Press 01 G | PASS | {"cell": "Dashboard!G9", "expected": 680.0, "actual": 680.0} |
| oee_examples | machine Press 01 H | PASS | {"cell": "Dashboard!H9", "expected": 0.8579545454545454, "actual": 0.8579545454545454} |
| oee_examples | machine Press 01 I | PASS | {"cell": "Dashboard!I9", "expected": 0.9006622516556292, "actual": 0.9006622516556292} |
| oee_examples | machine Press 01 J | PASS | {"cell": "Dashboard!J9", "expected": 0.9847058823529412, "actual": 0.9847058823529412} |
| oee_examples | machine Press 01 K | PASS | {"cell": "Dashboard!K9", "expected": 0.7609090909090909, "actual": 0.760909090909091} |
| oee_examples | machine CNC Lathe 02 B | PASS | {"cell": "Dashboard!B10", "expected": 880, "actual": 880.0} |
| oee_examples | machine CNC Lathe 02 C | PASS | {"cell": "Dashboard!C10", "expected": 800, "actual": 800.0} |
| oee_examples | machine CNC Lathe 02 D | PASS | {"cell": "Dashboard!D10", "expected": 80, "actual": 80.0} |
| oee_examples | machine CNC Lathe 02 E | PASS | {"cell": "Dashboard!E10", "expected": 450, "actual": 450.0} |
| oee_examples | machine CNC Lathe 02 F | PASS | {"cell": "Dashboard!F10", "expected": 444, "actual": 444.0} |
| oee_examples | machine CNC Lathe 02 G | PASS | {"cell": "Dashboard!G10", "expected": 712.5, "actual": 712.5} |
| oee_examples | machine CNC Lathe 02 H | PASS | {"cell": "Dashboard!H10", "expected": 0.9090909090909091, "actual": 0.9090909090909091} |
| oee_examples | machine CNC Lathe 02 I | PASS | {"cell": "Dashboard!I10", "expected": 0.890625, "actual": 0.890625} |
| oee_examples | machine CNC Lathe 02 J | PASS | {"cell": "Dashboard!J10", "expected": 0.9866666666666667, "actual": 0.9866666666666667} |
| oee_examples | machine CNC Lathe 02 K | PASS | {"cell": "Dashboard!K10", "expected": 0.7988636363636363, "actual": 0.7988636363636363} |
| oee_examples | machine Packaging Line A B | PASS | {"cell": "Dashboard!B11", "expected": 880, "actual": 880.0} |
| oee_examples | machine Packaging Line A C | PASS | {"cell": "Dashboard!C11", "expected": 800, "actual": 800.0} |
| oee_examples | machine Packaging Line A D | PASS | {"cell": "Dashboard!D11", "expected": 80, "actual": 80.0} |
| oee_examples | machine Packaging Line A E | PASS | {"cell": "Dashboard!E11", "expected": 17600, "actual": 17600.0} |
| oee_examples | machine Packaging Line A F | PASS | {"cell": "Dashboard!F11", "expected": 17355, "actual": 17355.0} |
| oee_examples | machine Packaging Line A G | PASS | {"cell": "Dashboard!G11", "expected": 733.3333333333333, "actual": 733.3333333333333} |
| oee_examples | machine Packaging Line A H | PASS | {"cell": "Dashboard!H11", "expected": 0.9090909090909091, "actual": 0.9090909090909091} |
| oee_examples | machine Packaging Line A I | PASS | {"cell": "Dashboard!I11", "expected": 0.9166666666666665, "actual": 0.9166666666666665} |
| oee_examples | machine Packaging Line A J | PASS | {"cell": "Dashboard!J11", "expected": 0.9860795454545456, "actual": 0.9860795454545456} |
| oee_examples | machine Packaging Line A K | PASS | {"cell": "Dashboard!K11", "expected": 0.8217329545454545, "actual": 0.8217329545454546} |
| oee_examples | all machines summed-factor B | PASS | {"cell": "Dashboard!B29", "expected": 2640, "actual": 2640.0} |
| oee_examples | all machines summed-factor C | PASS | {"cell": "Dashboard!C29", "expected": 2355, "actual": 2355.0} |
| oee_examples | all machines summed-factor D | PASS | {"cell": "Dashboard!D29", "expected": 285, "actual": 285.0} |
| oee_examples | all machines summed-factor E | PASS | {"cell": "Dashboard!E29", "expected": 21450, "actual": 21450.0} |
| oee_examples | all machines summed-factor F | PASS | {"cell": "Dashboard!F29", "expected": 21147, "actual": 21147.0} |
| oee_examples | all machines summed-factor G | PASS | {"cell": "Dashboard!G29", "expected": 2125.8333333333335, "actual": 2125.833333333333} |
| oee_examples | all machines summed-factor H | PASS | {"cell": "Dashboard!H29", "expected": 0.8920454545454546, "actual": 0.8920454545454546} |
| oee_examples | all machines summed-factor I | PASS | {"cell": "Dashboard!I29", "expected": 0.902689313517339, "actual": 0.9026893135173388} |
| oee_examples | all machines summed-factor J | PASS | {"cell": "Dashboard!J29", "expected": 0.9858369266954135, "actual": 0.9858369266954137} |
| oee_examples | all machines summed-factor K | PASS | {"cell": "Dashboard!K29", "expected": 0.7938352272727273, "actual": 0.7938352272727273} |
| oee_examples | heterogeneous machines OEE = sum ideal good time / sum planned time | PASS | {"cell": "Dashboard!K29", "expected": 0.7938352272727273, "actual": 0.7938352272727273} |
| oee_examples | equal planned example shifts agree with their average (weighting tested separately) | PASS | Examples have equal planned times; unequal-shift scenario establishes weighting, not this equality. |
| oee_heterogeneous | different cycle/reject mix yields 60/120 = 50%, not 60/660 = 9.09% | PASS | {"cell": "Dashboard!K29", "expected": 0.5, "actual": 0.5} |
| oee_date_blank | date filter blank inclusive planned time | PASS | {"cell": "Dashboard!B29", "expected": 2640, "actual": 2640.0} |
| oee_date_from | date filter from inclusive planned time | PASS | {"cell": "Dashboard!B29", "expected": 1320, "actual": 1320.0} |
| oee_date_to | date filter to inclusive planned time | PASS | {"cell": "Dashboard!B29", "expected": 1320, "actual": 1320.0} |
| oee_date_both | date filter both inclusive planned time | PASS | {"cell": "Dashboard!B29", "expected": 2640, "actual": 2640.0} |
| oee_date_boundary | date filter boundary inclusive planned time | PASS | {"cell": "Dashboard!B29", "expected": 1320, "actual": 1320.0} |
| oee_date_outside | date filter outside inclusive planned time | PASS | {"cell": "Dashboard!B29", "expected": 0, "actual": 0.0} |
| oee_bad_rejects | Check catches rejects | PASS | {"cell": "Production Log!R5", "actual": "Rejects > total parts", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_rejects | invalid rejects suppresses OEE | PASS | {"cell": "Production Log!Q5", "expected": "", "actual": ""} |
| oee_bad_downtime | Check catches downtime | PASS | {"cell": "Production Log!R5", "actual": "Downtime > planned time", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_downtime | invalid downtime suppresses OEE | PASS | {"cell": "Production Log!Q5", "expected": "", "actual": ""} |
| oee_bad_planned_stops | Check catches planned_stops | PASS | {"cell": "Production Log!R5", "actual": "Planned stops >= shift length", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_planned_stops | invalid planned_stops suppresses OEE | PASS | {"cell": "Production Log!Q5", "expected": "", "actual": ""} |
| oee_bad_zero_parts | zero output is valid with zero OEE | PASS | {"cell": "Production Log!R5", "expected": "OK", "actual": "OK"} |
| oee_bad_zero_parts | zero output OEE | PASS | {"cell": "Production Log!Q5", "expected": 0, "actual": 0.0} |
| oee_bad_zero_shift | Check catches zero_shift | PASS | {"cell": "Production Log!R5", "actual": "Values must be 0 or more (shift length above 0)", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_zero_shift | invalid zero_shift suppresses OEE | PASS | {"cell": "Production Log!Q5", "expected": "", "actual": ""} |
| oee_bad_unknown_machine | Check catches unknown_machine | PASS | {"cell": "Production Log!R5", "actual": "Machine not in Setup", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_unknown_machine | invalid unknown_machine suppresses OEE | PASS | {"cell": "Production Log!Q5", "expected": "", "actual": ""} |
| oee_bad_missing_cycle | Check catches missing_cycle | PASS | {"cell": "Production Log!R5", "actual": "Set an ideal cycle time in Setup", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_missing_cycle | invalid missing_cycle suppresses OEE | PASS | {"cell": "Production Log!Q5", "expected": "", "actual": ""} |
| oee_bad_performance_102 | Check catches performance_102 | PASS | {"cell": "Production Log!R5", "actual": "Check: performance above 100%", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_performance_102 | performance warning retains explicitly flagged OEE | PASS | {"cell": "Production Log!Q5", "expected": 0.9386363636363636, "actual": 0.9386363636363636} |
| oee_bad_performance_110 | Check catches performance_110 | PASS | {"cell": "Production Log!R5", "actual": "Check: performance above 100%", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_performance_110 | performance warning retains explicitly flagged OEE | PASS | {"cell": "Production Log!Q5", "expected": 1.0227272727272727, "actual": 1.0227272727272727} |
| oee_bad_negative_parts | Check catches negative_parts | PASS | {"cell": "Production Log!R5", "actual": "Values must be 0 or more (shift length above 0)", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_negative_parts | invalid negative_parts suppresses OEE | PASS | {"cell": "Production Log!Q5", "expected": "", "actual": ""} |
| oee_bad_text_parts | Check catches text_parts | PASS | {"cell": "Production Log!R5", "actual": "Enter numbers: shift length and total parts are required", "expected": "explicit invalid/missing-input warning"} |
| oee_bad_text_parts | invalid text_parts suppresses OEE | PASS | {"cell": "Production Log!Q5", "expected": "", "actual": ""} |
| oee_unequal | unequal shifts time-weighted 270/300, not average 75% | PASS | {"cell": "Dashboard!K9", "expected": 0.9, "actual": 0.9} |
| oee_target_0.95 | vs target follows 95% | PASS | {"K9": 0.760909090909091, "L9": -0.1890909090909091, "target": 0.95} |
| oee_target_0.5 | vs target follows 50% | PASS | {"K9": 0.760909090909091, "L9": 0.260909090909091, "target": 0.5} |
| oee_capacity | 500 rows 20 machines B | PASS | {"cell": "Dashboard!B29", "expected": 225000, "actual": 225000.0} |
| oee_capacity | 500 rows 20 machines C | PASS | {"cell": "Dashboard!C29", "expected": 214100, "actual": 214100.0} |
| oee_capacity | 500 rows 20 machines D | PASS | {"cell": "Dashboard!D29", "expected": 10900, "actual": 10900.0} |
| oee_capacity | 500 rows 20 machines E | PASS | {"cell": "Dashboard!E29", "expected": 324750, "actual": 324750.0} |
| oee_capacity | 500 rows 20 machines F | PASS | {"cell": "Dashboard!F29", "expected": 322500, "actual": 322500.0} |
| oee_capacity | 500 rows 20 machines G | PASS | {"cell": "Dashboard!G29", "expected": 162375.0, "actual": 162375.0} |
| oee_capacity | 500 rows 20 machines H | PASS | {"cell": "Dashboard!H29", "expected": 0.9515555555555556, "actual": 0.9515555555555556} |
| oee_capacity | 500 rows 20 machines I | PASS | {"cell": "Dashboard!I29", "expected": 0.7584072863148061, "actual": 0.7584072863148061} |
| oee_capacity | 500 rows 20 machines J | PASS | {"cell": "Dashboard!J29", "expected": 0.9930715935334873, "actual": 0.9930715935334873} |
| oee_capacity | 500 rows 20 machines K | PASS | {"cell": "Dashboard!K29", "expected": 0.7166666666666667, "actual": 0.7166666666666667} |
| oee_capacity | last OEE row counted | PASS | {"cell": "Production Log!R504", "expected": "OK", "actual": "OK"} |
| down_examples | example duration 5 | PASS | {"cell": "Downtime Log!G5", "expected": 35, "actual": 35.0} |
| down_examples | example duration 6 | PASS | {"cell": "Downtime Log!G6", "expected": 15, "actual": 15.0} |
| down_examples | example duration 7 | PASS | {"cell": "Downtime Log!G7", "expected": 60, "actual": 60.0} |
| down_examples | example duration 8 | PASS | {"cell": "Downtime Log!G8", "expected": 45, "actual": 45.0} |
| down_examples | example duration 9 | PASS | {"cell": "Downtime Log!G9", "expected": 55, "actual": 55.0} |
| down_examples | example duration 10 | PASS | {"cell": "Downtime Log!G10", "expected": 30, "actual": 30.0} |
| down_examples | example duration 11 | PASS | {"cell": "Downtime Log!G11", "expected": 15, "actual": 15.0} |
| down_examples | blank machine filter includes all 255 minutes | PASS | {"cell": "Pareto!B6", "expected": 255, "actual": 255.0} |
| down_examples | By Machine example 5 | PASS | {"cell": "By Machine!B5", "expected": 105, "actual": 105.0} |
| down_examples | By Machine example 6 | PASS | {"cell": "By Machine!B6", "expected": 75, "actual": 75.0} |
| down_examples | By Machine example 7 | PASS | {"cell": "By Machine!B7", "expected": 75, "actual": 75.0} |
| down_examples | By Machine reconciles to Pareto unfiltered | PASS | {"By Machine": 255.0, "Pareto": 255.0} |
| down_durations | duration normal | PASS | {"cell": "Downtime Log!G5", "expected": 35, "actual": 35.0} |
| down_durations | duration overnight | PASS | {"cell": "Downtime Log!G6", "expected": 45, "actual": 45.0} |
| down_durations | duration equal | PASS | {"cell": "Downtime Log!G7", "expected": 0, "actual": 0.0} |
| down_durations | duration midnight_end | PASS | {"cell": "Downtime Log!G8", "expected": 20, "actual": 20.0} |
| down_durations | duration midnight_start | PASS | {"cell": "Downtime Log!G9", "expected": 25, "actual": 25.0} |
| down_durations | duration override | PASS | {"cell": "Downtime Log!G10", "expected": 7, "actual": 7.0} |
| down_durations | duration zero_override | PASS | {"cell": "Downtime Log!G11", "expected": 0, "actual": 0.0} |
| down_durations | duration missing_start | PASS | {"cell": "Downtime Log!G12", "expected": "", "actual": ""} |
| down_durations | duration missing_end | PASS | {"cell": "Downtime Log!G13", "expected": "", "actual": ""} |
| down_durations | duration missing_both | PASS | {"cell": "Downtime Log!G14", "expected": "", "actual": ""} |
| down_durations | stop counts use same definition on Pareto and By Machine | PASS | {"Pareto": 5.0, "By Machine": 5.0} |
| down_literal_machine_0 | literal machine Line*1 minutes | PASS | {"cell": "By Machine!B5", "expected": 10, "actual": 10.0} |
| down_literal_machine_0 | literal machine filter Line*1 | PASS | {"cell": "Pareto!B6", "expected": 10, "actual": 10.0} |
| down_literal_machine_0 | literal reason category lookup Line*1 | PASS | {"cell": "Downtime Log!I5", "expected": "Cat", "actual": "Cat"} |
| down_literal_machine_1 | literal machine Line?1 minutes | PASS | {"cell": "By Machine!B5", "expected": 10, "actual": 10.0} |
| down_literal_machine_1 | literal machine filter Line?1 | PASS | {"cell": "Pareto!B6", "expected": 10, "actual": 10.0} |
| down_literal_machine_1 | literal reason category lookup Line?1 | PASS | {"cell": "Downtime Log!I5", "expected": "Cat", "actual": "Cat"} |
| down_literal_machine_2 | literal machine Line~1 minutes | PASS | {"cell": "By Machine!B5", "expected": 10, "actual": 10.0} |
| down_literal_machine_2 | literal machine filter Line~1 | PASS | {"cell": "Pareto!B6", "expected": 10, "actual": 10.0} |
| down_literal_machine_2 | literal reason category lookup Line~1 | PASS | {"cell": "Downtime Log!I5", "expected": "Cat", "actual": "Cat"} |
| down_literal_reason_0 | literal reason Jam*1 minutes | PASS | {"cell": "Pareto!J9", "expected": 10, "actual": 10.0} |
| down_literal_reason_0 | literal reason total no duplication Jam*1 | PASS | {"cell": "Pareto!B6", "expected": 100, "actual": 100.0} |
| down_literal_reason_0 | literal reason category lookup Jam*1 | PASS | {"cell": "Downtime Log!I5", "expected": "Cat", "actual": "Cat"} |
| down_literal_reason_1 | literal reason Jam?1 minutes | PASS | {"cell": "Pareto!J9", "expected": 10, "actual": 10.0} |
| down_literal_reason_1 | literal reason total no duplication Jam?1 | PASS | {"cell": "Pareto!B6", "expected": 100, "actual": 100.0} |
| down_literal_reason_1 | literal reason category lookup Jam?1 | PASS | {"cell": "Downtime Log!I5", "expected": "Cat", "actual": "Cat"} |
| down_literal_reason_2 | literal reason Jam~1 minutes | PASS | {"cell": "Pareto!J9", "expected": 10, "actual": 10.0} |
| down_literal_reason_2 | literal reason total no duplication Jam~1 | PASS | {"cell": "Pareto!B6", "expected": 100, "actual": 100.0} |
| down_literal_reason_2 | literal reason category lookup Jam~1 | PASS | {"cell": "Downtime Log!I5", "expected": "Cat", "actual": "Cat"} |
| down_literal_regex_reason_0 | literal regex_reason R.1 minutes | PASS | {"cell": "Pareto!J9", "expected": 10, "actual": 10.0} |
| down_literal_regex_reason_0 | literal reason total no duplication R.1 | PASS | {"cell": "Pareto!B6", "expected": 100, "actual": 100.0} |
| down_literal_regex_reason_0 | literal reason category lookup R.1 | PASS | {"cell": "Downtime Log!I5", "expected": "Cat", "actual": "Cat"} |
| down_literal_regex_reason_1 | literal regex_reason R(1) minutes | PASS | {"cell": "Pareto!J9", "expected": 10, "actual": 10.0} |
| down_literal_regex_reason_1 | literal reason total no duplication R(1) | PASS | {"cell": "Pareto!B6", "expected": 100, "actual": 100.0} |
| down_literal_regex_reason_1 | literal reason category lookup R(1) | PASS | {"cell": "Downtime Log!I5", "expected": "Cat", "actual": "Cat"} |
| down_literal_regex_reason_2 | literal regex_reason R+1 minutes | PASS | {"cell": "Pareto!J9", "expected": 10, "actual": 10.0} |
| down_literal_regex_reason_2 | literal reason total no duplication R+1 | PASS | {"cell": "Pareto!B6", "expected": 100, "actual": 100.0} |
| down_literal_regex_reason_2 | literal reason category lookup R+1 | PASS | {"cell": "Downtime Log!I5", "expected": "Cat", "actual": "Cat"} |
| down_ranking | all 30 reason minutes table total | PASS | {"cell": "Pareto!B6", "expected": 605, "actual": 605.0} |
| down_ranking | ties stable Setup order first | PASS | {"cell": "Pareto!B9", "expected": "R00", "actual": "R00"} |
| down_ranking | ties stable Setup order second | PASS | {"cell": "Pareto!B10", "expected": "R01", "actual": "R01"} |
| down_ranking | zero minute reason hidden | PASS | {"cell": "Pareto!B38", "expected": "", "actual": ""} |
| down_ranking | positive reason cumulative ends at 100% | PASS | {"cell": "Pareto!F37", "expected": 1, "actual": 1.0} |
| down_ranking | top 12 cumulative uses all reasons denominator | PASS | {"cell": "Pareto!F20", "expected": 0.71900826446281, "actual": 0.71900826446281} |
| down_ranking | ranked reason 00 minutes | PASS | {"cell": "Pareto!C9", "expected": 100, "actual": 100.0} |
| down_ranking | ranked reason 01 minutes | PASS | {"cell": "Pareto!C10", "expected": 100, "actual": 100.0} |
| down_ranking | ranked reason 02 minutes | PASS | {"cell": "Pareto!C11", "expected": 28, "actual": 28.0} |
| down_ranking | ranked reason 03 minutes | PASS | {"cell": "Pareto!C12", "expected": 27, "actual": 27.0} |
| down_ranking | ranked reason 04 minutes | PASS | {"cell": "Pareto!C13", "expected": 26, "actual": 26.0} |
| down_ranking | ranked reason 05 minutes | PASS | {"cell": "Pareto!C14", "expected": 25, "actual": 25.0} |
| down_ranking | ranked reason 06 minutes | PASS | {"cell": "Pareto!C15", "expected": 24, "actual": 24.0} |
| down_ranking | ranked reason 07 minutes | PASS | {"cell": "Pareto!C16", "expected": 23, "actual": 23.0} |
| down_ranking | ranked reason 08 minutes | PASS | {"cell": "Pareto!C17", "expected": 22, "actual": 22.0} |
| down_ranking | ranked reason 09 minutes | PASS | {"cell": "Pareto!C18", "expected": 21, "actual": 21.0} |
| down_ranking | ranked reason 10 minutes | PASS | {"cell": "Pareto!C19", "expected": 20, "actual": 20.0} |
| down_ranking | ranked reason 11 minutes | PASS | {"cell": "Pareto!C20", "expected": 19, "actual": 19.0} |
| down_ranking | ranked reason 12 minutes | PASS | {"cell": "Pareto!C21", "expected": 18, "actual": 18.0} |
| down_ranking | ranked reason 13 minutes | PASS | {"cell": "Pareto!C22", "expected": 17, "actual": 17.0} |
| down_ranking | ranked reason 14 minutes | PASS | {"cell": "Pareto!C23", "expected": 16, "actual": 16.0} |
| down_ranking | ranked reason 15 minutes | PASS | {"cell": "Pareto!C24", "expected": 15, "actual": 15.0} |
| down_ranking | ranked reason 16 minutes | PASS | {"cell": "Pareto!C25", "expected": 14, "actual": 14.0} |
| down_ranking | ranked reason 17 minutes | PASS | {"cell": "Pareto!C26", "expected": 13, "actual": 13.0} |
| down_ranking | ranked reason 18 minutes | PASS | {"cell": "Pareto!C27", "expected": 12, "actual": 12.0} |
| down_ranking | ranked reason 19 minutes | PASS | {"cell": "Pareto!C28", "expected": 11, "actual": 11.0} |
| down_ranking | ranked reason 20 minutes | PASS | {"cell": "Pareto!C29", "expected": 10, "actual": 10.0} |
| down_ranking | ranked reason 21 minutes | PASS | {"cell": "Pareto!C30", "expected": 9, "actual": 9.0} |
| down_ranking | ranked reason 22 minutes | PASS | {"cell": "Pareto!C31", "expected": 8, "actual": 8.0} |
| down_ranking | ranked reason 23 minutes | PASS | {"cell": "Pareto!C32", "expected": 7, "actual": 7.0} |
| down_ranking | ranked reason 24 minutes | PASS | {"cell": "Pareto!C33", "expected": 6, "actual": 6.0} |
| down_ranking | ranked reason 25 minutes | PASS | {"cell": "Pareto!C34", "expected": 5, "actual": 5.0} |
| down_ranking | ranked reason 26 minutes | PASS | {"cell": "Pareto!C35", "expected": 4, "actual": 4.0} |
| down_ranking | ranked reason 27 minutes | PASS | {"cell": "Pareto!C36", "expected": 3, "actual": 3.0} |
| down_ranking | ranked reason 28 minutes | PASS | {"cell": "Pareto!C37", "expected": 2, "actual": 2.0} |
| down_unknown | unknown reason warning shown | PASS | {"cell": "Downtime Log!I5", "expected": "Not in Setup", "actual": "Not in Setup"} |
| down_unknown | unknown reason not lost from total downtime | PASS | {"cell": "Pareto!B6", "expected": 100, "actual": 100.0} |
| down_unknown | By Machine includes unknown reason | PASS | {"cell": "By Machine!B5", "expected": 100, "actual": 100.0} |
| down_blank_machine | blank all-machine filter includes blank-machine downtime | PASS | {"cell": "Pareto!B6", "expected": 100, "actual": 100.0} |
| down_combined | date + machine intersection inclusive | PASS | {"cell": "Pareto!B6", "expected": 30, "actual": 30.0} |
| down_combined | By Machine ignores machine filter but follows dates | PASS | {"cell": "By Machine!B6", "expected": 170, "actual": 170.0} |
| down_capacity | 1000 rows 30 reasons total | PASS | {"cell": "Pareto!B6", "expected": 30100, "actual": 30100.0} |
| down_capacity | capacity cumulative 100% | PASS | {"cell": "Pareto!F38", "expected": 1, "actual": 1.0} |
| down_capacity | 1000th duration counted | PASS | {"cell": "Downtime Log!G1004", "expected": 40, "actual": 40.0} |
| down_capacity | capacity By Machine total reconciles | PASS | {"expected": 30100, "actual": 30100.0} |
| down_negative | negative duration rejected or warned | PASS | {"G5": "", "Pareto total": 10.0} |
| pm_examples | TODAY examples remain relative on actual office date | PASS | {"days left": [-10.0, 4.0, 3.0, 12.0, 160.0]} |
| pm_examples | example overdue count | PASS | {"cell": "PM Plan!L1", "expected": 1, "actual": 1.0} |
| pm_examples | example due-soon count | PASS | {"cell": "PM Plan!L2", "expected": 2, "actual": 2.0} |
| pm_examples | example OK count | PASS | {"cell": "PM Plan!L3", "expected": 2, "actual": 2.0} |
| pm_never | never completed days left zero | PASS | {"cell": "PM Plan!H5", "expected": 0, "actual": 0.0} |
| pm_never | never completed due today | PASS | {"cell": "PM Plan!G5", "expected": 46305, "actual": 46305.0} |
| pm_never | never completed status due soon | PASS | {"cell": "PM Plan!I5", "expected": "Due soon", "actual": "Due soon"} |
| pm_never | never status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_latest | latest of multiple unsorted completions | PASS | {"cell": "PM Plan!F5", "expected": 46274, "actual": 46274.0} |
| pm_latest | latest status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_earlier_later | pre-log later than logged date wins | PASS | {"cell": "PM Plan!F5", "expected": 46295, "actual": 46295.0} |
| pm_earlier_later | earlier_later status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_typo_asset | completion typo_asset warning | PASS | {"cell": "Completion Log!F5", "expected": "No matching asset + task in plan", "actual": "No matching asset + task in plan"} |
| pm_typo_asset | completion typo_asset leaves plan unchanged | PASS | {"cell": "PM Plan!F5", "expected": "", "actual": ""} |
| pm_typo_asset | typo_asset status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_typo_task | completion typo_task warning | PASS | {"cell": "Completion Log!F5", "expected": "No matching asset + task in plan", "actual": "No matching asset + task in plan"} |
| pm_typo_task | completion typo_task leaves plan unchanged | PASS | {"cell": "PM Plan!F5", "expected": "", "actual": ""} |
| pm_typo_task | typo_task status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_blank_frequency | invalid blank_frequency explicitly warned | PASS | {"cell": "PM Plan!I5", "actual": "Check frequency", "expected": "explicit invalid/missing-input warning"} |
| pm_blank_frequency | blank_frequency status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_zero_frequency | invalid zero_frequency explicitly warned | PASS | {"cell": "PM Plan!I5", "actual": "Check frequency", "expected": "explicit invalid/missing-input warning"} |
| pm_zero_frequency | zero_frequency status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_negative_frequency | invalid negative_frequency explicitly warned | PASS | {"cell": "PM Plan!I5", "actual": "Check frequency", "expected": "explicit invalid/missing-input warning"} |
| pm_negative_frequency | negative_frequency status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_window0 | window0 follows setting | PASS | {"cell": "PM Plan!I5", "expected": "OK", "actual": "OK"} |
| pm_window0 | window0 status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_window30 | window30 follows setting | PASS | {"cell": "PM Plan!I5", "expected": "Due soon", "actual": "Due soon"} |
| pm_window30 | window30 status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_duplicate | duplicate asset+task explicitly warned | PASS | {"statuses": ["Duplicate row", "Duplicate row"], "last completed": [46266.0, 46266.0], "next due": [46273.0, 46296.0]} |
| pm_duplicate | duplicate status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_wildcard | completion wildcard warning | PASS | {"cell": "Completion Log!F5", "expected": "No matching asset + task in plan", "actual": "No matching asset + task in plan"} |
| pm_wildcard | completion wildcard leaves plan unchanged | PASS | {"cell": "PM Plan!F5", "expected": "", "actual": ""} |
| pm_wildcard | wildcard status counts match all plan rows | PASS | counts independently counted from plan statuses |
| pm_blank_date | undated completion not reported OK | PASS | {"cell": "Completion Log!F5", "actual": "Enter the date done", "expected": "explicit invalid/missing-input warning"} |
| pm_blank_date | blank_date status counts match all plan rows | PASS | counts independently counted from plan statuses |
| original_oee | Setup native frozen position | FAIL | {"expected": [true, 0, 4], "actual": [true, 0, 5]} |
| original_oee | Production Log native frozen position | FAIL | {"expected": [true, 3, 4], "actual": [true, 3, 5]} |
| original_oee | Dashboard native frozen position | FAIL | {"expected": [true, 1, 8], "actual": [true, 1, 9]} |
| original_oee | Production Log!C5 native list validation | PASS | {"formula2": "0", "formula1": "$Setup.$A$5:$A$24", "validation_type": "LIST", "show_list": 1, "show_error": false, "conditional_rules": []} |
| original_oee | native conditional colour styles | PASS | [{"formula2": "0", "operator": "FORMULA", "style": "ConditionalStyle_1", "formula1": "AND(ISNUMBER(A1);A1<0.6)", "background": 16305069}, {"formula2": "0", "operator": "FORMULA", "style": "ConditionalStyle_2", "formula1": "AND(ISNUMBER(A1);A1>=$B$5)", "background": 13037518}, {"formula2": "0", "operator": "FORMULA", "style": "ConditionalStyle_3", "formula1": "AND(ISNUMBER(A1);A1>=0.6;A1<$B$5)", "background": 16770713}, {"formula2": "0", "operator": "FORMULA", "style": "ConditionalStyle_1", "form |
| original_oee | native OEE column chart type | PASS | [["com.sun.star.chart2.ColumnChartType", 0]] |
| original_down | Setup native frozen position | FAIL | {"expected": [true, 0, 4], "actual": [true, 0, 5]} |
| original_down | Downtime Log native frozen position | FAIL | {"expected": [true, 3, 4], "actual": [true, 3, 5]} |
| original_down | Pareto native frozen position | FAIL | {"expected": [true, 0, 8], "actual": [true, 0, 9]} |
| original_down | By Machine native frozen position | FAIL | {"expected": [true, 0, 4], "actual": [true, 0, 5]} |
| original_down | Downtime Log!C5 native list validation | PASS | {"formula2": "0", "formula1": "$Setup.$A$5:$A$34", "validation_type": "LIST", "show_list": 1, "show_error": false, "conditional_rules": []} |
| original_down | Downtime Log!H5 native list validation | PASS | {"formula2": "0", "formula1": "$Setup.$D$5:$D$34", "validation_type": "LIST", "show_list": 1, "show_error": false, "conditional_rules": []} |
| original_down | Pareto!B5 native list validation | PASS | {"formula2": "0", "formula1": "$Setup.$A$5:$A$34", "validation_type": "LIST", "show_list": 1, "show_error": false, "conditional_rules": []} |
| original_down | native Pareto column plus secondary-axis line | PASS | [["com.sun.star.chart2.ColumnChartType", 0], ["com.sun.star.chart2.LineChartType", 1]] |
| original_down | unaltered shipped blank-filter Pareto total | PASS | {"cell": "Pareto!B6", "expected": 255, "actual": 255.0} |
| original_pm | PM Plan native frozen position | FAIL | {"expected": [true, 2, 4], "actual": [true, 2, 5]} |
| original_pm | Completion Log native frozen position | FAIL | {"expected": [true, 0, 4], "actual": [true, 0, 5]} |
| original_pm | Completion Log!B5 native list validation | PASS | {"formula2": "0", "formula1": "$'PM Plan'.$A$5:$A$304", "validation_type": "LIST", "show_list": 1, "show_error": false, "conditional_rules": []} |
| original_pm | Completion Log!C5 native list validation | PASS | {"formula2": "0", "formula1": "$'PM Plan'.$B$5:$B$304", "validation_type": "LIST", "show_list": 1, "show_error": false, "conditional_rules": []} |
| original_pm | native conditional colour styles | PASS | [{"formula2": "0", "operator": "FORMULA", "style": "ConditionalStyle_1", "formula1": "A1=\"OVERDUE\"", "background": 16305069}, {"formula2": "0", "operator": "FORMULA", "style": "ConditionalStyle_2", "formula1": "A1=\"Due soon\"", "background": 16770713}, {"formula2": "0", "operator": "FORMULA", "style": "ConditionalStyle_3", "formula1": "A1=\"OK\"", "background": 13037518}, {"formula2": "0", "operator": "FORMULA", "style": "ConditionalStyle_4", "formula1": "OR(A1=\"Check frequency\";A1=\"Duplic |
| oee_examples | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_heterogeneous | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_date_blank | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_date_from | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_date_to | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_date_both | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_date_boundary | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_date_outside | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_rejects | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_downtime | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_planned_stops | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_zero_parts | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_zero_shift | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_unknown_machine | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_missing_cycle | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_performance_102 | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_performance_110 | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_negative_parts | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_bad_text_parts | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_unequal | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_target_0.95 | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_target_0.5 | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| oee_capacity | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| down_examples | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_durations | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_literal_machine_0 | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_literal_machine_1 | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_literal_machine_2 | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_literal_reason_0 | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_literal_reason_1 | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_literal_reason_2 | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_literal_regex_reason_0 | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_literal_regex_reason_1 | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_literal_regex_reason_2 | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_ranking | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_unknown | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_blank_machine | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_combined | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_capacity | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| down_negative | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| pm_examples | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_never | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_latest | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_earlier_later | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_typo_asset | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_typo_task | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_blank_frequency | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_zero_frequency | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_negative_frequency | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_window0 | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_window30 | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_duplicate | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_wildcard | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| pm_blank_date | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| original_oee | zero recalculated formula errors including empty rows | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| original_down | zero recalculated formula errors including empty rows | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| original_pm | zero recalculated formula errors including empty rows | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| safety | shipped files unchanged | PASS | source hashes preserved |

Full evidence (including long formulas/rule inventories) is in the corresponding JSON; table cells are bounded to500 characters.

### New native edges

| Scenario | Assertion | Result | Expected / actual evidence |
|---|---|---|---|
| edge_oee_missing_date | missing_date visibly warned | FAIL | {"cell": "Production Log!R5", "actual": "OK", "expected": "explicit invalid/missing-input warning"} |
| edge_oee_duplicate_machine | duplicate setup cannot silently double cycle and totals | FAIL | {"expected": "40% or explicit duplicate warning", "cycle": 120.0, "check": "OK", "all_oee": 0.8} |
| edge_oee_text_cycle | text_cycle visibly warned | PASS | {"cell": "Production Log!R5", "actual": "Set an ideal cycle time in Setup", "expected": "explicit invalid/missing-input warning"} |
| edge_oee_low_target | 40% OEE exceeds 30% target | PASS | {"cell": "Dashboard!K9", "expected": 0.4, "actual": 0.4} |
| edge_pm_text_date_matching | invalid completion visibly warned | PASS | {"cell": "Completion Log!F5", "actual": "Enter the date done", "expected": "explicit invalid/missing-input warning"} |
| edge_pm_text_date_matching | invalid completion leaves last-completed blank | PASS | {"cell": "PM Plan!F5", "expected": "", "actual": ""} |
| edge_pm_text_date_unrelated | invalid completion visibly warned | PASS | {"cell": "Completion Log!F5", "actual": "Enter the date done", "expected": "explicit invalid/missing-input warning"} |
| edge_pm_text_date_unrelated | invalid completion leaves last-completed blank | PASS | {"cell": "PM Plan!F5", "expected": "", "actual": ""} |
| edge_pm_missing_key | invalid completion visibly warned | FAIL | {"cell": "Completion Log!F5", "actual": "OK", "expected": "explicit invalid/missing-input warning"} |
| edge_pm_missing_key | invalid completion leaves last-completed blank | PASS | {"cell": "PM Plan!F5", "expected": "", "actual": ""} |
| edge_down_duplicate_reason | duplicate reason cannot silently create negative unclassified minutes | FAIL | {"total": 10.0, "unclassified": -10.0, "cumulative": 2.0} |
| edge_down_duplicate_machine | duplicate machine cannot silently create negative other minutes | FAIL | {"other": -10.0, "all": 10.0} |
| edge_oee_missing_date | zero formula errors | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| edge_oee_duplicate_machine | zero formula errors | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| edge_oee_text_cycle | zero formula errors | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| edge_oee_low_target | zero formula errors | PASS | {"Production Log": "", "Setup": "", "Dashboard": "", "How to use": ""} |
| edge_pm_text_date_matching | zero formula errors | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| edge_pm_text_date_unrelated | zero formula errors | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| edge_pm_missing_key | zero formula errors | PASS | {"PM Plan": "", "Completion Log": "", "How to use": ""} |
| edge_down_duplicate_reason | zero formula errors | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |
| edge_down_duplicate_machine | zero formula errors | PASS | {"Downtime Log": "", "Setup": "", "Pareto": "", "By Machine": "", "How to use": ""} |

Full evidence (including long formulas/rule inventories) is in the corresponding JSON; table cells are bounded to500 characters.

### Structural / documentation agreement

| Scenario | Assertion | Result | Expected / actual evidence |
|---|---|---|---|
| — | bundle title and tag limits | PASS | {"title_characters": 123, "tag_count": 13, "longest_tag": 16} |
| — | oee title and tag limits | PASS | {"title_characters": 112, "tag_count": 13, "longest_tag": 18} |
| — | downtime title and tag limits | PASS | {"title_characters": 108, "tag_count": 13, "longest_tag": 16} |
| — | pm title and tag limits | PASS | {"title_characters": 111, "tag_count": 13, "longest_tag": 17} |
| — | Downtime-Log-and-Pareto.xlsx no macros/external links/personal identifiers/paths | PASS | {"creator": "openpyxl (library)", "external_links": [], "suspicious_metadata": []} |
| — | OEE-Tracker.xlsx no macros/external links/personal identifiers/paths | PASS | {"creator": "openpyxl (library)", "external_links": [], "suspicious_metadata": []} |
| — | Preventive-Maintenance-Schedule.xlsx no macros/external links/personal identifiers/paths | PASS | {"creator": "openpyxl (library)", "external_links": [], "suspicious_metadata": []} |
| — | OEE Check flags every performance above 100% | PASS | =IF($C5="","",IF(NOT(SUMPRODUCT(--(Setup!$A$5:$A$24=$C5))>0),"Machine not in Setup",IF(OR(NOT(ISNUMBER(K5)),N(K5)<=0),"Set an ideal cycle time in Setup",IF(OR(NOT(ISNUMBER(D5)),NOT(ISNUMBER(G5)),AND(E5<>"",NOT(ISNUMBER(E5))),AND(F5<>"",NOT(ISNUMBER(F5))),AND(H5<>"",NOT(ISNUMBER(H5)))),"Enter numbers: shift length and total parts are required",IF(OR(N(D5)<=0,N(E5)<0,N(F5)<0,N(G5)<0,N(H5)<0),"Values must be 0 or more (shift length above 0)",IF(N(H5)>N(G5),"Rejects > total parts",IF(N(E5)>=N(D5),"P |
| — | OEE machine literal names safe under documented Excel wildcard semantics | PASS | {"formula": "=IF($A9=\"\",\"\",SUMPRODUCT(('Production Log'!$C$5:$C$504=$A9)*('Production Log'!$T$5:$T$504=TRUE())*('Production Log'!$A$5:$A$504>=$D$3)*('Production Log'!$A$5:$A$504<=$D$4),'Production Log'!$I$5:$I$504))", "acceptance": "Escaped criteria or exact array equality without wildcard-consuming criteria functions", "source": "https://support.microsoft.com/en-au/excel/functions/sumifs-function", "native_Excel_test": "unverified; exact equality removes the documented wildcard construct"} |
| — | OEE cycle lookup literal names safe under documented Excel wildcard semantics | PASS | {"formula": "=IF($C5=\"\",\"\",IF(SUMPRODUCT(--(Setup!$A$5:$A$24=$C5))>0,SUMPRODUCT((Setup!$A$5:$A$24=$C5)*1,Setup!$B$5:$B$24),\"\"))", "acceptance": "Escaped criteria or exact array equality without wildcard-consuming criteria functions", "source": "https://support.microsoft.com/en-us/excel/functions/match-function", "native_Excel_test": "unverified; exact equality removes the documented wildcard construct"} |
| — | downtime machine literal names safe under documented Excel wildcard semantics | PASS | {"formula": "=IF($A5=\"\",\"\",SUMPRODUCT(('Downtime Log'!$C$5:$C$1004=$A5)*('Downtime Log'!$A$5:$A$1004>=Pareto!$D$3)*('Downtime Log'!$A$5:$A$1004<=Pareto!$D$4),'Downtime Log'!$G$5:$G$1004))", "acceptance": "Escaped criteria or exact array equality without wildcard-consuming criteria functions", "source": "https://support.microsoft.com/en-au/excel/functions/sumifs-function", "native_Excel_test": "unverified; exact equality removes the documented wildcard construct"} |
| — | downtime reason literal names safe under documented Excel wildcard semantics | PASS | {"formula": "=IF(I9=\"\",0,SUMPRODUCT(('Downtime Log'!$H$5:$H$1004=I9)*('Downtime Log'!$A$5:$A$1004>=$D$3)*('Downtime Log'!$A$5:$A$1004<=$D$4)*((($B$5=\"\")+('Downtime Log'!$C$5:$C$1004=$B$5))>0),'Downtime Log'!$G$5:$G$1004))", "acceptance": "Escaped criteria or exact array equality without wildcard-consuming criteria functions", "source": "https://support.microsoft.com/en-au/excel/functions/sumifs-function", "native_Excel_test": "unverified; exact equality removes the documented wildcard constr |
| — | downtime stops literal names safe under documented Excel wildcard semantics | PASS | {"formula": "=IF(I9=\"\",0,SUMPRODUCT(('Downtime Log'!$H$5:$H$1004=I9)*('Downtime Log'!$A$5:$A$1004>=$D$3)*('Downtime Log'!$A$5:$A$1004<=$D$4)*((($B$5=\"\")+('Downtime Log'!$C$5:$C$1004=$B$5))>0)*ISNUMBER('Downtime Log'!$G$5:$G$1004)*('Downtime Log'!$G$5:$G$1004>0)))", "acceptance": "Escaped criteria or exact array equality without wildcard-consuming criteria functions", "source": "https://support.microsoft.com/en-au/excel/functions/sumifs-function", "native_Excel_test": "unverified; exact equal |
| — | downtime category lookup literal names safe under documented Excel wildcard semantics | PASS | {"formula": "=IF(H5=\"\",\"\",IF(SUMPRODUCT(MAX((Setup!$D$5:$D$34=H5)*(ROW(Setup!$D$5:$D$34)-4)))=0,\"Not in Setup\",INDEX(Setup!$E$5:$E$34,SUMPRODUCT(MAX((Setup!$D$5:$D$34=H5)*(ROW(Setup!$D$5:$D$34)-4))))))", "acceptance": "Escaped criteria or exact array equality without wildcard-consuming criteria functions", "source": "https://support.microsoft.com/en-us/excel/functions/match-function", "native_Excel_test": "unverified; exact equality removes the documented wildcard construct"} |
| — | PM completion matching literal names safe under documented Excel wildcard semantics | PASS | {"formula": "=IF(AND(A5=\"\",B5=\"\",C5=\"\"),\"\",IF(NOT(ISNUMBER(A5)),\"Enter the date done\",IF(SUMPRODUCT(('PM Plan'!$A$5:$A$304=B5)*('PM Plan'!$B$5:$B$304=C5))=0,\"No matching asset + task in plan\",\"OK\")))", "acceptance": "Escaped criteria or exact array equality without wildcard-consuming criteria functions", "source": "https://support.microsoft.com/en-au/excel/functions/sumifs-function", "native_Excel_test": "unverified; exact equality removes the documented wildcard construct"} |
| — | Declared direct-upload format agrees with Etsy's published file-type list | FAIL | {"instructions": "- Bundle: the three `.xlsx` files plus `guides/Manufacturing-Bundle-Guide.pdf` (Etsy allows 5 files).\n- Each single listing: its `.xlsx` plus its own guide PDF.", "supported_wrapper": ".zip", "contrary_repository_record": "PR #14 / main 1c9ebda records direct XLSX attachments after reload", "live_upload_and_buyer_download": "unverified; this check is documentation-list agreement, not proof of rejection", "source": "https://help.etsy.com/hc/en-us/articles/115015628347-How-to-Ma |

Full evidence (including long formulas/rule inventories) is in the corresponding JSON; table cells are bounded to500 characters.

### Guide integrity/rendering

| Scenario | Assertion | Result | Expected / actual evidence |
|---|---|---|---|
| — | Downtime-Log-and-Pareto-Guide.pdf checkout cross-reference offset | PASS | {"offset": 549924, "bytes_at_offset": "b'xref\\n0 21\\n0000000000'", "actual_xref_offset": 549924} |
| — | Downtime-Log-and-Pareto-Guide.pdf checkout strict PDF parse | PASS | {"pages": 4} |
| — | Downtime-Log-and-Pareto-Guide.pdf committed blob cross-reference offset | PASS | {"offset": 549924, "bytes_at_offset": "b'xref\\n0 21\\n0000000000'", "actual_xref_offset": 549924} |
| — | Downtime-Log-and-Pareto-Guide.pdf committed blob strict PDF parse | PASS | {"pages": 4} |
| — | Downtime-Log-and-Pareto-Guide.pdf no owner identifiers or local paths | PASS | {"suspicious": [], "author": "TaktTools"} |
| — | Downtime-Log-and-Pareto-Guide.pdf explicitly clears yellow example cells only | PASS | Guide instructs clearing yellow cells and retaining formula rows |
| — | Downtime-Log-and-Pareto-Guide.pdf recovery rendering of every page | PASS | {"returncode": 0, "pages_rendered": 4, "stderr_first_1000_chars": "Syntax Error: No display font for 'Symbol'\nSyntax Error: No display font for 'ArialUnicode'\n", "stderr_line_count": 2} |
| — | Manufacturing-Bundle-Guide.pdf checkout cross-reference offset | PASS | {"offset": 1062665, "bytes_at_offset": "b'xref\\n0 39\\n0000000000'", "actual_xref_offset": 1062665} |
| — | Manufacturing-Bundle-Guide.pdf checkout strict PDF parse | PASS | {"pages": 11} |
| — | Manufacturing-Bundle-Guide.pdf committed blob cross-reference offset | PASS | {"offset": 1062665, "bytes_at_offset": "b'xref\\n0 39\\n0000000000'", "actual_xref_offset": 1062665} |
| — | Manufacturing-Bundle-Guide.pdf committed blob strict PDF parse | PASS | {"pages": 11} |
| — | Manufacturing-Bundle-Guide.pdf no owner identifiers or local paths | PASS | {"suspicious": [], "author": "TaktTools"} |
| — | Manufacturing-Bundle-Guide.pdf explicitly clears yellow example cells only | PASS | Guide instructs clearing yellow cells and retaining formula rows |
| — | Manufacturing-Bundle-Guide.pdf recovery rendering of every page | PASS | {"returncode": 0, "pages_rendered": 11, "stderr_first_1000_chars": "Syntax Error: No display font for 'Symbol'\nSyntax Error: No display font for 'ArialUnicode'\n", "stderr_line_count": 2} |
| — | OEE-Tracker-Guide.pdf checkout cross-reference offset | PASS | {"offset": 331252, "bytes_at_offset": "b'xref\\n0 19\\n0000000000'", "actual_xref_offset": 331252} |
| — | OEE-Tracker-Guide.pdf checkout strict PDF parse | PASS | {"pages": 4} |
| — | OEE-Tracker-Guide.pdf committed blob cross-reference offset | PASS | {"offset": 331252, "bytes_at_offset": "b'xref\\n0 19\\n0000000000'", "actual_xref_offset": 331252} |
| — | OEE-Tracker-Guide.pdf committed blob strict PDF parse | PASS | {"pages": 4} |
| — | OEE-Tracker-Guide.pdf no owner identifiers or local paths | PASS | {"suspicious": [], "author": "TaktTools"} |
| — | OEE-Tracker-Guide.pdf explicitly clears yellow example cells only | PASS | Guide instructs clearing yellow cells and retaining formula rows |
| — | OEE-Tracker-Guide.pdf recovery rendering of every page | PASS | {"returncode": 0, "pages_rendered": 4, "stderr_first_1000_chars": "Syntax Error: No display font for 'Symbol'\nSyntax Error: No display font for 'ArialUnicode'\n", "stderr_line_count": 2} |
| — | Preventive-Maintenance-Schedule-Guide.pdf checkout cross-reference offset | PASS | {"offset": 229147, "bytes_at_offset": "b'xref\\n0 17\\n0000000000'", "actual_xref_offset": 229147} |
| — | Preventive-Maintenance-Schedule-Guide.pdf checkout strict PDF parse | PASS | {"pages": 3} |
| — | Preventive-Maintenance-Schedule-Guide.pdf committed blob cross-reference offset | PASS | {"offset": 229147, "bytes_at_offset": "b'xref\\n0 17\\n0000000000'", "actual_xref_offset": 229147} |
| — | Preventive-Maintenance-Schedule-Guide.pdf committed blob strict PDF parse | PASS | {"pages": 3} |
| — | Preventive-Maintenance-Schedule-Guide.pdf no owner identifiers or local paths | PASS | {"suspicious": [], "author": "TaktTools"} |
| — | Preventive-Maintenance-Schedule-Guide.pdf explicitly clears yellow example cells only | PASS | Guide instructs clearing yellow cells and retaining formula rows |
| — | Preventive-Maintenance-Schedule-Guide.pdf recovery rendering of every page | PASS | {"returncode": 0, "pages_rendered": 3, "stderr_first_1000_chars": "Syntax Error: No display font for 'Symbol'\nSyntax Error: No display font for 'ArialUnicode'\n", "stderr_line_count": 2} |

Full evidence (including long formulas/rule inventories) is in the corresponding JSON; table cells are bounded to500 characters.

### Shared native cell expectations

| Scenario | Cell | Expected | Native actual | Result |
|---|---|---|---|---|
| oee_examples | Production Log!R5 | OK | OK | PASS |
| oee_examples | Production Log!Q5 | 0.8536363636363636 | 0.8536363636363636 | PASS |
| oee_examples | Production Log!R6 | OK | OK | PASS |
| oee_examples | Production Log!Q6 | 0.7412878787878788 | 0.7412878787878788 | PASS |
| oee_examples | Production Log!R7 | OK | OK | PASS |
| oee_examples | Production Log!Q7 | 0.8570075757575757 | 0.8570075757575757 | PASS |
| oee_examples | Production Log!R8 | OK | OK | PASS |
| oee_examples | Production Log!Q8 | 0.6681818181818182 | 0.6681818181818182 | PASS |
| oee_examples | Production Log!R9 | OK | OK | PASS |
| oee_examples | Production Log!Q9 | 0.856439393939394 | 0.856439393939394 | PASS |
| oee_examples | Production Log!R10 | OK | OK | PASS |
| oee_examples | Production Log!Q10 | 0.7864583333333334 | 0.7864583333333334 | PASS |
| oee_examples | Dashboard!K9 | 0.760909090909091 | 0.760909090909091 | PASS |
| oee_examples | Dashboard!K10 | 0.7988636363636363 | 0.7988636363636363 | PASS |
| oee_examples | Dashboard!K11 | 0.8217329545454546 | 0.8217329545454546 | PASS |
| oee_examples | Dashboard!K29 | 0.7938352272727273 | 0.7938352272727273 | PASS |
| oee_mixed_cycle_times | Production Log!R5 | OK | OK | PASS |
| oee_mixed_cycle_times | Production Log!Q5 | 1.0 | 1.0 | PASS |
| oee_mixed_cycle_times | Production Log!R6 | OK | OK | PASS |
| oee_mixed_cycle_times | Production Log!Q6 | 0.0 | 0.0 | PASS |
| oee_mixed_cycle_times | Dashboard!K9 | 1.0 | 1.0 | PASS |
| oee_mixed_cycle_times | Dashboard!K10 | 0.0 | 0.0 | PASS |
| oee_mixed_cycle_times | Dashboard!K29 | 0.5 | 0.5 | PASS |
| oee_bad_inputs | Production Log!R5 | OK | OK | PASS |
| oee_bad_inputs | Production Log!Q5 | 0.8536363636363636 | 0.8536363636363636 | PASS |
| oee_bad_inputs | Production Log!R6 | Rejects > total parts | Rejects > total parts | PASS |
| oee_bad_inputs | Production Log!Q6 |  |  | PASS |
| oee_bad_inputs | Production Log!R7 | Enter numbers: shift length and total parts are required | Enter numbers: shift length and total parts are required | PASS |
| oee_bad_inputs | Production Log!Q7 |  |  | PASS |
| oee_bad_inputs | Production Log!R8 | Values must be 0 or more (shift length above 0) | Values must be 0 or more (shift length above 0) | PASS |
| oee_bad_inputs | Production Log!Q8 |  |  | PASS |
| oee_bad_inputs | Production Log!R9 | Downtime > planned time | Downtime > planned time | PASS |
| oee_bad_inputs | Production Log!Q9 |  |  | PASS |
| oee_bad_inputs | Production Log!R10 | Machine not in Setup | Machine not in Setup | PASS |
| oee_bad_inputs | Production Log!Q10 |  |  | PASS |
| oee_bad_inputs | Production Log!R11 | Values must be 0 or more (shift length above 0) | Values must be 0 or more (shift length above 0) | PASS |
| oee_bad_inputs | Production Log!Q11 |  |  | PASS |
| oee_bad_inputs | Production Log!R12 | Check: performance above 100% | Check: performance above 100% | PASS |
| oee_bad_inputs | Production Log!Q12 | 0.9386363636363636 | 0.9386363636363636 | PASS |
| oee_bad_inputs | Dashboard!K9 | 0.8961363636363636 | 0.8961363636363636 | PASS |
| oee_bad_inputs | Dashboard!K29 | 0.8961363636363636 | 0.8961363636363636 | PASS |
| oee_wildcard_names | Production Log!R5 | OK | OK | PASS |
| oee_wildcard_names | Production Log!Q5 | 0.5 | 0.5 | PASS |
| oee_wildcard_names | Production Log!R6 | OK | OK | PASS |
| oee_wildcard_names | Production Log!Q6 | 1.0 | 1.0 | PASS |
| oee_wildcard_names | Production Log!R7 | OK | OK | PASS |
| oee_wildcard_names | Production Log!Q7 | 0.16666666666666669 | 0.16666666666666669 | PASS |
| oee_wildcard_names | Dashboard!K9 | 0.5 | 0.5 | PASS |
| oee_wildcard_names | Dashboard!K10 | 1.0 | 1.0 | PASS |
| oee_wildcard_names | Dashboard!K11 | 0.16666666666666669 | 0.16666666666666669 | PASS |
| oee_wildcard_names | Dashboard!K29 | 0.5555555555555555 | 0.5555555555555556 | PASS |
| oee_date_filter | Production Log!R5 | OK | OK | PASS |
| oee_date_filter | Production Log!Q5 | 0.8536363636363636 | 0.8536363636363636 | PASS |
| oee_date_filter | Production Log!R6 | OK | OK | PASS |
| oee_date_filter | Production Log!Q6 | 0.6681818181818182 | 0.6681818181818182 | PASS |
| oee_date_filter | Production Log!R7 | OK | OK | PASS |
| oee_date_filter | Production Log!Q7 | 0.9090909090909091 | 0.9090909090909091 | PASS |
| oee_date_filter | Dashboard!K9 | 0.6681818181818182 | 0.6681818181818182 | PASS |
| oee_date_filter | Dashboard!K29 | 0.6681818181818182 | 0.6681818181818182 | PASS |
| down_examples | Pareto!B6 | 240 | 240.0 | PASS |
| down_examples | Pareto!B7 | 0 | 0.0 | PASS |
| down_examples | Pareto!J9 | 160 | 160.0 | PASS |
| down_examples | Pareto!K9 | 3 | 3.0 | PASS |
| down_examples | Pareto!J10 | 65 | 65.0 | PASS |
| down_examples | Pareto!K10 | 2 | 2.0 | PASS |
| down_examples | Pareto!J11 | 15 | 15.0 | PASS |
| down_examples | Pareto!K11 | 1 | 1.0 | PASS |
| down_examples | By Machine!B5 | 105 | 105.0 | PASS |
| down_examples | By Machine!C5 | 3 | 3.0 | PASS |
| down_examples | By Machine!B6 | 60 | 60.0 | PASS |
| down_examples | By Machine!C6 | 1 | 1.0 | PASS |
| down_examples | By Machine!B7 | 75 | 75.0 | PASS |
| down_examples | By Machine!C7 | 2 | 2.0 | PASS |
| down_examples | By Machine!B36 | 240 | 240.0 | PASS |
| down_examples | By Machine!C36 | 6 | 6.0 | PASS |
| down_machine_filter | Pareto!B6 | 25 | 25.0 | PASS |
| down_machine_filter | Pareto!B7 | 0 | 0.0 | PASS |
| down_machine_filter | Pareto!J9 | 20 | 20.0 | PASS |
| down_machine_filter | Pareto!K9 | 1 | 1.0 | PASS |
| down_machine_filter | Pareto!J10 | 5 | 5.0 | PASS |
| down_machine_filter | Pareto!K10 | 1 | 1.0 | PASS |
| down_machine_filter | Pareto!J11 | 0 | 0.0 | PASS |
| down_machine_filter | Pareto!K11 | 0 | 0.0 | PASS |
| down_machine_filter | By Machine!B5 | 30 | 30.0 | PASS |
| down_machine_filter | By Machine!C5 | 1 | 1.0 | PASS |
| down_machine_filter | By Machine!B6 | 25 | 25.0 | PASS |
| down_machine_filter | By Machine!C6 | 2 | 2.0 | PASS |
| down_machine_filter | By Machine!B36 | 55 | 55.0 | PASS |
| down_machine_filter | By Machine!C36 | 3 | 3.0 | PASS |
| down_unknown_negative_zero | Pareto!B6 | 115 | 115.0 | PASS |
| down_unknown_negative_zero | Pareto!B7 | 90 | 90.0 | PASS |
| down_unknown_negative_zero | Pareto!J9 | 10 | 10.0 | PASS |
| down_unknown_negative_zero | Pareto!K9 | 1 | 1.0 | PASS |
| down_unknown_negative_zero | Pareto!J10 | 0 | 0.0 | PASS |
| down_unknown_negative_zero | Pareto!K10 | 0 | 0.0 | PASS |
| down_unknown_negative_zero | Pareto!J11 | 15 | 15.0 | PASS |
| down_unknown_negative_zero | Pareto!K11 | 1 | 1.0 | PASS |
| down_unknown_negative_zero | By Machine!B5 | 100 | 100.0 | PASS |
| down_unknown_negative_zero | By Machine!C5 | 2 | 2.0 | PASS |
| down_unknown_negative_zero | By Machine!B36 | 115 | 115.0 | PASS |
| down_unknown_negative_zero | By Machine!C36 | 3 | 3.0 | PASS |
| down_wildcard_names | Pareto!B6 | 107 | 107.0 | PASS |
| down_wildcard_names | Pareto!B7 | 0 | 0.0 | PASS |
| down_wildcard_names | Pareto!J9 | 10 | 10.0 | PASS |
| down_wildcard_names | Pareto!K9 | 1 | 1.0 | PASS |
| down_wildcard_names | Pareto!J10 | 90 | 90.0 | PASS |
| down_wildcard_names | Pareto!K10 | 1 | 1.0 | PASS |
| down_wildcard_names | Pareto!J11 | 7 | 7.0 | PASS |
| down_wildcard_names | Pareto!K11 | 1 | 1.0 | PASS |
| down_wildcard_names | By Machine!B5 | 10 | 10.0 | PASS |
| down_wildcard_names | By Machine!C5 | 1 | 1.0 | PASS |
| down_wildcard_names | By Machine!B6 | 97 | 97.0 | PASS |
| down_wildcard_names | By Machine!C6 | 2 | 2.0 | PASS |
| down_wildcard_names | By Machine!B36 | 107 | 107.0 | PASS |
| down_wildcard_names | By Machine!C36 | 3 | 3.0 | PASS |
| down_dates | Pareto!B6 | 20 | 20.0 | PASS |
| down_dates | Pareto!B7 | 0 | 0.0 | PASS |
| down_dates | Pareto!J9 | 20 | 20.0 | PASS |
| down_dates | Pareto!K9 | 1 | 1.0 | PASS |
| down_dates | Pareto!J10 | 0 | 0.0 | PASS |
| down_dates | Pareto!K10 | 0 | 0.0 | PASS |
| down_dates | Pareto!J11 | 0 | 0.0 | PASS |
| down_dates | Pareto!K11 | 0 | 0.0 | PASS |
| down_dates | By Machine!B5 | 20 | 20.0 | PASS |
| down_dates | By Machine!C5 | 1 | 1.0 | PASS |
| down_dates | By Machine!B36 | 20 | 20.0 | PASS |
| down_dates | By Machine!C36 | 1 | 1.0 | PASS |
| pm_rules | PM Plan!I5 | Due soon | Due soon | PASS |
| pm_rules | PM Plan!I6 | OVERDUE | OVERDUE | PASS |
| pm_rules | PM Plan!I7 | Check frequency | Check frequency | PASS |
| pm_rules | PM Plan!I8 | Check frequency | Check frequency | PASS |
| pm_rules | PM Plan!I9 | Check frequency | Check frequency | PASS |
| pm_rules | PM Plan!I10 | Duplicate row | Duplicate row | PASS |
| pm_rules | PM Plan!I11 | Duplicate row | Duplicate row | PASS |
| pm_rules | PM Plan!I12 | Due soon | Due soon | PASS |
| pm_rules | PM Plan!I13 | OK | OK | PASS |
| pm_rules | PM Plan!I14 | OK | OK | PASS |
| pm_rules | PM Plan!L1 | 1 | 1.0 | PASS |
| pm_rules | PM Plan!L2 | 2 | 2.0 | PASS |
| pm_rules | PM Plan!L3 | 2 | 2.0 | PASS |
| pm_rules | PM Plan!L4 | 5 | 5.0 | PASS |
| pm_rules | Completion Log!F5 | OK | OK | PASS |
| pm_rules | Completion Log!F6 | OK | OK | PASS |
| pm_rules | Completion Log!F7 | Enter the date done | Enter the date done | PASS |
| pm_rules | Completion Log!F8 | No matching asset + task in plan | No matching asset + task in plan | PASS |
| pm_rules | Completion Log!F9 | OK | OK | PASS |
| pm_rules | Completion Log!F10 | OK | OK | PASS |
<!-- RECHECK_TABLES_END -->
