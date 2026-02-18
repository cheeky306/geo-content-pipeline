# GEO Content Pipeline

## What This Is

A production-grade content pipeline for generating GEO/AEO-optimized, evidence-backed content. Built by Haandshake.

## Repository Structure

- `.agent/` — Antigravity version (10-step workflow, skills, rules)
- `.claude/agents/` — Claude Code agent teams version (6 specialist agents)
- `knowledge/` — Brand files and ingested knowledge bases
- `input/` — Drop zone for source URLs and documents
- `output/` — Generated content (drafts, ledgers, publishing cards)
- `scraper/` — Python knowledge ledger tool (URL + document ingestion)
- `scripts/` — Automation wrappers

## Quick Start

```bash
# Setup (installs Python deps, NLTK data)
bash scripts/setup.sh

# Add sources
echo "https://example.com/article" >> input/urls.txt
# Or drop PDFs/docs into input/downloads/

# Ingest sources into knowledge ledger
bash scripts/ingest.sh

# Run the full pipeline
bash scripts/generate.sh
```

## Content Generation Commands

### Solo Mode (follow steps manually)
Read the workflow steps in `.agent/workflows/step-0.md` through `step-10.md` and execute them in sequence.

### Agent Teams Mode
The `content-lead` agent orchestrates a team of 5 specialists. Start by asking the content-lead to run the pipeline for your topic. The team will:

1. **knowledge-ingester** — Ingest sources, build knowledge ledger (Step 0)
2. **content-writer** — Frame topic, design outline, generate draft (Steps 1-3)
3. **evidence-optimizer** — Integrate citations, optimize for GEO/AEO (Steps 4-5)
4. **editorial-qa** — Run editorial QA checklist, PASS/FAIL verdict (Step 6)
5. **publisher** — Generate Ghost card, request approval, verify, schedule maintenance (Steps 7-10)

## Key Rules

- **Evidence first**: No claim ships without a source or explicit label ([Needs source], [Hypothesis], [Verified])
- **Structure before prose**: Outline is locked before drafting begins
- **Human approval required**: No content publishes without explicit human APPROVE
- **GEO optimization**: Answer-first sentences, chunked H2/H3 every 200-400 words, extractable tables/lists
- **Taxonomy**: Every post needs exactly one content type tag, one topic tag, one pillar tag

## Brand Voice

Read `knowledge/brand/haandshake-company.md` before writing any content. Key attributes: clear, precise, calm, confident, analytical, practical. No hype. No fluff.

## File Conventions

- Knowledge ledgers go in `output/knowledge-ledgers/`
- Draft content goes in `output/drafts/`
- Publishing cards go in `output/publishing-cards/`
- The latest ingested ledger is copied to `knowledge/latest-ledger.md`
