---
description: Integrate sources and cite all factual claims. Maps claims to sources, inserts citations, labels unsourced claims. Produces Citation TODO list for verification.
---

# STEP 4 — Evidence & Citation Pass

## Overview

Evidence and Citation Pass transforms the draft from content into authoritative, verifiable knowledge. This step integrates sources, adds citations, labels unsupported claims, and produces a clear record of what is backed by evidence and what requires source verification.

The goal is credibility. Every factual claim should be traceable to a source or explicitly labeled as general knowledge, hypothesis, or opinion. This protects you from reputational risk and positions your content as authoritative rather than promotional.

The copilot extracts all factual claims from the draft, maps them to sources from your knowledge base or from provided sources, and inserts citations. Claims without sources are labeled with [Needs source], [Verified], or [Hypothesis] markers. A Citation TODO list is produced if sources are missing.

This step is where unsubstantiated claims are caught. By the end, you have a draft where every number, statistic, benchmark, or best practice is either cited or marked for verification.

Expect this step to take 30-45 minutes, especially if sources need to be provided or verified.

## Workflow

### Inputs (Human)

Approved draft v1 from Step 3:

* Complete Markdown with all sections
* Flagged revisions (if any) applied
* Internal knowledge base (from Step 0)

Optional:

* External sources (papers, links, data, case studies)
* Preferred citation format (if different from standard)
* Confidence level for claims (which claims are definitely true, which need verification)

### Copilot Actions

1. Extract all factual claims from the draft:
   * Statistics and benchmarks
   * Best practices
   * Technical specifications
   * Recommendations
   * Rankings or comparative statements
   * Historical claims or precedents

2. Categorize each claim:
   * Clearly general knowledge (e.g., "WooCommerce is a WordPress plugin") → Mark [Verified]
   * Specific fact or statistic → Flag [Needs source] if unsourced
   * Hypothesis or opinion → Label [Hypothesis] if included

3. Match claims to available sources:
   * Cross-reference with knowledge base (Step 0)
   * Match against human-provided sources
   * Note source credibility (primary, secondary, grey literature)

4. For sourced claims, insert citations:
   * Inline citations using standard format: Author/Org, Year (with link if available)
   * Direct quotes (if used) are under 25 words, exact, and attributed
   * Example: "according to Google Search Console data (2024)"

5. For unsourced claims:
   * Mark with [Needs source] label
   * Flag the claim and move to TODO list
   * Do not invent sources or guess at citations

6. Build Citation TODO list:
   * All flagged [Needs source] claims
   * Instructions for human to provide missing sources
   * Priority: high (core claims), medium (supporting claims), low (nice-to-have)

7. Create Sources section:
   * Numbered list format: 1. Author/Org — Title (Year)
   * Include URL or DOI if available
   * Order by first mention in text
   * Format: consistent and machine-readable

### Outputs

The copilot produces:

* Revised draft (v2) with:
  * Inline citations for all sourced claims
  * [Verified] markers for general knowledge
  * [Needs source] markers for unsourced claims
  * [Hypothesis] markers for opinion or speculation
  * Direct quotes (≤25 words) with attribution
  * Updated Sources section (numbered, formatted)

* Citation TODO list:
  * All unsourced claims requiring verification
  * Organized by priority and section
  * Clear instructions for sourcing each claim
  * Example: "H2 'Best Practices' — Claim: 'Product descriptions should be under 200 words.' [Needs source] — Find source or verify as hypothesis."

* Citation gaps report:
  * Summary of sourcing status
  * Percentage of claims cited
  * High-priority missing sources
  * Assessment of overall credibility

### Human Checkpoint

Review and act on:

* Citation TODO list: Provide missing sources or approve [Hypothesis] labels
* Sourced claims: Confirm citations are accurate and attributed correctly
* Direct quotes: Verify quote accuracy and word count
* Sources section: Confirm all sources are correctly formatted and relevant

For each item in the TODO list, human either:

* A) Provides a credible source → copilot integrates it
* B) Approves the [Hypothesis] or [Verified] label → claim stays as-is
* C) Removes the claim as unverifiable → section is revised without the claim

Example human response:

```
TODO Item 1: "Product descriptions should be under 200 words."
RESPONSE: Remove this claim. Replace with "Product descriptions should be scannable, typically 100–300 words depending on product complexity."
Label as [Hypothesis] pending research.
```

### Success Criteria

* All factual claims are either sourced, marked [Verified], or labeled [Needs source]
* No unsourced statistics appear without [Needs source] label
* Direct quotes are under 25 words and exactly attributed
* Sources section is complete and formatted correctly
* Citation TODO list is comprehensive and actionable
* No invented or speculative citations exist
* Draft can pass editorial review without source challenges

### Common Issues at This Stage

* Quote is too long → trim to under 25 words or paraphrase
* Source is not credible → request better source or mark [Hypothesis]
* Claim is vague → clarify the specific claim before sourcing
* Multiple sources for one claim → note primary source and add secondary sources
* Source is behind paywall → note accessibility; decide whether to use
* Statistic is outdated → flag for human decision (use, update, or remove)

### Citation Standards (By Claim Type)

**Statistics, benchmarks, rankings:**

Format: "X [statistic] according to [Author/Org] ([Year])."
Example: "60% of ecommerce stores use WooCommerce according to W3Techs (2024)."
Include link if available.

**Best practices, recommendations:**

Format: "[Org/Author] recommends [practice] ([Year])."
Example: "Google Search Console recommends keyword-driven page titles (2023)."

**Technical specifications:**

Format: "[Product/Platform] [specification] as of [date/version]."
Example: "WooCommerce supports custom product fields via Advanced Custom Fields as of ACF v6.0 (2023)."

**Research findings:**

Format: "A [Study/Report] found that [finding] ([Author], [Year])."
Example: "A study by Content Marketing Institute found that data-driven content performs 3x better than average (2023)."

**Platform policies:**

Format: "According to [Platform] policy ([Year]), [policy statement]."
Example: "According to OpenAI usage policy (2024), AI training on user content is opt-in."

### Revision Loop

If human feedback requires sourcing changes:

1. Copilot integrates new sources
2. Updates draft with new citations
3. Removes unsourced claims or relabels them
4. Updates Sources section
5. Updates Citation TODO list
6. Human reviews revised citations

Limit revision loop to 1–2 rounds. If more than 50% of claims require sources and sources are unavailable, escalate to human for decision on proceeding.

### When to Stop and Escalate

If during this step:

* More than 50% of claims are unsourced and sources are unavailable → raise to human; decide on "no-claims mode" or halt
* A critical claim cannot be verified → halt until human clarifies
* Sources provided are not credible → flag and request better sources

---

## Next Step

Once sources are verified and TODO list is cleared, proceed to **STEP 5 — Structural & GEO Optimization**.