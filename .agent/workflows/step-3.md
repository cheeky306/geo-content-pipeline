---
description: Generate full Markdown draft using approved outline. Writes all sections, TL;DR, FAQs, tables, checklists. First complete draft ready for evidence review.
---

# STEP 3 — Draft Generation (v1)

## Overview

Draft Generation is where the approved outline becomes prose. The copilot fills in the structure with content, examples, explanations, and transitions using the knowledge base from Step 0 and adhering strictly to the structure approved in Step 2.

This step is mechanical in discipline: no deviations from the outline, no new sections, no skipped sections. The copilot writes to the outline as approved. If the outline says five subsections under H2 "How to Optimize Descriptions," then there are five subsections and no more.

The copilot prioritizes clarity and directness. Every section opens with a direct answer to the section's stated question. Paragraphs are short (4 lines or fewer). Examples are concrete and relevant. Tables and checklists support the text, not replace it.

This draft is not final. Expect it to need refinement in Steps 4, 5, and 6. The goal here is a complete first pass that covers all required content, uses the approved knowledge base, and creates a solid foundation for evidence review and optimization.

Expect this step to take 30-45 minutes depending on depth and length. The copilot will produce a complete Markdown file ready for review.

## Workflow

### Inputs (Human)

Approved assets from previous steps:

* Approved outline and section intent map (from Step 2)
* Topic statement, reader profile, thesis, and success criteria (from Step 1)
* Knowledge base (from Step 0)
* Content type (Blog or Guide)
* Pillar assignment
* Required components checklist
* Internal linking placeholders

Optional:

* Specific examples or case studies to include
* Known sources to prioritize
* Tone or voice preferences beyond standard

### Copilot Actions

1. Apply the approved template structure from Step 2
2. Generate TL;DR bullets (3–6):
   * Each bullet is 1 sentence, under 15 words
   * Bullets are scannable and actionable
   * Bullets are extracted from body content, not separate ideas

3. Write Quick Answer section:
   * 2–4 sentences
   * Directly answers the main thesis question
   * Assumes no prior knowledge
   * Sets up the deeper sections

4. Write all H2 sections:
   * Each section opens with a direct answer sentence that could stand alone
   * Body supports and elaborates on the answer
   * Use concrete examples from the knowledge base
   * Maintain consistent terminology from Step 0

5. Write all H3 subsections:
   * Same discipline: answer first, then explain
   * Subsections build on parent H2
   * Transitions are clear and logical

6. Integrate tables, checklists, or frameworks:
   * At least one required per Blog; at least one framework table per Guide
   * Tables are parsed and meaningful, not decorative
   * Checklists are actionable and specific
   * Frameworks reinforce the core thesis

7. Write Common Mistakes section (for Blogs):
   * 3–5 specific, actionable mistakes
   * Each mistake is a realistic error your reader might make
   * Each includes why it's a mistake and what to do instead

8. Write FAQs (3–6 for Blogs):
   * Questions are real questions your reader asks
   * Answers are concise (2–3 sentences)
   * FAQs do not repeat body content

9. Prepare Sources section:
   * List placeholder for sources (copilot will integrate them in Step 4)
   * Format: "Author/Org — Title (Year)" as per brand standards

10. Insert internal linking placeholders:
    * For Blog: "See full framework at /resources/guides/[pillar-slug]/"
    * Placeholder is exact and searchable

### Outputs

The copilot produces:

* Complete Markdown draft (v1) with:
  * Title and slug
  * Meta information (content type, pillar tags)
  * TL;DR section
  * Quick Answer
  * All H2/H3 sections with body copy
  * Tables/checklists
  * Common Mistakes (for Blog)
  * FAQs
  * Sources section (placeholder for citations)
  * Internal linking placeholders

* Word count report (actual vs. target)
* Section-by-section summary
* Quality indicators (readability, example density, answer-first ratio)

### Human Checkpoint

Read and review for:

* Generic language: Does any section feel like boilerplate or AI-generic content?
* Weak sections: Which sections need more depth or better examples?
* Incorrect assumptions: Are there any factual errors or misaligned claims?
* Missing depth: Are there sections that feel too shallow for the reader level?
* Tone drift: Does voice stay consistent throughout?
* Structure adherence: Does the draft follow the approved outline exactly?

Flag specific sections for revision, not the whole draft.

Example feedback:

* "H2 #3 feels generic. Add a concrete WooCommerce example here."
* "Quick Answer assumes too much knowledge. Simplify."
* "The FAQ on [topic] isn't answered clearly. Rewrite."
* "This checklist is too long. Cut it to 5 items."

### Success Criteria

* Draft covers all sections in approved outline
* TL;DR is scannable and extracted from body
* Quick Answer is clear and accessible
* Each H2 opens with a direct answer
* Examples are concrete and relevant
* Tables and checklists are actionable
* Word count is within 10% of target
* Tone is consistent
* No sections are skipped or duplicated
* Internal linking placeholders are present
* Sources section is ready for integration

### Common Issues at This Stage

* Overly long paragraphs → editor flag; will be fixed in Step 5
* Generic examples → request specific, relevant examples
* Missing section → copilot returns to outline; section was marked required
* Weak opening to section → request rewrite of opening sentence
* FAQ answers repeat body → flag for consolidation or removal

### Revision Loop

If human feedback requires significant rewrites:

1. Copilot revises only flagged sections
2. Rewrites are checked for structure and tone consistency
3. Human reviews revised sections
4. If acceptable, move to Step 4
5. If more revisions needed, repeat

Limit revision loop to 2 rounds at this stage. Major structural issues should have been caught in Step 2.

### When to Stop and Escalate

If during drafting the copilot encounters:

* A required claim with no source available → flag for human; proceed with [Needs source] label
* A knowledge gap (topic requires expertise not in knowledge base) → flag and wait for human guidance
* An ambiguity in the outline → raise to human before proceeding

---

## Next Step

Once draft is approved, proceed to **STEP 4 — Evidence & Citation Pass**. call/step-4