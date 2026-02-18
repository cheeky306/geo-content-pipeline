# GEO Content Pipeline

A production-grade pipeline for generating evidence-backed, GEO/AEO-optimized content. Built for AI-first search environments.

```
URLs + Documents  ──►  Knowledge Ledger  ──►  10-Step Pipeline  ──►  Publish-Ready Content
                         (scraper)           (agents)                (Markdown + Publishing Card)
```

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     GEO CONTENT PIPELINE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INPUT                    PROCESSING                  OUTPUT    │
│  ─────                    ──────────                  ──────    │
│                                                                 │
│  input/urls.txt    ──►  ┌──────────────┐                        │
│  input/downloads/  ──►  │   Scraper    │  ──►  Knowledge       │
│                         │  (Python)    │       Ledger (.md)    │
│                         └──────────────┘                        │
│                                │                                │
│                                ▼                                │
│  knowledge/brand/  ──►  ┌──────────────────────────────────┐    │
│                         │     10-STEP WORKFLOW              │    │
│                         │                                  │    │
│                         │  Step 0:  Knowledge Ingestion    │    │
│                         │  Step 1:  Intake & Framing       │    │
│                         │  Step 2:  Outline Validation     │    │
│                         │  Step 3:  Draft Generation       │    │
│                         │  Step 4:  Evidence & Citations   │    │
│                         │  Step 5:  GEO Optimization       │    │
│                         │  Step 6:  Editorial QA           │──► │
│                         │  Step 7:  Publishing Card  │    │
│                         │  Step 8:  Human Approval         │    │
│                         │  Step 9:  Post-Publish Verify    │    │
│                         │  Step 10: Maintenance Schedule   │    │
│                         └──────────────────────────────────┘    │
│                                                                 │
│                                                    output/      │
│                                                    ├── drafts/  │
│                                                    ├── ledgers/ │
│                                                    └── cards/   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  INTERFACES                                                     │
│                                                                 │
│  .agent/     Antigravity (workflows, skills, rules)             │
│  .claude/    Claude Code  (6 agent team + CLAUDE.md)            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Two Interfaces, One Pipeline

This repo provides two parallel ways to run the same 10-step workflow:

### Antigravity (`.agent/`)
The original workflow built for the Antigravity platform. Contains step-by-step workflow files, editorial rules, skills, prompt scripts, and templates.

### Claude Code (`.claude/`)
An agent teams version with 6 specialist agents that map to the 10 workflow steps. A content-lead orchestrates the team with TaskCreate/TaskUpdate coordination.

Both share the same knowledge base, brand files, scraper, and output directories.

## Prerequisites

- Python 3.8+
- One of:
  - [Antigravity](https://antigravity.dev) — for the `.agent/` version
  - [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — for the `.claude/` version

## Quick Start

### 1. Setup

```bash
git clone <repo-url> geo-content-pipeline
cd geo-content-pipeline
bash scripts/setup.sh
```

### 2. Add Sources

```bash
# Add URLs
echo "https://example.com/research-article" >> input/urls.txt

# Or drop documents
cp ~/path/to/research.pdf input/downloads/
```

### 3. Ingest

```bash
bash scripts/ingest.sh
```

This scrapes URLs, processes documents, and produces a structured knowledge ledger in `output/knowledge-ledgers/`.

### 4. Generate Content

**Antigravity:**
Open the repo in Antigravity. Start with `call/step-0`.

**Claude Code (Agent Teams):**
Open the repo in Claude Code. Ask the content-lead:
```
@content-lead Start the content pipeline for [your topic]
```

**Claude Code (Solo):**
Open the repo and follow the steps in `CLAUDE.md`.

## The 10-Step Workflow

| Step | Name | What It Does |
|------|------|-------------|
| 0 | Knowledge Ingestion | Parse uploads, build knowledge map, flag conflicts |
| 1 | Intake & Framing | Validate topic, define audience, set success criteria |
| 2 | Outline & Angle Validation | Design H2/H3 structure, lock outline before writing |
| 3 | Draft Generation | Write complete v1 draft following locked outline |
| 4 | Evidence & Citation Pass | Source all claims, build citation TODO list |
| 5 | GEO Optimization | Optimize for extraction: chunking, answer-first, tables |
| 6 | Editorial QA | PASS/FAIL quality gate across 10 categories |
| 7 | Publishing Card | Generate publishing metadata and checklists |
| 8 | Human Approval | Explicit APPROVE/REQUEST CHANGES decision |
| 9 | Post-Publish Verification | Test live rendering, links, metadata |
| 10 | Maintenance Scheduling | Set review dates, track volatile sections |

## Key Principles

1. **Structure precedes prose.** Outline is locked before writing begins.
2. **Evidence precedes authority.** Claims must be sourced or explicitly labeled.
3. **Humans approve meaning.** Agent proposes; humans decide intent.
4. **Systems enforce standards.** QA gates prevent non-compliant content.
5. **Authority compounds over time.** Maintenance preserves content value.

## Scraper

The `scraper/` directory contains a Python CLI tool that processes URLs and documents into structured knowledge ledgers. It uses:

- **BeautifulSoup** for web scraping
- **pdfplumber** for PDF extraction
- **scikit-learn TF-IDF** for topic extraction
- **Authority scoring** based on source type and domain
- **QA checking** with pymarkdown and mdformat

```bash
# Direct usage
cd scraper
python3 knowledge_ledger_agent.py --urls "https://example.com" --output ledger.md
python3 knowledge_ledger_agent.py --folder ../input/downloads --output ledger.md
```

## Project Structure

```
geo-content-pipeline/
├── README.md
├── LICENSE (MIT)
├── CLAUDE.md                          # Claude Code project instructions
├── .gitignore
│
├── .agent/                            # Antigravity version
│   ├── workflows/step-0.md … step-10.md
│   ├── rules/rule1.md
│   └── skills/content-agent/
│
├── .claude/                           # Claude Code version
│   ├── agents/
│   │   ├── content-lead.md
│   │   ├── knowledge-ingester.md
│   │   ├── content-writer.md
│   │   ├── evidence-optimizer.md
│   │   ├── editorial-qa.md
│   │   └── publisher.md
│   └── settings.local.json
│
├── knowledge/                         # Shared knowledge base
│   └── brand/haandshake-company.md
│
├── input/                             # Source drop zone
│   ├── urls.txt
│   └── downloads/
│
├── output/                            # Generated content
│   ├── drafts/
│   ├── knowledge-ledgers/
│   └── publishing-cards/
│
├── scraper/                           # Python knowledge ledger tool
│   ├── knowledge_ledger_agent.py
│   ├── models.py, utils.py
│   ├── collectors/, processors/, generators/
│   ├── requirements.txt
│   └── setup.sh
│
├── scripts/                           # Automation
│   ├── setup.sh
│   ├── ingest.sh
│   └── generate.sh
│
└── docs/
    ├── ARCHITECTURE.md
    ├── WORKFLOW.md
    └── CLAUDE-CODE-TEAMS.md
```

## Built By

Built by [Jordian Farahani](https://www.linkedin.com/in/jordianfarahani/) at [Haandshake](https://haandshake.com) — Research-driven GEO/AEO agency. We engineer authority in generative and answer-first search environments.

## License

MIT
