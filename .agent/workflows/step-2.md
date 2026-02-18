---
description: Generate outline and validate angle before drafting prose. Creates title options, H2/H3 structure, section intent map. Approves skeleton before filling in content.
---

# STEP 2 — Outline & Angle Validation

## Overview

Outline and Angle Validation ensures the structure and positioning are correct before the copilot writes prose. This step prevents the most common waste: writing a well-crafted section that needs to be deleted because it doesn't serve the goal or contradicts the angle.

During this step, the copilot generates three title options, a recommended slug, and a complete H2/H3 outline mapped to the reader's journey and the original intent from Step 1. It also verifies that all required components (TL;DR, FAQs, sources, etc.) are included in the structure before writing begins.

This is where the editorial blueprint is finalized. Every section has a purpose. Every heading answers a specific question the reader has. There is no filler, no tangential sections, and no repetition.

You approve the structure at this stage, not after the draft is written. This is the checkpoint where revision is cheapest and most effective.

By the end of this step, the copilot has a locked structure. It will fill in the content in Step 3, but the skeleton is approved and immovable. This discipline prevents scope creep and keeps the output focused.

Expect this step to take 15-20 minutes including back-and-forth revisions. It is time well spent.

## Workflow

### Inputs (Human)

Approved framing from Step 1:

* Refined topic statement
* Reader profile
* Thesis statement
* Success criteria
* Content type (Blog or Guide)
* Pillar assignment
* Preferred length

### Copilot Actions

1. Generate three distinct title options:
   * Title A: Direct, benefit-driven (e.g., "How to Write Product Descriptions AI Agents Can Parse")
   * Title B: Question-based (e.g., "What Do AI Agents Look for in Product Descriptions?")
   * Title C: Frameworks or tools-based (e.g., "The Product Description Framework for AI Readiness")

2. Recommend one slug based on the chosen title
   * Slug is lowercase, hyphenated, no dates
   * Example: `how-to-write-product-descriptions-ai-agents`

3. Create a complete H2/H3 outline aligned to:
   * Reader's knowledge journey (beginner → intermediate → expert)
   * Thesis statement progression
   * Content type requirements (Blog or Guide minimum standards)

4. Map each section to reader intent:
   * What question does this section answer?
   * Why does the reader need this before the next section?
   * Does this section move toward the goal?

5. Insert all required components:
   * TL;DR bullets (3–6 for Blog, varies for Guide)
   * Quick Answer or definition
   * Body sections (H2/H3)
   * At least one table, checklist, or framework
   * Common mistakes or pitfalls (for Blog)
   * FAQs (3–6 for Blog)
   * Sources list section
   * For Blog: Pillar link placeholder (e.g., "/resources/guides/[pillar-slug]/")

6. Cross-check against pillar strategy:
   * Is this content aligned with the broader pillar topic?
   * Will this support other content in the same pillar?

7. Identify and flag any potential fluff sections:
   * Intro that doesn't serve the reader
   * Tangential sections
   * Repetition risk

### Outputs

The copilot produces:

* Title Options (3 distinct, ranked by strength)
* Recommended Slug (1–2 alternatives if titles diverge)
* Complete H2/H3 Outline with word count estimates per section
* Section Intent Map (what question each section answers)
* Required Components Checklist (all mandatory elements included)
* Internal Linking Placeholders (e.g., "Link to [Pillar Post] here")
* GEO/AEO Optimization Notes (where to strengthen for extraction)
* Potential Revision Areas (flagged weak or risky sections)

### Human Checkpoint

Review and approve:

* Best title: Which resonates with your audience? Which aligns with the goal?
* Slug: Is it memorable and SEO-aligned?
* Overall angle: Does the outline deliver on the thesis?
* Section order: Is the reader journey logical?
* Missing sections: Is there anything the outline should include?
* Fluff sections: Are there any sections you'd remove?
* Required components: Are all mandatory elements present?
* Length: Does the outline fit your target word count?

Revisions happen here through explicit feedback:

* "Move FAQ section earlier"
* "Add a section on common mistakes before the checklist"
* "Title B is stronger; use that angle"
* "This intro section feels like fluff; can we jump straight to Quick Answer?"

### Success Criteria

* All three titles are distinct and defensible
* Outline has clear logic and narrative flow
* Every section serves reader intent
* All required components are present
* No filler or tangential sections
* Outline fits target word count
* Slug is accurate and memorable
* Internal linking placeholders are clear

### Common Revisions at This Stage

* Order changed → sections reordered to improve reader journey
* Section removed → identified filler is cut from outline
* Section added → important question not covered is inserted
* Title swapped → different title option chosen
* Angle refined → outline adjusted to strengthen positioning

### When to Stop and Escalate

If the outline reveals that:

* Topic is too broad to cover in target length → narrow scope and restart Step 2
* Required sources don't exist → raise to human; decide on "no-claims mode"
* Angle is weak or generic → return to Step 1 to refine framing
* Reader goal is unclear → return to Step 1 for clarity

---

## Next Step

Once outline and angle are approved, proceed to **STEP 3 — Draft Generation (v1)**. call/step-3