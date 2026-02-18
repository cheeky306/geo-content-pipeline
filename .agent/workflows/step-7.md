---
description: Generate publishing specification card for Ghost CMS. Compiles metadata, tags, excerpt, feature image guidance, checklists. Ready for copy/paste publishing.
---

# STEP 7 — Ghost Publishing Card Generation

## Overview

Ghost Publishing Card Generation creates a compact, machine-readable publishing specification that makes going live fast and mistake-proof. The publishing card is a single reference containing all metadata, tags, settings, and publishing instructions in one place.

Ghost is your publishing platform (or this process adapts to your CMS). The card ensures that whoever publishes the piece uses consistent metadata, correct tags, proper formatting, and follows the right pre-and-post-publish steps. It removes ambiguity and prevents common publishing errors.

This step takes the final approved draft from Step 6 and translates it into actionable publishing instructions. The card is a template that can be copied directly into Ghost (or your CMS) with no guessing or interpretation required.

Expect this step to take 10-15 minutes. Most of the data has been defined in earlier steps; this step just compiles it into a clean format.

## Workflow

### Inputs (Human)

Approved final draft (v3) from Step 6:

* QA PASS verdict confirmed
* All fixes applied
* Sources finalized
* Tags correct and complete
* Metadata ready

Also required:

* Content type (Blog or Guide)
* Pillar assignment
* Slug
* Title
* Internal linking placeholders resolved
* Feature image guidance

### Copilot Actions

1. Extract title:
   * Pull approved title from draft
   * Verify title is in H1 format in Markdown
   * Format for Ghost: remove Markdown syntax (#)
   * Example: "# How to Write Product Descriptions AI Agents Can Parse" → Title: "How to Write Product Descriptions AI Agents Can Parse"

2. Extract and format slug:
   * Verify slug is lowercase, hyphenated, no dates
   * Example: "how-to-write-product-descriptions-ai-agents"
   * Confirm slug uniqueness (doesn't duplicate existing posts)
   * Provide alternate slug option if conflict exists

3. Create excerpt (meta description):
   * Generate 155–160 characters (Google snippet limit)
   * Use first 1–2 sentences of Quick Answer as base
   * Include keyword naturally
   * Make compelling for CTR
   * Example: "Learn how to structure product descriptions so AI agents extract key information accurately, improving visibility in AI-powered search."

4. Compile tags:
   * Confirm exactly three tags:
     * One content type tag ([#blog] or [#guide])
     * One topic tag (geo, aeo, ai-seo, ai-citations, eeat-ai)
     * One pillar tag ([#p-geo], [#p-aeo], etc.)
   * Format for Ghost: comma-separated, no brackets
   * Example: "#blog, aeo, #p-aeo"

5. Compile metadata:
   * Author name
   * Publish date (or recommended publish date)
   * Custom fields (if applicable to your CMS)
   * Language: English (or specify)
   * Status: Draft (ready to publish)

6. Create feature image guidance:
   * Describe ideal image dimensions (e.g., 1200×675px for social)
   * Describe image content: what should it show?
   * Recommend style (photography, illustration, diagram)
   * Provide alt text for accessibility
   * Example: "Image: A split-screen showing a product description on the left (with annotations highlighting key elements) and an AI agent interface on the right (showing extracted data). Style: clean, professional, minimal. Dimensions: 1200×675px. Alt text: 'AI agent extracting product description data.'"

7. Create canonical URL structure:
   * For Blog: /blog/[slug]/
   * For Guide: /resources/guides/[pillar-slug]/[slug]/
   * Provide full URL
   * Example: /blog/how-to-write-product-descriptions-ai-agents/

8. Create internal linking checklist:
   * Identify all internal links in the draft
   * Verify they resolve to correct URLs
   * Flag any placeholder links needing resolution
   * List all internal links separately for publishing team

9. Create pre-publish checklist:
   * Final draft review: read through once more for typos/errors
   * Verify all links are live (no 404s)
   * Confirm all inline citations link to sources
   * Preview in Ghost: render and check formatting
   * Test on mobile: ensure readability on small screens
   * Verify feature image is optimized and formatted

10. Create post-publish verification checklist:
    * Verify URL is live and accessible
    * Test all internal links
    * Check TOC generation (if auto-generated)
    * Verify TL;DR section rendered correctly
    * Check social media card preview (title + image)
    * Test in AI Overview simulation (optional)
    * Verify Google Search Console pickup (24 hours)

### Outputs

The copilot produces:

* Ghost Publishing Card (formatted for easy copy/paste):

```
═══════════════════════════════════════════════════
GHOST PUBLISHING CARD
═══════════════════════════════════════════════════

BASIC METADATA

Title: [Approved Title]
Slug: [approved-slug]
Excerpt (meta description): [155-160 char excerpt]
Author: [Author Name]
Publish Date: [Date or "Immediate"]
Status: Ready to Publish

TAGS & TAXONOMY

Content Type: [#blog or #guide]
Topic: [geo/aeo/ai-seo/ai-citations/eeat-ai]
Pillar: [#p-geo, #p-aeo, etc.]

Tags (for Ghost): [paste comma-separated]

CANONICAL & ROUTING

Canonical URL: [/blog/slug/ or /resources/guides/pillar/slug/]
Expected Route: [full URL path]

FEATURE IMAGE

Recommended Dimensions: 1200×675px
Content Description: [What should image show]
Style: [Photography/illustration/diagram]
Alt Text: [Accessibility description]
[Image attached or to be provided by design team]

SOCIAL METADATA

Social Title: [Title, optimized if needed]
Social Description: [Excerpt]
Social Image: [Feature image or alternate]

INTERNAL LINKS

Link 1: [Anchor text] → [URL]
Link 2: [Anchor text] → [URL]
[... all internal links listed]

WORD COUNT & STATS

Total Words: [X words]
Reading Time: [X min read]
Number of Sections: [X H2 sections]
Number of Sources: [X citations]

═══════════════════════════════════════════════════

PRE-PUBLISH CHECKLIST

□ Final draft reviewed for typos/errors
□ All inline citations link to live sources
□ All internal links verified (no 404s expected)
□ Markdown previewed in Ghost
□ Mobile rendering checked
□ Feature image is optimized and final
□ All placeholder links resolved
□ Tags confirmed in Ghost system

═══════════════════════════════════════════════════

POST-PUBLISH VERIFICATION

□ URL is live and accessible
□ All internal links working (404 test)
□ TOC or section navigation rendering correctly
□ TL;DR bullets extracted/highlighted properly
□ Social card preview displays title + image correctly
□ Featured image displays at full resolution
□ Mobile layout is readable
□ Google Search Console shows indexing (24 hours)
□ Compare live URL to QA pass draft

═══════════════════════════════════════════════════

MAINTENANCE SCHEDULE

Review Date: [3 months from publish, or specific date]
Volatile Sections: [Any sections with dates/stats that may change]
Source Dependencies: [Any claims dependent on external sources]
Refresh Trigger: [When to revisit; e.g., "If X changes"]

═══════════════════════════════════════════════════
```

### Human Checkpoint

Review the publishing card for:

* Title and slug are correct
* Tags are accurate and complete
* Excerpt is compelling and keyword-rich
* Feature image guidance is clear
* Canonical URL is correct
* All checklists are actionable
* No placeholder content remains

Make any final adjustments to excerpt, tags, or feature image guidance.

### Success Criteria

* All metadata is complete and correct
* Tags follow taxonomy rules (exactly one of each type)
* Slug is unique and SEO-appropriate
* Excerpt is under 160 characters
* Feature image guidance is specific and actionable
* Checklists are detailed and actionable
* Card is ready for copy/paste into publishing platform

### Common Issues at This Stage

* Slug conflicts with existing post → provide alternate slug
* Excerpt is too long → trim to 155–160 characters
* Tags are incomplete → add missing pillar or topic tag
* Feature image guidance is vague → specify exactly what image should show
* Internal links are incomplete → resolve all placeholders before creating card

### Publishing Card Distribution

Once approved, the card is distributed to:

* Publishing team (who will enter metadata into Ghost)
* Content manager (who will verify pre-publish checklist)
* QA team (who will verify post-publish checklist)
* Analytics team (tracking performance against success criteria)
* Social media team (for scheduled promotion)

### Customization for Different CMS

This workflow assumes Ghost, but adapts to:

* WordPress: Tags → Categories, Custom Fields → Advanced Custom Fields
* Medium: Tags → Topics, Metadata → Publication settings
* Substack: Tags → Topics, Metadata → Email settings
* Webflow: Tags → Collections, Metadata → SEO panel

Consult your CMS documentation and customize the card accordingly.

---

## Next Step

Once publishing card is approved, proceed to **STEP 8 — Human Approval & Release**. call/step-8