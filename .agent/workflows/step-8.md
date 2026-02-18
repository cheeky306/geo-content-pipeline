---
description:  Get explicit human approval to publish. Summarizes changes across versions, highlights risks, requests binary decision: APPROVE or REQUEST CHANGES.
---

# STEP 8 — Human Approval & Release

## Overview

Human Approval and Release is the explicit decision point before publication. This step creates accountability and a clear handoff from creation to publishing. The copilot summarizes changes across all draft versions, highlights risk areas, and asks for explicit approval to publish.

This is not another review. The content has already passed QA (Step 6) and been formatted for publishing (Step 7). This step is purely about human judgment: does the leader approve this piece for publication? Are there any last-minute concerns? Is the timing right?

The copilot produces a release summary showing what changed from v1 to v3, what was fixed in QA, and what risks remain. The human then makes a binary decision: APPROVE or REQUEST CHANGES.

Expect this step to take 5-10 minutes. It is a formality if earlier steps were thorough, but it is a necessary formality.

## Workflow

### Inputs (Human)

Finalized assets from Steps 6 and 7:

* QA PASS verdict
* Final draft v3 (optimized, sourced, and QA-approved)
* Ghost Publishing Card (complete and ready)
* All revisions applied
* No outstanding issues

Also recommended:

* Change log across versions (v1 → v2 → v3)
* Risk assessment summary
* Success criteria from Step 1

### Copilot Actions

1. Summarize changes across versions:
   * Compare v1 (raw draft) to v2 (sourced) to v3 (optimized)
   * Highlight major changes:
     * Sections rewritten for clarity
     * Sources integrated
     * Optimization applied (paragraph breaks, chunking, etc.)
     * QA fixes applied
   * Produce a version summary document
   * Example summary:

   ```text
   DRAFT EVOLUTION SUMMARY

   v1 → v2 (Evidence & Citation Pass):
   • Added 8 inline citations to existing claims
   • Marked 3 claims as [Needs source]
   • Created Citation TODO list
   • Added Sources section with 5 references
   • No structural changes; same word count

   v2 → v3 (Structural & GEO Optimization):
   • Broke 5 paragraphs into shorter chunks (paragraph length limit)
   • Rewrote 3 opening sentences for directness
   • Added H3 "Common Pitfalls" subheading
   • Optimized checklist from 8 items to 6
   • Word count: 1840 → 1765 words (within target)
   
   Editorial QA (Step 6):
   • Fixed 2 tag inconsistencies
   • Resolved 1 broken internal link
   • No content changes required; PASS on first review
   ```

2. Identify risk areas:
   * List any claims that required source verification
   * Flag any sections relying on external data (may need refresh)
   * Note any competitive overlaps identified
   * Identify any assumptions that may become outdated
   * Example risks:

   ```text
   RISK ASSESSMENT

   Low Risk:
   • Most claims are sourced and evergreen
   • No critical dependencies on external APIs

   Medium Risk:
   • Statistics on "AI adoption in ecommerce" are from 2024 data
     Action: Flag for refresh in Q2 2025 if new data is published
   • References to "current WooCommerce market share"
     Action: Refresh annually or upon major WooCommerce release

   High Risk:
   • None identified
   ```

3. Confirm success criteria alignment:
   * Verify the piece addresses the original goal (from Step 1)
   * Confirm reader can achieve success criteria
   * Example: "After reading, readers can identify 5+ product description elements AI agents prioritize" → piece delivers this

4. Produce release summary:
   * What is this piece about (one sentence)?
   * Who is it for?
   * What should readers do with it?
   * What are the key claims / differentiators?
   * Why is this piece being published now?
   * Example release summary:

   ```text
   RELEASE SUMMARY

   Title: How to Write Product Descriptions AI Agents Can Parse

   Purpose: Help WooCommerce store owners optimize product descriptions for AI-powered search visibility

   Unique Angle: Step-by-step, practical guide focused on AI agent behavior rather than generic SEO

   Key Claims:
   • AI agents prioritize structured data (specifications, attributes)
   • Description length 100–200 words is optimal for parsing
   • Active voice improves agent comprehension by 15%

   Why Now: AI-powered search is growing 3x faster than traditional search; merchants need practical guidance

   Expected Audience Outcome: Readers implement 3–5 optimization techniques in their store descriptions
   ```

5. Compile final metrics:
   * Word count
   * Reading time
   * Number of sections
   * Number of citations
   * Number of internal links
   * SEO stats (keyword density, readability score, etc., if available)

6. Produce final sign-off template:
   * Clear approval request
   * List of any outstanding issues (should be none)
   * Next steps after approval
   * Example:

   ```text
   ═══════════════════════════════════════════════════
   READY FOR PUBLICATION
   ═══════════════════════════════════════════════════

   Draft: FINAL v3 (QA PASS)
   Status: Ready for Human Approval

   Outstanding Issues: NONE

   Pre-Publish Verification:
   ✓ Structure complete and verified
   ✓ All sources integrated and cited
   ✓ GEO optimization applied
   ✓ Editorial QA passed
   ✓ Publishing card generated
   ✓ No content changes required

   DECISION REQUIRED:

   [ ] APPROVE — Publish immediately
   [ ] APPROVE WITH NOTES — Publish, but note [specific concern]
   [ ] REQUEST CHANGES — Return to [specific step] for adjustment

   APPROVAL AUTHORITY:
   Approved by: [Name/Role]
   Date: [Date]
   ```

### Human Checkpoint

Human explicitly approves or requests changes:

A) APPROVE — Publish immediately

* Human confirms:
  * Piece aligns with brand and strategy
  * All claims are credible
  * Timeline for publication is right
  * No last-minute concerns

* Explicit statement: "I approve this piece for publication."

* Proceed to Step 9 (Post-Publish Verification) immediately

B) APPROVE WITH NOTES — Publish, but flag something

* Human approves publication but includes notes:
  * "Publish, but add a refresh reminder for Q2 2025"
  * "Publish, but monitor competitive response"
  * "Publish, but schedule follow-up post on [topic]"

* Notes are logged for post-publication follow-up
* Proceed to Step 9 with notes attached

C) REQUEST CHANGES — Return for adjustment

* Human specifies what needs to change:
  * "Rewrite the Common Mistakes section; feels generic"
  * "Get a better source for the 15% claim"
  * "Delay publication until [date]"
  * "Consolidate FAQs; there's redundancy"

* Copilot returns to appropriate step (3, 4, 5, or 6) for changes
* After changes, loop back to Step 6 (Editorial QA) before re-submitting for approval

### Success Criteria

* Human has reviewed release summary and change log
* All QA items are confirmed PASS
* Risk assessment is understood
* Success criteria alignment is confirmed
* Publishing card is ready
* Explicit approval decision is made

### Escalation Paths

If human requests changes:

* Minor changes (copy tweaks, single section) → Copilot revises and re-runs QA (Step 6)
* Structural changes (reorder, add section) → Return to Step 2 or 3
* Source changes (better sources) → Return to Step 4
* Optimization issues (readability, chunking) → Return to Step 5

If changes require re-running QA, the revised draft must pass QA again (Step 6) before re-submission for approval.

### Common Approval Scenarios

#### Scenario A: Clean Approval

```text
HUMAN APPROVAL

Status: APPROVED

"This piece is excellent. The angle is fresh, sources are solid,
and it delivers value to WooCommerce store owners.
Publish immediately."

→ Proceed to Step 9
```

#### Scenario B: Conditional Approval

```text
HUMAN APPROVAL

Status: APPROVED WITH NOTES

"Publish this. One note: The statistic about AI adoption
is from 2024. Schedule a refresh for Q2 2025 when new
data is available. Great work."

→ Proceed to Step 9; refresh flagged in maintenance schedule
```

#### Scenario C: Changes Required

```text
HUMAN APPROVAL

Status: CHANGES REQUESTED

"The FAQ section feels repetitive. Consolidate similar questions
and shorten answers. Also, find a better source for the
'15% improvement' claim if possible.

Return to Step 4 for better source, then Step 6 for QA."

→ Copilot returns to Step 4 for sources
→ Re-runs Step 6 (Editorial QA)
→ Returns to Step 8 for re-approval
```

### Approval Authority

Establish who has authority to approve:

* Editorial Lead (final decision)
* Content Director (final decision)
* Brand Manager (if brand implications)
* SME (subject matter expert, for accuracy)

Multiple sign-offs may be required depending on content type and risk level.

### Documentation

Log approval for audit trail:

* Who approved
* Date and time
* Any notes or conditions
* Any risks or dependencies flagged
* Publish date (scheduled or immediate)

---

## Next Step

Once approval is granted, proceed to **STEP 9 — Post-Publish Verification**.
