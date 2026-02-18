---
description: Verify live rendering after publication. Tests URLs, links, metadata, content rendering, tables, images, social preview. Confirms piece works as intended.
---

# STEP 9 — Post-Publish Verification

## Overview

Post-Publish Verification ensures that the piece rendered correctly after going live and that all the promises made in the publishing card are fulfilled. This is the quality check that happens after the hand-off to the publishing platform.

Many things can go wrong in publishing: links break, images don't load, formatting is corrupted, metadata is incorrect, or the URL doesn't match expectations. This step catches those errors within minutes of publication, when they're easiest to fix.

The verification checklist is objective: does the URL work? Do the links work? Does the content render as expected? Is the metadata correct? These are testable, measurable criteria.

Expect this step to take 15-20 minutes including any quick fixes. It is critical to the integrity of the published piece.

## Workflow

### Inputs (Human)

Published piece (just went live):

* URL is live
* Piece is accessible in your CMS
* Publishing card metadata is in place
* 5-10 minutes have passed since publication (allowing initial rendering)

Also required:

* Publishing card from Step 7 (reference document)
* Final Markdown draft from Step 6 (for comparison)
* Success criteria from Step 1 (for final assessment)

### Copilot Actions

1. Test URL accessibility:
   * Verify canonical URL is live and returns 200 status code
   * Example: https://yoursite.com/blog/product-descriptions-ai-agents/
   * Test on desktop and mobile browsers
   * Confirm page loads in under 3 seconds
   * Check: is the URL live and fast?

2. Verify metadata rendering:
   * Confirm page title appears in browser tab
   * Check meta description in Google Search result preview (if using simulation)
   * Verify featured image displays at expected dimensions
   * Confirm all tags are visible (if shown on page)
   * Check: is metadata displaying correctly?

3. Test all internal links:
   * List all internal links from the publishing card
   * Click each link and verify it works (200 status, no 404s)
   * Confirm links point to correct destination pages
   * Verify links open in correct window (same tab or new)
   * Example internal links to test:
     * Link to pillar guide: /resources/guides/aeo-framework/
     * Links to related posts (if any)
     * Links in FAQ or body sections
   * Check: do all internal links work?

4. Test external links:
   * Identify all outbound links (to citations, sources, tools)
   * Sample test 5–10 external links (especially citations)
   * Verify citations link to correct source pages
   * Confirm no links are broken or point to outdated sources
   * Check: are external links live and correct?

5. Verify content rendering:
   * Read through entire page on desktop
   * Check on mobile (test on actual mobile device or simulator)
   * Verify all headings are formatted correctly (H2, H3 hierarchy preserved)
   * Confirm all tables render correctly (not broken, readable)
   * Verify all lists are formatted correctly (bullets, numbering)
   * Check for text rendering issues (missing characters, encoding problems)
   * Verify bold, italic, and other formatting survived
   * Check: does content render as intended?

6. Verify TL;DR section:
   * Confirm TL;DR bullets appear prominently (often highlighted)
   * Verify all TL;DR bullets are scannable
   * Confirm TL;DR extraction is correct (if platform auto-extracts)
   * Check: is TL;DR rendering correctly?

7. Verify table of contents (if auto-generated):
   * Confirm TOC is present (if your CMS auto-generates)
   * Verify all section headings appear in TOC
   * Test TOC anchor links (click → jumps to section)
   * Confirm anchor links work correctly
   * Check: is TOC navigation functional?

8. Verify image quality:
   * Confirm featured image displays at full resolution
   * Check image is not pixelated or compressed excessively
   * Verify image loads quickly
   * Confirm alt text appears on hover (accessibility)
   * Test image on mobile (scales correctly)
   * Check: is featured image displaying properly?

9. Test social media preview:
   * Copy page URL
   * Paste into Facebook Share Dialog (or equivalent) to preview
   * Verify social title, description, and image display correctly
   * Confirm image is not stretched or distorted
   * Repeat for LinkedIn (if applicable)
   * Check: does social preview look correct?

10. Verify tag functionality:
    * If tags are clickable, test tag navigation
    * Verify clicking a tag shows related posts
    * Confirm tag pages are indexed (not orphaned)
    * Check: do tags work correctly?

11. Final integrity check:
    * Compare live URL content to final Markdown draft (word count, structure)
    * Confirm no content was lost or corrupted
    * Verify citations are present and correct
    * Check Common Mistakes section (if present)
    * Verify FAQs are complete
    * Confirm Sources list is complete and formatted
    * Check: is live content matching the approved draft?

### Outputs

The copilot produces:

* Post-Publish Verification Report with results for each check:

```
═══════════════════════════════════════════════════
POST-PUBLISH VERIFICATION REPORT
═══════════════════════════════════════════════════

Publication URL: https://yoursite.com/blog/product-descriptions/
Published Date: [Date and time]
Verification Date: [Date and time]
Verification Status: ✓ PASS or ✗ FAIL

TEST RESULTS

1. URL Accessibility
   Status: ✓ PASS
   URL responds with 200 status code
   Page load time: 1.2 seconds
   Accessible on: Desktop ✓, Mobile ✓

2. Metadata Rendering
   Status: ✓ PASS
   Page title: "How to Write Product Descriptions AI Agents Can Parse"
   Meta description: "Learn how to structure product descriptions..."
   Featured image: 1200×675px, loads correctly
   Tags visible: [#blog], [aeo], [#p-aeo] ✓

3. Internal Links (5 total tested)
   Status: ✓ PASS
   Link 1: /resources/guides/aeo-framework/ — ✓ Working
   Link 2: /blog/related-post/ — ✓ Working
   Link 3: [Pillar link] — ✓ Working
   [All internal links working, no 404s]

4. External Links (8 sampled of 12 total)
   Status: ✓ PASS
   Citation link 1 [Source A] — ✓ Live
   Citation link 2 [Source B] — ✓ Live
   [All sampled links live; assume rest are valid]

5. Content Rendering
   Status: ✓ PASS
   Desktop rendering: All sections display correctly
   Mobile rendering: Text is readable, tables are scrollable
   Headings: H2/H3 hierarchy preserved
   Tables: All render correctly, no broken cells
   Lists: Bullets and numbering intact
   Formatting (bold, italic): Preserved correctly
   Text encoding: No missing characters

6. TL;DR Section
   Status: ✓ PASS
   TL;DR bullets: 4 bullets present and highlighted
   Extractability: High (well-formatted)
   Content matches approved draft: ✓

7. Table of Contents
   Status: ✓ PASS
   TOC generated automatically with 7 sections
   All H2 headings appear in TOC
   Anchor links functional: Tested 3 links, all work
   Navigation smooth: ✓

8. Featured Image Quality
   Status: ✓ PASS
   Image dimensions: 1200×675px as specified
   Resolution: Full quality, no visible compression
   Load time: <500ms
   Mobile scaling: Responsive, no distortion
   Alt text: "AI agent extracting product description data" ✓

9. Social Media Preview
   Status: ✓ PASS
   Facebook preview: Title + description + image display correctly
   LinkedIn preview: Correct metadata
   Image is not stretched or distorted: ✓

10. Tag Functionality
    Status: ✓ PASS
    Content type tag (#blog): Clickable, shows related blog posts
    Topic tag (aeo): Clickable, shows AEO-related posts
    Pillar tag (#p-aeo): Clickable, shows pillar-related content

11. Final Integrity Check
    Status: ✓ PASS
    Content word count: 1765 words (matches draft)
    Structure: All sections present (11 H2 sections)
    Citations: 8 inline citations present
    Sources list: 5 sources listed and formatted correctly
    FAQs: 4 questions answered
    Common Mistakes: 3 mistakes addressed

═══════════════════════════════════════════════════

FINAL VERDICT: ✓ PASS — READY FOR PROMOTION

Issues Found: 0
Fixes Applied: 0
Critical Errors: None
Warnings: None

STATUS: Piece is live, renders correctly, all links functional.
Ready for promotion on social media and email.

═══════════════════════════════════════════════════
```

### Human Checkpoint

Review the verification report:

A) If PASS:

* Confirm no issues remain
* Approve piece for social/email promotion
* Archive the verification report for audit trail

B) If FAIL:

* Review issues listed in report
* For critical issues (broken links, missing content) → apply fix immediately
* For minor issues (formatting glitches) → log for future fixes
* Re-run verification after fixes

Example FAIL scenario:

```
POST-PUBLISH VERIFICATION REPORT

FINAL VERDICT: ✗ FAIL — ISSUES FOUND

Issues Found: 2
Critical Issues: 1
Warnings: 1

ISSUE 1 (Critical): Broken Internal Link
Location: H2 "Related Resources"
Link text: "See our full AEO framework"
Expected: /resources/guides/aeo-framework/
Actual: /resources/guides/aeo-framework (missing trailing slash)
Status: 404 error
Fix: Edit in CMS; add trailing slash to URL

ISSUE 2 (Warning): Image Load Delay
Location: Featured image
Load time: 3.5 seconds (slow on mobile)
Recommendation: Optimize image compression; currently 2.1MB

ACTION: Fix Issue 1 immediately. Optimize image after verification passes.
→ Re-run verification after fix
```

### Success Criteria

* URL is live and accessible (200 status)
* Page load time is acceptable (<3 seconds)
* All metadata renders correctly
* All internal links work (no 404s)
* All external links work and point to correct sources
* Content renders as expected (desktop and mobile)
* TL;DR section is scannable and prominent
* TOC (if present) is functional
* Featured image displays at full quality
* Social media preview looks correct
* All tags are functional
* Content matches approved draft (no corruption)
* Word count and structure match
* All citations are present

### Common Issues and Fixes

**Broken internal link:**

* Fix: Edit in CMS; correct URL
* Re-test: Verify link works

**Image not loading:**

* Fix: Re-upload image; ensure filename is correct
* Re-test: Confirm image loads on all devices

**Formatting corrupted (bold/italic missing):**

* Fix: Re-save HTML in CMS; restore formatting
* Re-test: Verify formatting is intact

**TOC links broken:**

* Fix: Check heading ID generation; re-save page
* Re-test: Verify anchor links work

**Social preview incorrect:**

* Fix: Clear cache; regenerate preview
* Re-test: Verify preview in Facebook/LinkedIn

**Page loads slowly:**

* Fix: Optimize images; reduce external scripts
* Re-test: Check load time again

### Timeline for Verification

* Immediately after publication (0–5 min): URL accessibility test
* 5–15 min: Full content rendering test
* 15–20 min: Links test
* 20–30 min: Full verification report

Target: Complete verification within 30 minutes of publication.

If critical issues are found (broken links, 404s), fix and re-verify before promoting on social/email.

### Documentation

Log verification results:

* Verification date and time
* Pass/Fail verdict
* Any issues found and fixed
* Final approval to promote
* Promotion start date

---

## Next Step

Once verification is PASS and any issues are fixed, proceed to **STEP 10 — Maintenance Scheduling**. call/step-10
