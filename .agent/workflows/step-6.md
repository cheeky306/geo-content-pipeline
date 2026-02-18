---
description: Quality assurance gate before publishing. Validates structure, taxonomy, citations, links, consistency, tone. PASS/FAIL verdict with required fixes.
---

# STEP 6 — Editorial QA

## Overview

Editorial QA is the quality gate before publishing. The copilot runs a comprehensive checklist covering structure, taxonomy, sources, tone, logic, and compliance. The output is PASS/FAIL with explicit fixes required for any failures.

This is the moment where errors are caught before they go live. A missing tag, a broken link, a repetitive section, or a logic gap can damage credibility. Editorial QA prevents those mistakes from reaching production.

The checklist is objective: structure is complete, tags are correct, no paragraphs exceed limits, sources are cited, internal links work, terminology is consistent. These are measurable criteria, not subjective judgments. A piece either passes or it doesn't.

By the end of this step, the copilot has produced a final PASS/FAIL report. If FAIL, the exact fixes required are listed. If PASS, the piece is ready for Step 7 (publishing card generation) and Step 8 (human approval).

Expect this step to take 10-15 minutes. Most pieces pass on first run if earlier steps were thorough.

## Workflow

### Inputs (Human)

Approved draft v3 from Step 5:

* Optimized, structured Markdown
* All sections complete
* Sources integrated
* Tables and lists finalized
* Citations in place

Also required from earlier steps:

* Content type (Blog or Guide)
* Pillar assignment
* Success criteria (from Step 1)
* Required components checklist (from Step 2)

### Copilot Actions

1. Structural validation:
   * Verify all H2 sections are present (per outline from Step 2)
   * Verify all required H3 subsections are present
   * Confirm no headings are skipped (no H2 → H4 jumps)
   * Verify TL;DR section exists and has 3–6 bullets
   * Confirm Quick Answer exists and is 2–4 sentences
   * Verify at least one table or checklist is present
   * Confirm FAQs section exists (for Blog) with 3–6 questions
   * Verify Common Mistakes section exists (for Blog)
   * Confirm Sources section exists with numbered list
   * Verify pillar link placeholder is present
   * Check word count against target (within 10% acceptable)

2. Paragraph length audit:
   * Scan all body paragraphs
   * Flag any paragraph >4 lines
   * Report paragraph distribution
   * Test: does the draft pass paragraph length requirement?

3. Tag and taxonomy validation:
   * Confirm exactly one content type tag ([#blog] or [#guide])
   * Confirm exactly one topic tag (geo/aeo/ai-seo/ai-citations/eeat-ai)
   * Confirm exactly one pillar tag ([#p-geo], etc.)
   * Verify tags are formatted correctly
   * Check: are all required tags present and only one of each type?

4. Citation and source validation:
   * Count all inline citations
   * Verify every statistic has a citation
   * Verify every best practice claim is cited or marked [Verified]
   * Confirm no [Needs source] labels remain
   * Verify Sources section is numbered and formatted correctly
   * Check: is every claim either cited or explicitly labeled?

5. Internal linking validation:
   * Verify pillar link placeholder is present
   * Check format: "/resources/guides/[pillar-slug]/"
   * Verify any other internal links are present and formatted
   * Confirm links are not broken (URLs are valid)
   * Check: are all internal links correct and discoverable?

6. Consistency audit:
   * Scan for terminology consistency (same term used same way throughout)
   * Flag terminology variations (e.g., "AI agent" vs "intelligent agent")
   * Check for consistent voice and tone
   * Verify consistent formatting in tables and lists
   * Verify consistent citation format throughout
   * Report: are there terminology or tone inconsistencies?

7. Repetition detection:
   * Scan for repeated claims or ideas across sections
   * Identify sections that restate the same concept
   * Flag unnecessary redundancy
   * Note: some repetition is acceptable (key concepts restated for clarity)
   * Report: what is repeated, and is it necessary?

8. Logic and flow validation:
   * Verify outline is followed exactly
   * Check reader journey: does content build logically?
   * Verify transitions between sections
   * Confirm each section advances toward the goal (from Step 1)
   * Test: does the piece answer the original intent clearly?

9. GEO compliance:
   * Verify answer-first sentences in each H2/H3
   * Confirm chunking every 200–400 words
   * Verify tables and lists are extraction-ready
   * Check: is content optimized for search extraction?

10. Tone and voice:
    * Verify tone matches approved voice (practitioner, formal, etc.)
    * Check for brand voice consistency
    * Flag any jarring tone shifts
    * Verify no fluff language ("In today's world…", "It goes without saying…")
    * Report: is tone consistent and brand-aligned?

### Outputs

The copilot produces:

* Editorial QA Report with PASS/FAIL verdict
* Detailed checklist results for each category:
  * Structural completeness: ✓ PASS or ✗ FAIL (with missing elements)
  * Paragraph length: ✓ PASS or ✗ FAIL (with count of violations)
  * Tags and taxonomy: ✓ PASS or ✗ FAIL (with missing/incorrect tags)
  * Citations and sources: ✓ PASS or ✗ FAIL (with unsourced claims)
  * Internal links: ✓ PASS or ✗ FAIL (with broken or missing links)
  * Consistency: ✓ PASS or ✗ FAIL (with inconsistencies flagged)
  * Repetition: ✓ PASS or ✗ FAIL (with repeated concepts noted)
  * Logic and flow: ✓ PASS or ✗ FAIL (with logic gaps noted)
  * GEO compliance: ✓ PASS or ✗ FAIL (with extraction issues noted)
  * Tone and voice: ✓ PASS or ✗ FAIL (with tone issues noted)

* Required fixes (if FAIL):
  * Specific fixes needed for each failure
  * Priority level (critical, high, medium, low)
  * Locations of issues (section, line)

* Final verdict:
  * ✓ READY FOR PUBLICATION
  * ✗ REQUIRES FIXES (with fix list)

### Human Checkpoint

Review the QA report:

A) If PASS:

* Confirm all items are acceptable
* Acknowledge readiness for Step 7

B) If FAIL:

* Review required fixes
* Assign fixes to copilot OR apply manually
* Copilot re-runs QA on fixed draft
* Iterate until PASS

Example FAIL scenario:

```
EDITORIAL QA REPORT — DRAFT v3

FAIL: Paragraph length
Issue: 3 paragraphs exceed 4 lines
Locations: H2 "Section 2", line 45 (5 lines); H2 "Section 4", line 72 (6 lines); FAQs, line 98 (5 lines)
Fix: Break these paragraphs into shorter ones, one idea per paragraph.

FAIL: Tags and taxonomy
Issue: Missing pillar tag
Location: Meta section
Fix: Add [#p-aeo] tag (or correct pillar)

PASS: Citations and sources
All claims are cited or labeled. No issues.

FAIL: Tone and voice
Issue: One section uses passive voice; rest is active
Location: H2 "Best Practices", line 55
Fix: Rewrite to active voice for consistency.

VERDICT: ✗ REQUIRES FIXES
PRIORITY: 3 fixes required before publication (2 high, 1 medium)
```

### Success Criteria

* All structural elements are present and complete
* All paragraphs are ≤4 lines
* All tags are correct, complete, and consistent
* All claims are cited or explicitly labeled
* All internal links are correct and functional
* Terminology is consistent throughout
* Unnecessary repetition is flagged and justified
* Logic and reader journey are clear
* Content is GEO-optimized and extraction-ready
* Tone and voice are consistent and brand-aligned
* Word count is within 10% of target

### QA Thresholds

* ✓ PASS: All checks pass OR only minor issues that don't affect credibility
* ✗ FAIL: Any critical issue (missing section, unsourced claim, broken tag, broken link)

Critical issues:

* Missing required section
* Unsourced factual claim
* Incorrect or missing tags
* Broken internal or external links
* Major logic gap
* Significant tone inconsistency

### When to Stop and Escalate

If QA reveals:

* Fundamental structure problems → return to Step 2 (outline) to restructure
* Major content gaps → return to Step 3 (draft) to rewrite affected sections
* Unresolvable repetition → return to Step 2 or 3 to clarify outline and purpose
* Irreconcilable tone issues → clarify brand voice with human before proceeding

If more than 5 critical fixes are required, stop and escalate to human for decision on whether to continue or restart.

---

## Next Step

Once QA is PASS and all fixes are applied, proceed to **STEP 7 — Ghost Publishing Card Generation**. call/step-7