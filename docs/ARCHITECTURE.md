# Architecture

## System Overview

The GEO Content Pipeline is a structured workflow that transforms raw source materials (URLs, PDFs, documents) into publish-ready, GEO/AEO-optimized content with full editorial governance.

## Data Flow

```
                    ┌─────────────┐
                    │   SOURCES   │
                    │             │
                    │  URLs       │
                    │  PDFs       │
                    │  Markdown   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   SCRAPER   │
                    │             │
                    │  Collect    │
                    │  Clean      │
                    │  Chunk      │
                    │  Score      │
                    │  Extract    │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  KNOWLEDGE  │
                    │   LEDGER    │
                    │             │
                    │  Topics     │
                    │  Sources    │
                    │  Authority  │
                    └──────┬──────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
   ┌──────▼──────┐ ┌──────▼──────┐ ┌───────▼─────┐
   │   FRAMING   │ │   OUTLINE   │ │    DRAFT    │
   │  (Step 1)   │ │  (Step 2)   │ │  (Step 3)   │
   │             │ │             │ │             │
   │  Topic      │ │  Titles     │ │  v1 draft   │
   │  Audience   │ │  H2/H3     │ │  TL;DR      │
   │  Thesis     │ │  Structure  │ │  FAQs       │
   └─────────────┘ └─────────────┘ └──────┬──────┘
                                          │
                    ┌──────▼──────┐ ┌──────▼──────┐
                    │  EVIDENCE   │ │     GEO     │
                    │  (Step 4)   │ │  (Step 5)   │
                    │             │ │             │
                    │  Citations  │ │  Chunking   │
                    │  Sources    │ │  Answer-1st │
                    │  TODO list  │ │  Extraction │
                    └─────────────┘ └──────┬──────┘
                                          │
                    ┌──────▼──────┐
                    │ EDITORIAL   │
                    │    QA       │
                    │  (Step 6)   │
                    │             │
                    │  PASS/FAIL  │
                    └──────┬──────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
   ┌──────▼──────┐ ┌──────▼──────┐ ┌───────▼─────┐
   │ GHOST CARD  │ │  APPROVAL   │ │   VERIFY    │
   │  (Step 7)   │ │  (Step 8)   │ │  (Step 9)   │
   └─────────────┘ └─────────────┘ └──────┬──────┘
                                          │
                                   ┌──────▼──────┐
                                   │ MAINTENANCE │
                                   │  (Step 10)  │
                                   └─────────────┘
```

## Component Architecture

### Scraper (`scraper/`)

```
scraper/
├── knowledge_ledger_agent.py    # Main CLI — orchestrates the pipeline
├── models.py                    # Data models (Source, Topic, KnowledgeLedger)
├── utils.py                     # Shared utilities
├── collectors/
│   ├── base_collector.py        # Abstract collector interface
│   ├── url_collector.py         # HTTP scraping with BeautifulSoup
│   └── document_collector.py    # PDF (pdfplumber) and text file reading
├── processors/
│   ├── cleaner.py               # Text normalization, encoding fixes
│   ├── chunker.py               # Semantic chunking by headings/paragraphs
│   ├── topic_extractor.py       # TF-IDF keyword and topic extraction
│   ├── authority_scorer.py      # Source classification and scoring
│   └── qa_checker.py            # Markdown linting and structure validation
└── generators/
    ├── ledger_builder.py        # Assembles the final ledger markdown
    ├── tier1_builder.py         # Executive index (topics + source map)
    └── tier2_builder.py         # Full source content with metadata
```

### Agent Architecture (Claude Code)

```
content-lead (orchestrator)
    │
    ├── knowledge-ingester  →  Step 0
    ├── content-writer      →  Steps 1-3
    ├── evidence-optimizer  →  Steps 4-5
    ├── editorial-qa        →  Step 6
    └── publisher           →  Steps 7-10
```

The content-lead uses TaskCreate/TaskUpdate to coordinate work across agents. Quality gates at Steps 2, 6, and 8 require human approval before proceeding.

### Shared Resources

Both the Antigravity and Claude Code versions share:

- `knowledge/brand/` — Brand voice and positioning
- `knowledge/` — Ingested knowledge bases
- `input/` — Source materials
- `output/` — Generated content
- `scraper/` — Python knowledge ledger tool
- `.agent/skills/content-agent/resources/templates.json` — Structure templates
- `.agent/rules/rule1.md` — Editorial governance rules

## Authority Scoring

The scraper scores each source 0-100 based on:

| Factor | Impact |
|--------|--------|
| Source type (academic, research, documentation, news, blog, opinion) | Base score (40-90) |
| Domain authority (.edu, .gov, .org, major publications) | +5 to +15 |
| Content quality (references, data, methodology, credentials) | +5 to +25 |
| Metadata completeness (author, date, description) | +2 to +7 |
| Clickbait indicators | -5 penalty |

## Quality Enforcement

The pipeline enforces quality at multiple levels:

1. **Rule-level** — `.agent/rules/rule1.md` defines hard rules for taxonomy, structure, claims, writing quality, GEO optimization, and output formatting
2. **Template-level** — `templates.json` defines minimum section requirements for blogs and guides
3. **QA-level** — Step 6 runs a 10-category checklist with PASS/FAIL verdicts
4. **Human-level** — Steps 2, 6, and 8 require explicit human approval
