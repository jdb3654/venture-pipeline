"""Build the buyer-facing step-by-step PDF guides.

Run: python3 build_guides.py <screenshot dir>
The screenshot dir comes from: python3 preview.py <soffice.py> <dir> 220
Writes guides/*.pdf: one per template, plus a combined guide for the bundle.
Keep the text in sync with build.py: every limit, column and message below is taken from it.
"""
import sys
from pathlib import Path

from PIL import Image
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (Image as RLImage, KeepTogether, ListFlowable, ListItem, PageBreak, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

HERE = Path(__file__).parent
OUT = HERE / "guides"
LOGO = HERE.parent.parent / "brand" / "takttools-icon-1000.png"
NAVY = colors.HexColor("#1F3A5F")
ORANGE = colors.HexColor("#C85F00")  # darker than the logo orange so text stays readable
YELLOW = colors.HexColor("#FFF2CC")
GREY = colors.HexColor("#F2F2F2")
INK = colors.HexColor("#222222")
MUTED = colors.HexColor("#555555")
WIDTH = letter[0] - 1.6 * inch

S = {
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=24, leading=29, textColor=NAVY, spaceAfter=4),
    "sub": ParagraphStyle("sub", fontName="Helvetica", fontSize=12, leading=16, textColor=MUTED, spaceAfter=14),
    "h1": ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=NAVY, spaceBefore=14, spaceAfter=6, keepWithNext=1),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=INK, spaceBefore=8, spaceAfter=4, keepWithNext=1),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10.5, leading=14.5, textColor=INK, spaceAfter=6, alignment=TA_LEFT),
    "small": ParagraphStyle("small", fontName="Helvetica", fontSize=9, leading=12, textColor=MUTED, spaceAfter=4),
    "cell": ParagraphStyle("cell", fontName="Helvetica", fontSize=9.5, leading=12.5, textColor=INK),
    "cellb": ParagraphStyle("cellb", fontName="Helvetica-Bold", fontSize=9.5, leading=12.5, textColor=colors.white),
}


def p(text, style="body"):
    return Paragraph(text, S[style])


def steps(items):
    return ListFlowable([ListItem(p(t), leftIndent=14, value=i + 1) for i, t in enumerate(items)],
                        bulletType="1", bulletFontName="Helvetica-Bold", bulletColor=NAVY, leftIndent=18,
                        spaceAfter=6)


def bullets(items):
    return ListFlowable([ListItem(p(t), leftIndent=12) for t in items], bulletType="bullet", start="•",
                        leftIndent=16, bulletColor=NAVY, spaceAfter=6)


def table(rows, widths):
    data = [[Paragraph(c, S["cellb"] if r == 0 else S["cell"]) for c in row] for r, row in enumerate(rows)]
    t = Table(data, colWidths=[w * WIDTH for w in widths], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#D9D9D9")),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F8FA")]),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def colour_key():
    t = Table([[Paragraph("Yellow cells: type here.", S["cell"]),
                Paragraph("Grey cells: calculated. Don't type over them.", S["cell"])]],
              colWidths=[WIDTH / 2, WIDTH / 2])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, 0), YELLOW), ("BACKGROUND", (1, 0), (1, 0), GREY),
                           ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#BFBFBF")),
                           ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#BFBFBF")),
                           ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
    return t


class Shots:
    def __init__(self, folder):
        self.folder = Path(folder)
        self.tmp = OUT / "_img"
        self.tmp.mkdir(parents=True, exist_ok=True)

    def __call__(self, name, caption, max_h=3.6):
        im = Image.open(self.folder / f"{name}.png").convert("RGB")
        box = im.convert("L").point(lambda v: 255 if v < 250 else 0).getbbox()
        pad = 20
        im = im.crop((max(box[0] - pad, 0), max(box[1] - pad, 0), min(box[2] + pad, im.width), min(box[3] + pad, im.height)))
        path = self.tmp / f"{name}.png"
        im.save(path)
        w = WIDTH
        h = w * im.height / im.width
        if h > max_h * inch:
            h = max_h * inch
            w = h * im.width / im.height
        img = RLImage(str(path), width=w, height=h)
        frame = Table([[img]], colWidths=[WIDTH])
        frame.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#BFBFBF")),
                                   ("ALIGN", (0, 0), (-1, -1), "CENTER")]))
        return KeepTogether([frame, p(caption, "small"), Spacer(1, 6)])


def header(title, subtitle):
    logo = RLImage(str(LOGO), width=0.7 * inch, height=0.7 * inch)
    t = Table([[logo, [p(title, "title"), p(subtitle, "sub")]]], colWidths=[0.9 * inch, WIDTH - 0.9 * inch])
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 0)]))
    return t


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(0.8 * inch, 0.55 * inch, f"TaktTools  ·  {doc.title}")
    canvas.drawRightString(letter[0] - 0.8 * inch, 0.55 * inch, f"Page {doc.page}")
    canvas.setStrokeColor(colors.HexColor("#D9D9D9"))
    canvas.line(0.8 * inch, 0.75 * inch, letter[0] - 0.8 * inch, 0.75 * inch)
    canvas.restoreState()


COMMON_START = [
    "Open the file in your spreadsheet app (see <b>Works with</b> in the listing). If Excel shows a yellow "
    "<i>Protected View</i> bar because the file was downloaded, click <b>Enable Editing</b>.",
    "Save a copy under your own name (for example, add your plant or year) and keep the original download as a clean "
    "spare.",
    "Read the <b>How to use</b> sheet. It's a one-page summary of this guide.",
]

CLEAR_EXAMPLES = ("The rows marked <b>EXAMPLE</b> show the expected format. When you're ready, select just their "
                  "<b>yellow</b> cells and press <b>Delete</b> to clear them. Don't delete whole rows: that removes the "
                  "formulas in the grey columns too.")

SUPPORT = [
    p("Need help?", "h1"),
    p("Message us through Etsy (the <b>Message seller</b> button on our shop or your order). Tell us which file, which "
      "sheet, and what you typed. We answer questions about using the templates as described in this guide; we "
      "can't do custom changes or set-up work."),
    p("These templates were designed with help from AI tools and checked by the seller.", "small"),
]


def oee(shot):
    return [
        header("OEE Tracker", "Step-by-step guide: track Overall Equipment Effectiveness by machine and shift"),
        p("What it does", "h1"),
        p("You log one row per machine per shift. The workbook calculates Availability, Performance, Quality and OEE "
          "for every row, then summarizes each machine on the <b>Dashboard</b> for any date range you choose, with a "
          "chart and a comparison to your target."),
        colour_key(),
        p("The sheets", "h1"),
        table([["Sheet", "What it's for"],
               ["How to use", "A one-page summary."],
               ["Setup", "Your machines and each one's ideal cycle time. Up to 20 machines."],
               ["Production Log", "One row per machine per shift. Up to 500 rows."],
               ["Dashboard", "Totals and OEE by machine for a date range, plus a chart."]], [0.25, 0.75]),
        p("Before you start", "h1"),
        steps(COMMON_START),
        p("Step 1: Set up your machines", "h1"),
        steps([
            "Go to the <b>Setup</b> sheet.",
            "In <b>Machine</b>, type each machine's name once, one per row (up to 20). Use the names your team already "
            "uses.",
            "In <b>Ideal cycle time (seconds per part)</b>, enter the fastest time the machine can sustainably make "
            "one good part. For a line, use the time per finished unit at rated speed. Example: a machine rated at "
            "300 parts per hour has an ideal cycle time of 3600 / 300 = <b>12 seconds</b>.",
            "Type each machine only once. If a name is repeated, <b>Check</b> on the repeat says <b>Duplicate: only "
            "the first row is used</b>; delete the repeat.",
            "Clear the three EXAMPLE machines when you no longer need them (yellow cells only).",
        ]),
        p("Getting the ideal cycle time right matters most: if it's too slow, Performance can show over 100% and the "
          "Check column will flag it.", "small"),
        p("Step 2: Log each shift", "h1"),
        steps([
            "Go to the <b>Production Log</b> sheet.",
            "Fill in one row per machine per shift. The yellow columns are: <b>Date</b>, <b>Shift</b> (any label, "
            "e.g. Day or 1st), <b>Machine</b> (pick from the drop-down), <b>Shift length (min)</b>, <b>Planned stops "
            "(min)</b>, <b>Unplanned downtime (min)</b>, <b>Total parts</b> and <b>Rejected parts</b>. Shift length "
            "and total parts are required; blank planned stops, downtime or rejects count as 0.",
            "<b>Planned stops</b> are times the machine isn't expected to run, like breaks and scheduled meetings. "
            "<b>Unplanned downtime</b> is every other minute it was stopped: breakdowns, changeovers, waiting for "
            "material.",
            "The grey columns fill in by themselves, including <b>OEE</b> (coloured green, amber or red) and "
            "<b>Check</b>.",
            "Look at <b>Check</b> on each new row. It should say <b>OK</b>. If not, see the table below. Rows with an "
            "error are left out of the Dashboard until you fix them. The \"performance above 100%\" warning is not an "
            "error: those rows still count.",
            CLEAR_EXAMPLES,
        ]),
        shot("OEE-Tracker-3", "Production Log with the example rows. Yellow columns are typed in; grey columns calculate."),
        p("What the Check column means", "h2"),
        table([["Message", "What to do"],
               ["Machine not in Setup", "The machine name isn't on the Setup sheet, or is spelled differently. Pick "
                "it from the drop-down, or add it to Setup."],
               ["Set an ideal cycle time in Setup", "The machine has no ideal cycle time (or 0) on the Setup sheet."],
               ["Enter a date", "The Date cell is empty or isn't a real date. Undated rows can't be placed in a date "
                "range, so they are left out."],
               ["Enter numbers: shift length and total parts are required", "A required cell is empty, or a cell "
                "contains text instead of a number."],
               ["Values must be 0 or more (shift length above 0)", "A negative number, or a shift length of 0."],
               ["Rejects > total parts", "Rejected parts must be part of the total. Fix one of the two numbers."],
               ["Planned stops >= shift length", "Planned stops leave no time to run. Check both numbers."],
               ["Downtime > planned time", "Unplanned downtime is longer than shift length minus planned stops. "
                "Check the three time columns."],
               ["Check: performance above 100%", "A warning only; the row still counts. The machine made parts faster "
                "than its ideal cycle time allows. Usually the cycle time in Setup is too slow, or the count is wrong."],
               ["OK", "Nothing obviously wrong."]], [0.38, 0.62]),
        p("Step 3: Read the Dashboard", "h1"),
        steps([
            "Go to the <b>Dashboard</b> sheet.",
            "Optional: enter a <b>From date</b> and/or <b>To date</b>. Leave them blank to include every row. Both "
            "dates are included in the range.",
            "Set your <b>OEE target</b> (85% is filled in). OEE cells turn <b>green</b> at or above target, "
            "<b>amber</b> from 60% up to the target, and <b>red</b> below 60%. Red always wins: below 60% is red even "
            "if your target is lower than 60%. <b>OEE vs target</b> shows the gap.",
            "Each row adds up times and part counts first, then calculates the percentages, so a long shift counts "
            "more than a short one. <b>All machines</b> OEE is total ideal time for good parts divided by total "
            "planned production time, which stays correct when machines have different cycle times. Its <b>Quality</b> "
            "is weighted by ideal time (ideal time for good parts ÷ ideal time for all parts), so Availability × "
            "Performance × Quality still equals OEE.",
        ]),
        shot("OEE-Tracker-4", "Dashboard: totals and OEE by machine, the all-machines total, and the OEE chart.", 4.4),
        p("How the numbers are calculated", "h1"),
        table([["Measure", "Formula"],
               ["Planned production time", "Shift length - planned stops"],
               ["Run time", "Planned production time - unplanned downtime"],
               ["Availability", "Run time ÷ planned production time"],
               ["Performance", "(Ideal cycle time × total parts) ÷ run time"],
               ["Quality", "Good parts ÷ total parts (good parts = total - rejected)"],
               ["OEE", "Availability × Performance × Quality = (ideal cycle time × good parts) ÷ planned "
                "production time"]], [0.35, 0.65]),
        p("85% OEE is a commonly cited \"world-class\" benchmark. Many plants start well below it; improving against "
          "your own baseline matters more.", "small"),
        p("Questions", "h1"),
        p("<b>The log is full (500 rows). What now?</b> Save the workbook as a new file for the next period (for "
          "example, one per quarter), clear the yellow cells in the log, and keep going.", "body"),
        p("<b>Can I add more than 20 machines?</b> Not in this version. Message us if you need more.", "body"),
        p("<b>Can I rename the sheets or move columns?</b> Please don't. The formulas refer to them by position.", "body"),
        *SUPPORT,
    ]


def downtime(shot):
    return [
        header("Downtime Log & Pareto", "Step-by-step guide: log every stop and see which causes cost the most time"),
        p("What it does", "h1"),
        p("You record each stop with a reason. The <b>Pareto</b> sheet ranks the reasons by minutes lost, with each "
          "reason's share and the running total, so you can see the few causes behind most of your downtime. Filter "
          "by date range and machine."),
        colour_key(),
        p("The sheets", "h1"),
        table([["Sheet", "What it's for"],
               ["How to use", "A one-page summary."],
               ["Setup", "Your machines (up to 30) and your downtime reasons with categories (up to 30)."],
               ["Downtime Log", "One row per stop. Up to 1,000 rows."],
               ["Pareto", "Reasons ranked by minutes lost, with a Pareto chart of the top 12."],
               ["By Machine", "Downtime minutes and stop counts per machine."]], [0.25, 0.75]),
        p("Before you start", "h1"),
        steps(COMMON_START),
        p("Step 1: Set up machines and reasons", "h1"),
        steps([
            "Go to the <b>Setup</b> sheet.",
            "Under <b>Machine</b>, list your machines, one per row.",
            "Under <b>Downtime reason</b> and <b>Category</b>, edit the 12 starter reasons to match how your plant "
            "talks about stops. Keep the list short, about 10 to 15 reasons. Categories (Breakdown, Material, and so "
            "on) can be renamed too.",
            "List each machine and each reason only once. A repeated name shows <b>Duplicate: only the first row is "
            "used</b> in the <b>Check</b> column next to it; delete the repeat.",
        ]),
        shot("Downtime-Log-and-Pareto-2", "Setup: machines on the left, reasons and categories on the right.", 3.2),
        p("Step 2: Log every stop", "h1"),
        steps([
            "Go to the <b>Downtime Log</b> sheet and use one row per stop.",
            "Enter <b>Date</b>, <b>Shift</b> and <b>Machine</b> (from the drop-down).",
            "Enter <b>Start</b> and <b>End</b> as times, like <b>7:15</b> and <b>7:50</b>. A stop that crosses "
            "midnight, like 23:40 to 0:25, is handled automatically (45 minutes).",
            "If you only know how long it lasted, leave Start and End blank and type the minutes in <b>Minutes (if "
            "no start/end)</b>. Typed minutes always win over start and end times.",
            "Pick a <b>Reason</b> from the drop-down. <b>Duration</b>, <b>Category</b> and <b>Check</b> fill in by "
            "themselves. Check should say <b>OK</b>; otherwise it tells you what's missing, such as a date, a "
            "reason, or minutes that aren't a number of 0 or more.",
            "Add <b>Notes</b> if useful, especially for \"Other\".",
            CLEAR_EXAMPLES,
        ]),
        shot("Downtime-Log-and-Pareto-3", "Downtime Log with the example rows, including a stop that crosses midnight."),
        p("If <b>Category</b> shows <b>Not in Setup</b>, the reason was typed instead of picked, or is spelled "
          "differently from the Setup list. Its minutes still count in the total, under <b>Unclassified</b> on the "
          "Pareto sheet. Pick the reason from the drop-down so it's counted under the right reason. A row counts as "
          "a <b>stop</b> when its duration is more than 0 minutes; rows without a date, or with invalid minutes, are "
          "left out of the totals.", "small"),
        p("Step 3: Read the Pareto", "h1"),
        steps([
            "Go to the <b>Pareto</b> sheet.",
            "Optional: set <b>From date</b>, <b>To date</b> and <b>Machine</b>. Leave any of them blank to include "
            "everything. Both dates are included in the range.",
            "<b>Total downtime</b> is every valid logged minute in the range. <b>Unclassified</b> shows minutes whose "
            "reason is blank or not on the Setup list. Fix those in the log so they're ranked.",
            "Read the table from the top: <b>Rank</b>, <b>Reason</b>, <b>Minutes</b>, <b>Stops</b>, <b>% of "
            "total</b> and <b>Cumulative %</b>. Reasons with no minutes in the range are left out.",
            "The chart shows the top 12 reasons as bars, with the cumulative % as a line on the right-hand axis.",
            "Start improvement work with the reasons at the top. Often the first two or three account for most of "
            "the lost time.",
        ]),
        shot("Downtime-Log-and-Pareto-4", "Pareto: reasons ranked by minutes, with cumulative % and the Pareto chart."),
        p("Step 4: Compare machines", "h1"),
        p("The <b>By Machine</b> sheet shows total downtime, number of stops, average minutes per stop and each "
          "machine's share of all downtime, plus <b>No machine / not in Setup</b> and <b>All logged downtime</b> "
          "rows so the totals always add up. It uses the date range set on the Pareto sheet; the machine filter "
          "doesn't apply here."),
        shot("Downtime-Log-and-Pareto-5", "By Machine: downtime minutes, stops and share per machine.", 2.6),
        p("Tips", "h1"),
        bullets([
            "If <b>Other</b> climbs into your top reasons, read its notes and add the missing reason to Setup.",
            "Durations are rounded to whole minutes.",
            "Log stops the same day, while people remember the cause.",
        ]),
        p("Questions", "h1"),
        p("<b>The log is full (1,000 rows). What now?</b> Save the workbook as a new file for the next period, clear "
          "the yellow cells in the log, and keep going."),
        p("<b>Can I rename the sheets or move columns?</b> Please don't. The formulas refer to them by position."),
        *SUPPORT,
    ]


def pm(shot):
    return [
        header("Preventive Maintenance Schedule", "Step-by-step guide: plan recurring maintenance and see what's due"),
        p("What it does", "h1"),
        p("You list each recurring maintenance task and how often it's due. Each time a task is done, you add a line "
          "to the <b>Completion Log</b>. The plan then shows each task's last completion, next due date, days left "
          "and a colour-coded status."),
        colour_key(),
        p("The sheets", "h1"),
        table([["Sheet", "What it's for"],
               ["How to use", "A one-page summary."],
               ["PM Plan", "One row per asset and task, with status. Up to 300 tasks."],
               ["Completion Log", "One row each time a task is done. Up to 2,000 rows."]], [0.25, 0.75]),
        p("Before you start", "h1"),
        steps(COMMON_START),
        p("Step 1: Build your plan", "h1"),
        steps([
            "Go to the <b>PM Plan</b> sheet.",
            "Add one row per asset and task. Fill in <b>Asset</b>, <b>Task</b>, <b>Frequency (days)</b> and "
            "<b>Assigned to</b>. The frequency is a fixed number of days: 1 = daily, 7 = weekly, 14 = every two "
            "weeks, 30 = about monthly, 90 = about quarterly, 365 = about yearly.",
            "If you know when a task was last done before you started using this workbook, enter that date in "
            "<b>Last done before log</b>. Otherwise leave it blank: the task shows as due today, every day, until you "
            "log it or enter a date.",
            "Keep each asset + task combination on one row only. A repeated combination shows <b>Duplicate row</b>; "
            "a blank, zero or negative frequency shows <b>Check frequency</b>. Both are counted under <b>Needs "
            "fixing</b> at the top right.",
            CLEAR_EXAMPLES,
        ]),
        shot("Preventive-Maintenance-Schedule-2", "PM Plan with example tasks, statuses and the counts box (top right)."),
        p("Step 2: Log completed work", "h1"),
        steps([
            "Go to the <b>Completion Log</b> sheet.",
            "Each time a task is done, add a row: <b>Date done</b>, <b>Asset</b> and <b>Task</b> (pick both from the "
            "drop-downs so they match the plan exactly), <b>Done by</b> and any <b>Notes</b>.",
            "Check <b>Matches plan?</b>. It should say <b>OK</b>. <b>Enter the date done</b> means the date is missing. "
            "<b>Fill in asset and task</b> means one of them is blank. "
            "<b>No matching asset + task in plan</b> means the asset or task is spelled differently from the PM "
            "Plan, so the plan won't update. Fix the spelling.",
        ]),
        shot("Preventive-Maintenance-Schedule-3", "Completion Log: each completion updates the plan."),
        p("Step 3: Read the plan", "h1"),
        steps([
            "Back on <b>PM Plan</b>, the grey columns update automatically: <b>Last completed</b> (the most recent of "
            "the logged dates and the before-log date), <b>Next due</b>, <b>Days until due</b> and <b>Status</b>.",
            "<b>OVERDUE</b> (red) means the due date has passed. <b>Due soon</b> (amber) means it's due within the "
            "window. <b>OK</b> (green) means it's not due yet.",
            "Change the <b>Due soon window (days)</b> at the top of the sheet. It starts at 7.",
            "The counts box at the top right shows how many tasks are Overdue, Due soon, OK, and Needs fixing.",
            "To get this week's work list, sort or filter by Status: <b>Data > Filter</b> in Excel.",
        ]),
        p("Dates and statuses use today's date from your computer, so they change from day to day. The example rows "
          "are set relative to today for the same reason.", "small"),
        p("Questions", "h1"),
        p("<b>What if a task is done early?</b> Log the actual date. The next due date counts from the last completion."),
        p("<b>The Completion Log is full.</b> Save the workbook as a new file, enter each task's most recent date in "
          "<b>Last done before log</b>, clear the yellow cells in the log, and keep going."),
        p("<b>Can I rename the sheets or move columns?</b> Please don't. The formulas refer to them by position."),
        *SUPPORT,
    ]


def build(name, title, parts, shots):
    OUT.mkdir(exist_ok=True)
    doc = SimpleDocTemplate(str(OUT / name), pagesize=letter, leftMargin=0.8 * inch, rightMargin=0.8 * inch,
                            topMargin=0.7 * inch, bottomMargin=0.95 * inch, title=title, author="TaktTools",
                            subject="Step-by-step guide", creator="TaktTools")
    story = []
    for i, part in enumerate(parts):
        if i:
            story.append(PageBreak())
        story.extend(part(shots))
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print("wrote", OUT / name)


if __name__ == "__main__":
    shots = Shots(sys.argv[1])
    build("OEE-Tracker-Guide.pdf", "OEE Tracker guide", [oee], shots)
    build("Downtime-Log-and-Pareto-Guide.pdf", "Downtime Log & Pareto guide", [downtime], shots)
    build("Preventive-Maintenance-Schedule-Guide.pdf", "Preventive Maintenance Schedule guide", [pm], shots)
    build("Manufacturing-Bundle-Guide.pdf", "Manufacturing templates bundle guide", [oee, downtime, pm], shots)
    import shutil
    shutil.rmtree(OUT / "_img")
