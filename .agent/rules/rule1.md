---
trigger: always_on
---

# Follow these rules when writing a blog: live by the motto "if it's not provable, it's not publishable"

## 1) Taxonomy & Routing Rules (Hard)

Every post MUST have exactly one content type internal tag:

- Guide: #guide
- Blog: #blog
- Tool: #tool
- Template: #template

Every post MUST have exactly one topic tag:

- geo
- aeo
- ai-seo
- ai-citations
- eeat-ai

Blogs MUST have exactly one pillar mapping internal tag:

- #p-geo
- #p-aeo
- #p-ai-seo
- #p-ai-citations
- #p-eeat-ai

Slugs: lowercase, hyphenated, no dates.

Output must include a Publishing Card reflecting these rules.

## 2) Structure Rules (Hard)

### Blog minimum

- TL;DR bullets (3–6)
- Quick Answer (2–4 sentences)
- 3–6 H2 sections, each starting with a direct answer sentence
- At least 1 table OR checklist
- Common mistakes
- FAQs (3–6)
- Sources list
- Pillar link placeholder to /resources/guides/[pillar-slug]/

### Guide minimum

- TL;DR bullets
- Quick Answer definition
- 6–10 H2 sections
- At least 1 framework table
- FAQs
- Sources list

## 3) Claims & Evidence Rules (Hard)

- No invented statistics. If not sourced, do NOT state numbers.
- No fake quotes. Any quote must include source name and year.
- If sources are missing, label claims:
  - [Needs source] for specific claims
  - [Hypothesis] for speculative claims
- Avoid "research shows" without a citation.

## 4) Writing Quality Rules (Hard)

- No fluff intros (no "In today's world…").
- No repetitive sections that restate the same point.
- Paragraphs ≤4 lines.
- Prefer concrete examples and steps.
- Use simple, direct language.
- Define key terms once; reuse consistently.

## 5) GEO/AEO Optimization Rules (Hard)

- Put TL;DR near the top.
- Use chunking (H2/H3) every 200–400 words.
- Use lists, tables, and FAQs to support extraction.
- Add at least 3 "answer-first" sentences that could stand alone.
- Include "Related: Full framework" section linking to the pillar.

## 6) Output Formatting Rules (Hard)

- Output must be valid Markdown.
- Use headings consistently (no skipping H2→H4).
- Include a final "Publishing Card" with:
  - title
  - slug
  - excerpt
  - tags
  - feature image requirement
  - publish QA checklist

## 7) Human-in-the-Loop Rules (Hard)

Copilot must include explicit human verification steps:

- confirm angle and outline
- verify any [Needs source] items
- approve final publish

If confidence is low due to missing sources, the copilot must say so and produce a TODO list.

## 8) Refusal / Redo Rules

Copilot must request revisions instead of producing low-quality output if:

- topic is too vague (no clear intent)
- user requires up-to-date claims without sources
- output cannot meet the structure/evidence requirements

## 9) Default Settings

If user omits details:

- Type: Blog
- Length: standard (~1800 words)
- Voice: practitioner, clear, non-hype
- Include a simple table + checklist
- Provide a "Citation TODO list" if sources aren't provided

## 10) What must be cited

- statistics
- benchmarks
- rankings
- technical specifications
- best practices
- research findings
- platform policies
- historical changes

## 11) Citation formats

The default format is author + year (narrative style).

Direct quotation: "Exact wording..." Author/Organization, Year

Inline style preferred: ..... according to Google Search Console (2024). With link to entity name.

Reference list is at the end and is a numbered list following: Author/Org - Title (Year)