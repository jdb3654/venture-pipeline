# Discovery: Microsoft ecosystem for SMBs, IT generalists and MSPs

Issue #58. Researched 2026-10-11 by Claude. Budget about 50 lookups; used 48 (22 searches, 26 fetches, one fetch failed; the 48th answered a Codex review finding). $0 spend. No accounts, outreach or publishing.

Labels: **[fact]** verified on the cited page, **[report]** first-hand or secondary report, **[vendor]** vendor claim, **[est]** estimate, **[assume]** assumption. All pages checked 2026-10-11 unless a date is given.

## Bottom line

1. **Every paid route needs an account first.** Microsoft's transactable route needs a verified Partner Center account for a legally registered business with a business domain and email. The no-Microsoft route needs a merchant-of-record account. Raised as #59 (`needs:owner`).
2. **3 of 15 candidates survive Screen**, all in Microsoft 365 governance evidence for tenants too small for Microsoft's premium licences or for mid-market tools with 100-seat minimums. All three need tenant admin consent to read directory or SharePoint data, which keeps operating and security load high.
3. **Forced deadlines are mostly passed or already served.** Teams connectors (May 2026) and InfoPath (July 2026) are done; EWS (April 2027) has free discovery scripts; SMTP AUTH basic auth (end of 2026) can be switched back on by the admin.

## Routes to customers

| Route | Can we charge? | Microsoft's cut and payout | Gate (all approval-gated) | Source |
|---|---|---|---|---|
| Commercial marketplace / AppSource, transactable SaaS | Yes. Microsoft bills, collects tax and pays out. Work or school accounts only. | 3% store fee. Monthly payouts; card sales add a 30-day escrow; $50 payout minimum. | Partner Center account accepting the Microsoft Partner Agreement and Publisher Agreement. No listing fee found. | [fact: Marketplace FAQ, updated 2026-07-23](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/marketplace-faq-publisher-guide) |
| Marketplace listing-only (free trial / contact me) | Yes, off-platform with our own billing. | 0% to Microsoft. | Same Partner Center account. | [fact: same FAQ](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/marketplace-faq-publisher-guide) |
| Office add-ins (Excel, Outlook, Word) | Only indirectly. Add-ins must be free to download; charge by linking a transactable SaaS offer or through "your own payment model" with a sign-in and licence check. | 3% via linked SaaS; 0% via own billing. | Partner Center to list on AppSource. On iOS/Android the add-in may not show any purchase UI, prices or store links (policy 1120.2). Paid features must be disclosed in the listing (1100.1). | [fact: add-in monetization, updated 2025-09-25](https://learn.microsoft.com/en-us/office/dev/store/monetize-addins-through-microsoft-commercial-marketplace); [fact: certification policies](https://learn.microsoft.com/en-us/legal/marketplace/certification-policies) |
| Teams / Microsoft 365 apps and agents | Yes: linked SaaS offer (transactable, free or bring-your-own-licence) or in-app purchase. External payment links allowed only if disclosed in terms, privacy policy and description (1140.3.1). | 3% via linked SaaS. | Partner Center. | [fact: Teams monetization](https://learn.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/appsource/prepare/monetize-overview); [fact: certification policies](https://learn.microsoft.com/en-us/legal/marketplace/certification-policies) |
| Power Platform certified connector | No charge for the connector itself found. Independent publishers (not owning the API) may submit. | — | Certification is free [fact]. All certified connectors are Premium tier [fact], so the customer needs a Power Platform premium licence [assume]. | [fact: connector certification, footer 2025-03-26](https://learn.microsoft.com/nb-no/connectors/custom-connectors/submit-certification) |
| Power Automate templates | No paid route found. | — | — | [assume] |
| PowerShell Gallery, VS Code Marketplace | No paid listing found. Sell licences off-platform with our own merchant of record. | — | Publisher account on each. | [vendor: Dodo Payments guide](https://dodopayments.com/blogs/sell-vscode-extensions); [assume] for PowerShell Gallery |
| Own site + merchant of record (Paddle, Lemon Squeezy) | Yes. | About 5% + $0.50 per sale [assume, not rechecked]. | MoR account. | `BRIEF.md` |
| Microsoft Security Store | Seen as Senserva's listing route; not researched. | Unknown | Unknown | [vendor: Senserva](https://senserva.com/cyber-insurance.html) |

**Partner Center verification** [fact: [Microsoft, updated 2026-07-27](https://learn.microsoft.com/en-nz/partner-center/enroll/understand-the-verification-process)]: legally registered business matching official records, domain registration documents, a business email (no free mail), a primary contact employed by the business, a government ID check. Usually 3–5 business days. No fee mentioned. Whether a sole proprietor qualifies isn't stated; ask Partner Center support. The owner's existing Etsy seller account is an individual/sole proprietor account and a Gmail address (`docs/ACCOUNTS.md`), which would not pass the business-email check.

**Multi-tenant Entra apps** (anything that reads a customer's tenant through Graph): since November 2020, end users can't consent to apps from unverified publishers; an admin still can [report: [Thoughtstuff, 2020-11](https://blog.thoughtstuff.co.uk/2020/11/end-users-can-no-longer-grant-consent-to-unverified-multi-tenant-apps-what-this-means-for-you/)]. Publisher verification uses the Partner Center account. Every survivor below needs admin consent anyway.

### Gated steps, cost and lead time

| Step | Cost | Lead time | Needed for |
|---|---|---|---|
| Business registration (sole prop DBA or LLC; CPA consult already pending in `docs/LEGAL-TAX.md`) | State-dependent [assume] | Days to weeks [assume] | Partner Center |
| Business domain + mailbox | ~$12/year domain [assume]; mailbox cost varies | 1 day | Partner Center, publisher verification, support inbox |
| Partner Center enrolment and verification | $0 found | 3–5 business days [fact] | AppSource, transactable offers, publisher verification |
| Merchant-of-record account | $0 upfront; ~5% + $0.50 per sale [assume] | Days (approval) [assume] | Own billing on any route |
| Power Platform connector certification | $0 [fact] | Not stated | Connectors only |
| Microsoft 365 app compliance (publisher attestation, section 1140.6) | Not read this round | — | Teams / M365 apps |

## Denominator

15 candidates. 0 hit a hard disqualifier. 12 dropped on evidence. 3 advance to Screen. No candidate has outside demand evidence.

| # | Candidate | Lens | Outcome | Main reason |
|---|---|---|---|---|
| 1 | Cyber-insurance evidence pack for small M365 tenants | MSP / admin chores | **Screen (rank 1)** | Consultants charge $1,950 a project for this |
| 2 | Owner access reviews (guests, sharing links) for tenants under 100 seats | Admin chores / MSP | **Screen (rank 2)** | Microsoft charges for reviews; Syskit's floor is 100 users |
| 3 | Pre-Copilot oversharing check | AI-adjacent | **Screen (rank 3)** | SAM costs $3/user/month for tenants without Copilot |
| 4 | Scan-to-email fix for SMTP AUTH basic-auth retirement | Forced deadline | Parked | Admin can re-enable after end of 2026; SMTP2GO and a free OAuth proxy exist |
| 5 | EWS dependency finder | Forced deadline | Killed | Free scripts already find EWS apps; one-off task |
| 6 | Teams Office 365 connector migration | Forced deadline | Killed | Disabled May 18–22, 2026; Workflows is the free replacement |
| 7 | InfoPath form migration | Forced deadline | Parked | Vendors already sell it; per-form project work |
| 8 | SharePoint Add-in replacements | Forced deadline | Parked | Can't be sold on the marketplace; SPFx rebuilds are custom work |
| 9 | Outlook VBA/COM macro replacements for new Outlook | Excel/Outlook power users | Parked | Sperry Software lists 48 Outlook utilities; web add-ins can't act on incoming mail |
| 10 | Outlook mail merge with attachments | Excel/Outlook power users | Parked | Sperry's web add-in and MAPILab already sell it |
| 11 | MSP offboarding and licence clean-up automation | MSP / admin chores | Parked | CIPP: free self-hosted, €99/month hosted |
| 12 | Paid Power Platform connector | Route | Parked | No way to charge for the connector; Premium tier |
| 13 | Paid PowerShell module / VS Code extension | Route | Parked | No paid listing; community scripts are free |
| 14 | AI document extraction inside SharePoint for tenants without Copilot | AI | Parked | Not sourced this round; Microsoft's own AI tools assumed to cover it |
| 15 | Signatures for new Outlook and mobile | Ignored requests | Parked | Crowded paid category [assume, not sourced] |

Long-ignored requests (Microsoft Feedback, Tech Community idea boards) were not mined; budget went to the routes map and verifying deadline dates. That lens is untested, not empty.

### Forced-deadline dates verified

| Change | Date | Status | Source |
|---|---|---|---|
| Office 365 connectors in Teams disabled | 2026-05-18 to 05-22 | Passed | [fact: MC1181996, updated 2026-04-15](https://mc.merill.net/message/MC1181996) |
| InfoPath Forms Services in SharePoint Online retired | 2026-07-14 | Passed; some forms still render | [vendor: Lightning Tools, 2026-08-14](https://lightningtools.com/blog/infopath-still-working-sharepoint-online-retirement-2026/) |
| EWS off by default in Exchange Online | 2026-10-01 | Passed; admin can re-enable | [fact: MC1227454, 2026-02-05](https://mc.merill.net/message/MC1227454) |
| EWS permanently removed | 2027-04-01 | Open | same |
| SMTP AUTH basic auth off by default | End of December 2026 | Open; admin can reverse; final date to be announced H2 2027 | [report: Office 365 for IT Pros, 2026-01-29](https://office365itpros.com/2026/01/29/smtp-auth-basic-retirement/amp/) |
| New Outlook opt-out phase for enterprise | March 2027 | Open; classic Outlook supported to 2029 per the same source | [vendor: CloudFiler, 2026-03-03, citing MC949965](https://cloudfiler.io/blogs/news/microsoft-announce-new-march-2027-deadline-for-new-outlook-impacts-and-planning-tips) |

### Sources for parked and killed rows

- SMTP alternatives (SMTP2GO, email-oauth2-proxy): Office 365 for IT Pros, link above.
- EWS discovery scripts: [LazyAdmin](https://lazyadmin.nl/?p=12999), [EWS-App-Identifier on GitHub](https://github.com/peterschmidtdk/EWS-App-Identifier).
- InfoPath vendors: Lightning Tools (above), [Crow Canyon](https://www.crowcanyon.com/blog/infopath-end-of-life-migration-guide/).
- SharePoint Add-ins can no longer be sold on the marketplace: [add-in monetization page](https://learn.microsoft.com/en-us/office/dev/store/monetize-addins-through-microsoft-commercial-marketplace).
- Sperry Software's 48 Outlook add-ins: [Robert 365 directory](https://robert365.com/app/publisher/sperry); Send Individually web add-in: [AppSource](https://appsource.microsoft.com/en-us/product/office/WA200007008); MAPILab Mail Merge Toolkit: [MAPILab](https://www.mapilab.com/about/news/outlook_mail_merge_pro.html).
- CIPP pricing: [CyberDrain](https://cyberdrain.com/pricing/). CIPP's offboarding and licence features are [assume] from its reputation; not read this round.

### Overlap with earlier rounds

The old MSP handover idea was a one-time documentation package when an MSP takes over a client. Candidates 1 and 2 are recurring evidence for a third party (an insurer, or the business owner), and candidate 11 is a weekly chore. Candidate 11 is parked for the same broad reason (crowding), with CIPP as the specific competitor.
