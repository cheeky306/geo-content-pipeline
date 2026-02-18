---
description: Schedule long-term maintenance and refreshes. Identifies volatile sections, sets review dates, defines refresh triggers, tracks dependencies. Keeps content authoritative over time.
---

# STEP 10 — Maintenance Scheduling

## Overview

Maintenance Scheduling ensures that your published content remains authoritative and accurate over time. A piece published today may contain claims that become outdated, statistics that age, or references that break. This step identifies what needs to be refreshed and when, and creates a proactive maintenance schedule.

Content authority compounds over time, but only if it is maintained. A piece with outdated statistics loses credibility. A piece with broken links creates poor user experience. A piece that contradicts new research becomes a liability. This step prevents that decay.

Maintenance scheduling is the difference between content that has a shelf life and content that compounds authority year after year. The goal is a sustainable approach to keeping your content current and valuable.

Expect this step to take 10-15 minutes. You will identify refresh triggers, assign review dates, and log dependencies.

## Workflow

### Inputs (Human)

Published piece (verified as working in Step 9):

* Live URL
* Final published content
* All sources and citations
* All statistics and claims
* Internal links

Also required:

* Topic statement from Step 1
* Sources list from Step 4
* Any risks identified in Step 8
* Calendar/scheduling system for reminders

### Copilot Actions

1. Identify volatile sections:
   * Scan the content for claims that may age or change
   * Look for:
     * Statistics with publication years (especially current year)
     * Platform features or policies (e.g., "Google currently…")
     * Technology roadmaps or versions (e.g., "WooCommerce 8.0")
     * Market predictions or growth rates
     * Regulatory changes (e.g., "As of 2024…")
   * Flag each volatile claim with a refresh trigger
   * Example: "Section: Product Description Best Practices / Claim: 'AI agents prioritize metadata' / Refresh if: New research contradicts this"

2. Categorize by volatility level:
   * High: Likely to change within 6–12 months
   * Medium: May change within 12–24 months
   * Low: Unlikely to change; evergreen content
   * Examples:
     * High volatility: "Current AI adoption rate is X%"
     * Medium volatility: "WooCommerce best practices for [feature]"
     * Low volatility: "Why product descriptions matter"

3. Set review and refresh dates:
   * Calculate based on volatility:
     * High volatility: Review every 3 months
     * Medium volatility: Review every 6–12 months
     * Low volatility: Review annually or as-needed
   * Assign specific calendar dates
   * Example:
     * Published: February 2026
     * First review: May 2026 (3 months, high-volatility content)
     * Second review: August 2026 (6 months)
     * Third review: February 2027 (annual)

4. Identify source dependencies:
   * List all external sources cited in the piece
   * Flag sources that may change or disappear
   * Identify third-party tools, platforms, or data that the piece depends on
   * Example dependencies:
     * Google Search Console data (may change with updates)
     * Industry reports (may be superseded by newer reports)
     * Tool features (may be deprecated)
     * Statistics (may be updated with new research)

5. Define refresh triggers:
   * Specify the condition that triggers a refresh
   * Make triggers clear and testable
   * Examples:
     * Trigger: "If Google announces changes to AI Overview display format" → Refresh metadata section
     * Trigger: "If new WooCommerce major version is released" → Refresh version references
     * Trigger: "If competitive piece published on same topic" → Update with new insights or comparison
     * Trigger: "If external report is updated with new data" → Update statistics
     * Trigger: "If traffic declines >30% month-over-month" → Audit and refresh

6. Identify quick-update sections:
   * Which sections can be updated without major rewrites?
   * Which sections would require full rewrite if they change?
   * Examples:
     * Quick-update: Statistics (change number and source)
     * Quick-update: Platform features (update feature list)
     * Full-rewrite: Core methodology or framework (if it changes fundamentally)
     * Full-rewrite: Thesis or main claim (if research contradicts it)

7. Plan content relationships:
   * Identify other pieces that build on this one
   * Identify pillar content this piece supports
   * Note: if this piece is refreshed, do related pieces need updates?
   * Example: "This post is cited in [other blog post]. If we significantly change claims, update that post too."

8. Create maintenance log:
   * Document everything in a searchable log
   * Include:
     * Section titles and volatile claims
     * Volatility level
     * Review date
     * Refresh trigger
     * Last reviewed date (blank initially)
     * Last updated date (blank initially)

### Outputs

The copilot produces:

* Maintenance Schedule (template for ongoing tracking):

```
═══════════════════════════════════════════════════
MAINTENANCE SCHEDULE
═══════════════════════════════════════════════════

Content: How to Write Product Descriptions AI Agents Can Parse
Published: February 2026
URL: https://yoursite.com/blog/product-descriptions-ai-agents/
Status: Published and live

SCHEDULED REVIEWS

Review 1: May 15, 2026 (3 months post-publish)
  Purpose: Check for new research or AI agent behavior changes
  Focus: H2 "How AI Agents Evaluate Descriptions"

Review 2: August 15, 2026 (6 months post-publish)
  Purpose: Assess performance; update if needed
  Focus: All sections; full content audit

Review 3: February 15, 2027 (12 months post-publish)
  Purpose: Annual refresh; update statistics
  Focus: Any statistics or claims with 2024 publication dates

═══════════════════════════════════════════════════

VOLATILE SECTIONS & REFRESH TRIGGERS

Section 1: Product Description Best Practices
  Claim: "AI agents prioritize 5 key attributes: [list]"
  Volatility: Medium (likely stable but research may improve)
  Refresh Trigger: If new peer-reviewed research contradicts attributes
  Review Date: August 2026
  Last Reviewed: [blank]
  Last Updated: [blank]

Section 2: Optimal Description Length
  Claim: "Product descriptions should be 100–200 words"
  Volatility: Medium (may evolve as AI agents improve)
  Refresh Trigger: If benchmark study shows different optimal length
  Review Date: June 2026
  Last Reviewed: [blank]
  Last Updated: [blank]

Section 3: Market Adoption Statistics
  Claim: "60% of merchants use [platform]"
  Volatility: High (market data changes annually)
  Refresh Trigger: When new market research is published (e.g., W3Techs 2025 data)
  Review Date: Q1 2027
  Last Reviewed: [blank]
  Last Updated: [blank]

Section 4: WooCommerce Feature References
  Claim: "WooCommerce supports [feature] as of v8.0"
  Volatility: High (changes with major version releases)
  Refresh Trigger: When WooCommerce major version is released
  Review Date: Upon major WooCommerce release
  Last Reviewed: [blank]
  Last Updated: [blank]

Section 5: Google Policy References
  Claim: "According to Google Search Console docs (2024)"
  Volatility: Medium (platform policies may change)
  Refresh Trigger: When Google Search Console documentation is updated
  Review Date: Ongoing monitoring
  Last Reviewed: [blank]
  Last Updated: [blank]

═══════════════════════════════════════════════════

SOURCE DEPENDENCIES

Source 1: W3Techs Market Share Data
  Status: External, publicly available
  Last Updated: [check current]
  Risk: Data is updated annually; current data may age
  Action: Refresh annually or when new data is published

Source 2: Google Search Console Documentation
  Status: External, proprietary
  Last Updated: [check current]
  Risk: Google may update documentation; links may change
  Action: Monitor for updates; re-verify links quarterly

Source 3: [Your Research] AI Agent Behavior Study
  Status: Internal research
  Risk: May be contradicted by external research
  Action: Monitor for competing research; update if findings differ

═══════════════════════════════════════════════════

RELATED CONTENT & DEPENDENCIES

This piece is referenced by:
  • Blog post: "AI Shopping Agents: What They Look For"
  • Pillar guide: "AEO Framework"

Update dependency: If major claims change, update related posts to maintain consistency

═══════════════════════════════════════════════════

PERFORMANCE METRICS & DECAY INDICATORS

Track these metrics to trigger refresh:
  □ Traffic: If monthly traffic declines >30%, investigate
  □ Bounce rate: If >70%, may indicate outdated content
  □ Time on page: If <90 seconds, content may not be resonating
  □ Search rankings: If rankings drop >20%, investigate freshness
  □ Comments/feedback: If readers flag outdated info, prioritize refresh

Target metrics (baseline):
  Traffic: [X visits/month]
  Bounce rate: [X%]
  Time on page: [X minutes]
  Avg. ranking position: [X]

Review these metrics: Quarterly (every 3 months)

═══════════════════════════════════════════════════

REFRESH DECISION MATRIX

When a review is due, ask:

1. Are any claims outdated?
   YES → Proceed to refresh
   NO → Extend next review date by 3 months

2. Has competitive content been published?
   YES → Consider adding comparison or new insights
   NO → No action needed

3. Has performance declined?
   YES → Investigate and refresh if needed
   NO → Extend next review date

4. Is research available that contradicts claims?
   YES → Update with new research; cite it
   NO → Confirm claims remain valid

5. Have source links changed or broken?
   YES → Update links immediately
   NO → Continue

═══════════════════════════════════════════════════

REVISION HISTORY

Date        Change Type       What Changed        Version
[blank]     Initial publish   Full content        v1 (published)
[blank]     [pending]         [pending]           v2 (TBD)

═══════════════════════════════════════════════════
```

* Maintenance Log (one entry per volatile section):

```
MAINTENANCE LOG ENTRY TEMPLATE

Title: [Section name]
Claim: [Specific claim being monitored]
Volatility: High / Medium / Low
Published Version: v1
Current Version: v1
First Review: [Date]
Last Reviewed: [Date, blank if not yet]
Last Updated: [Date, blank if not yet]
Status: Active / Scheduled for Review / Needs Update
Next Review: [Date]
Refresh Trigger: [What would cause a refresh?]
Notes: [Any context about why this claim needs monitoring]
```

### Human Checkpoint

Review the maintenance schedule:

* Do review dates make sense?
* Are volatile sections identified correctly?
* Are refresh triggers clear and actionable?
* Do related content dependencies make sense?
* Is the performance monitoring plan realistic?

Adjustments:

* "Move Review 1 from May to April; prefer earlier check"
* "Add a trigger for [event]"
* "Remove Review 3; content is evergreen"
* "Add [section] to volatile sections list"

### Success Criteria

* All volatile sections are identified
* Review dates are assigned
* Refresh triggers are clear and testable
* Source dependencies are documented
* Related content relationships are noted
* Performance metrics are defined
* Maintenance log is in place and organized
* Schedule is realistic and sustainable
