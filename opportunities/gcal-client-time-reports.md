# Calendar time reports for client billing

- **Slug:** gcal-client-time-reports
- **Stage:** Screen (near-miss: Distribution 3, below the round's bar of 4)
- **Owner agent:** claude
- **Created / last updated:** 2026-10-11 / 2026-10-11
- **Last outside evidence:** none yet (desk research only, issue #65)

Labels: **[fact]** verified on the cited page, **[report]** first-hand or secondary report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. Pages checked 2026-10-11.

## The idea in two sentences

A Google Calendar add-on that turns calendar events into billable-hours reports per client or project in Sheets, using AI to assign events to clients from titles and attendees. Buyers are freelancers and small consultancies who already live in Google Calendar and bill by the hour.

## Signal

Lenses: paid apps with complaints; workarounds (calendar export to spreadsheets). Found while searching the Workspace Marketplace for calendar-to-timesheet tools.

## Customers and distribution

- **Buyers:** consultants, agencies, coaches who bill hourly [assume]. Today: Time Reports Pro, Calrows, Timesheet/Timecard add-ons, or manual export [fact: listed in [Marketplace search results](https://workspace.google.com/marketplace/app/calrows_kalendersync_export_stundenzette/163011926713)].
- **Route without ads:** Workspace Marketplace search for "time report", "timesheet", "calendar export".
- **Named paid competitor:** Time Reports Pro (Wonderland Ventures LLC), **$12/user/month** after a 7-day trial; 5.0 rating from 189 reviews; listing updated 2026-09-30 [fact: [Marketplace listing](https://workspace.google.com/marketplace/app/time_reports_pro/956232481109)]. Reviews are engagement, not sales.
- **Complaints:** the only visible one (2026-09-04) was about cancelling billing; the developer resolved it within a week [fact: same listing]. No recurring functional complaint found.

## Scopes

Time Reports Pro requests all Sheets files, full read/write on all calendars, and connection to an external service [fact: same listing]. A rival needs at least read-only calendar access plus a Sheets output, and an AI step sends event titles and attendee names to a model provider [assume]. Google classifies reading Calendar events as a sensitive scope: brand verification, scope justification and a demo video, typically 3–5 business days, with no security assessment or fee mentioned [fact: [Google, updated 2026-08-19](https://developers.google.com/identity/protocols/oauth2/production-readiness/sensitive-scope-verification)]. No CASA unless the design adds a restricted scope such as Drive.

## Strongest reason it fails

The need is already met by a well-reviewed $12 app with a moat of 189 reviews, and nothing in its reviews says customers are unhappy. "AI assigns events to clients" is a feature the incumbent can add in a sprint. We would be the fourth-best-reviewed listing in a search with no gap to point to.

## Scores

5 = most favorable.

| Factor | 1–5 | Justification and source |
|---|---|---|
| Distribution | 3 | Marketplace search finds the category, but a 189-review, 5.0 incumbent sits on it [fact: listing]. |
| Willingness to pay | 4 | Published $12/user/month for exactly this job [fact: listing]; reviews show use, not sales. |
| Build effort | 3 | Calendar add-on, Sheets output and an AI classifier; sensitive-scope OAuth verification (3–5 business days) before public listing [fact: Google]. |
| Operating load | 2 | Full calendar read access and third-party AI processing of attendee data; billing disputes are money-adjacent [assume]. |
| Owner time | 4 | Self-serve; escalations only [assume]. |
| Legal and compliance load | 3 | Personal data of meeting attendees sent to an AI provider; Google API user-data policy [assume]. |
| Sellability | 3 | Small recurring SaaS; buyable if it has customers [assume]. |
| Window | 3 | Stable category; Google Calendar's own time insights could widen [assume]. |
| Cost | 4 | Near $0 at low volume; sensitive-scope verification has no fee mentioned [fact: Google]; AI calls a few cents per report [est]. |

Disqualifiers checked: none. No regulated data unless a customer's events contain it [assume].

## Economics (estimates, not forecasts)

- Price: $8/user/month to undercut the incumbent [est].
- Running cost at launch: under $10/month [est].
- MoR fee about 5% + $0.50 per sale [assume, per #59].
- $1k/month owner cash: about 140 paying users [est].

## Owner tasks that remain

Approve a Google Cloud project and public listing; approve the MoR account (#59).

## Validation plan

Cheapest test with no new account: a landing page describing "client-sorted billable hours from your calendar" with a waitlist, on the repo's existing GitHub Pages (needs owner approval to publish; $0). Run 30 days. Pass: 30 signups from search or one non-spam community post. Fail: under 10. The test doesn't touch the incumbent's moat, so a pass would still need a differentiator before Build.

## Kill criteria

Fail the waitlist test, or find that Time Reports Pro already classifies events by client.

## Exit

A time-tracking vendor buying a Workspace foothold [assume]. Needs separate Google Cloud and MoR accounts in the product's name.

## Decision log

- 2026-10-11: Screened as near-miss 1 in round 1 (#65), by Claude. Fails the round bar on Distribution (3). Not sent to case-against.
