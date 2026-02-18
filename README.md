<p align="center">
  <h1 align="center">GEO Content Pipeline</h1>
  <p align="center">
    <strong>🚀 The open-source content engine built for AI search.</strong><br>
    Evidence-backed. GEO-optimized. Human-governed.
  </p>
  <p align="center">
    <a href="#quick-start">Quick Start</a> &nbsp;&bull;&nbsp;
    <a href="#the-10-step-workflow">Workflow</a> &nbsp;&bull;&nbsp;
    <a href="#why-this-exists">Why This Exists</a> &nbsp;&bull;&nbsp;
    <a href="docs/ARCHITECTURE.md">Architecture</a> &nbsp;&bull;&nbsp;
    <a href="docs/WORKFLOW.md">Full Guide</a>
  </p>
</p>

---

> **Most AI content tools optimize for speed. This one optimizes for trust.**
>
> Every claim is sourced or labeled. Every draft passes a 10-category QA gate. Every publish requires explicit human approval. The result is content that AI systems cite — not content they ignore.

---

## ⚡ What This Does

```
URLs + Documents  ──►  Knowledge Ledger  ──►  10-Step Pipeline  ──►  Publish-Ready Content
     (input/)            (scraper)             (agents)              (Markdown + Publishing Card)
```

Drop your research URLs and documents into `input/`. The pipeline scrapes, scores, and structures them into a knowledge ledger. Then 10 governed steps transform that knowledge into publish-ready content optimized for Google AI Overviews, ChatGPT, Perplexity, and other generative search systems.

---

## 🎯 Why This Exists

Content for AI search is a different game. Traditional SEO content — keyword-stuffed, opinion-heavy, lightly sourced — gets filtered out by generative engines. To earn citations in AI-generated answers, content needs to be:

- **Structured for extraction** — chunked sections, answer-first sentences, scannable tables
- **Evidence-dense** — every claim sourced, every statistic cited, every quote attributed
- **Editorially governed** — consistent terminology, brand-aligned tone, no fluff

This pipeline enforces all three. Systematically. Every time.

---

## 🏆 What Makes This Different

<table>
<tr>
<td width="50%">

### ❌ Typical AI Content Tools

- Generate content from prompts
- No source verification
- No editorial governance
- Output is a single draft
- Hope for the best

</td>
<td width="50%">

### ✅ GEO Content Pipeline

- Generate from YOUR research + knowledge base
- Every claim sourced, labeled, or flagged
- 10-category QA gate with PASS/FAIL verdict
- 3 draft versions (raw → cited → optimized)
- Structured for AI citation probability

</td>
</tr>
</table>

### Key Differentiators

**🧠 1. Knowledge-First, Not Prompt-First**
> Most tools start with a prompt. This pipeline starts with your actual research — URLs, PDFs, internal playbooks. The scraper ingests, scores authority (0-100), extracts topics via TF-IDF, and builds a structured knowledge ledger. Content is grounded in your evidence, not general AI training data.

**🔬 2. Evidence as a Hard Requirement**
> The pipeline treats unsourced claims like bugs. Step 4 extracts every factual claim and either matches it to a source, or labels it `[Needs source]`, `[Hypothesis]`, or `[Verified]`. A Citation TODO list tracks what's missing. No claim ships unaccounted for.

**🛡️ 3. Three-Gate Human Governance**
> Agents propose. Humans decide. Three checkpoints require explicit approval:
> - **Outline lock** (Step 2) — structure approved before any prose is written
> - **Editorial QA** (Step 6) — 10-category PASS/FAIL checklist
> - **Publish approval** (Step 8) — explicit APPROVE / REQUEST CHANGES decision

**📐 4. GEO-Engineered Structure**
> Every section opens with a standalone answer sentence. Content is chunked at H2/H3 every 200-400 words. Tables have headers and captions. Lists are parallel and actionable. Definitions appear once and are reused consistently. This isn't formatting — it's engineering content for extraction by generative systems.

**📊 5. Built-In Authority Scoring**
> The scraper classifies every source (academic, research, documentation, news, blog, opinion) and scores authority based on domain, content quality indicators, and metadata completeness. Your knowledge ledger shows exactly what you're building on.

**🔄 6. Post-Publish Lifecycle**
> Most pipelines stop at "publish." This one continues with post-publish verification (links, rendering, social previews) and maintenance scheduling (volatile section tracking, refresh triggers, decay indicators). Content authority compounds over time — but only if maintained.

---

## 🔟 The 10-Step Workflow

```
 STEP 0        STEP 1        STEP 2        STEP 3        STEP 4
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│KNOWLEDGE│─►│ INTAKE  │─►│ OUTLINE │─►│  DRAFT  │─►│EVIDENCE │
│INGESTION│  │& FRAMING│  │& ANGLE  │  │  (v1)   │  │& CITE   │
└─────────┘  └─────────┘  └────┬────┘  └─────────┘  └─────────┘
                               │                          │
                          HUMAN GATE                      ▼
                         (approve outline)
                                                    STEP 5
                                                   ┌─────────┐
                                                   │   GEO   │
                                                   │OPTIMIZE │
                                                   └────┬────┘
                                                        ▼
 STEP 10       STEP 9        STEP 8        STEP 7    STEP 6
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│MAINTAIN │◄─│ VERIFY  │◄─│ APPROVE │◄─│PUBLISH  │◄─│EDITORIAL│
│SCHEDULE │  │  LIVE   │  │(HUMAN)  │  │  CARD   │  │   QA    │
└─────────┘  └─────────┘  └────┬────┘  └─────────┘  └────┬────┘
                               │                          │
                          HUMAN GATE                 HUMAN GATE
                         (APPROVE/REJECT)           (PASS/FAIL)
```

| Step | Name | What Happens | Output |
|:----:|------|-------------|--------|
| 0 | **Knowledge Ingestion** | Scrape URLs, parse documents, build knowledge map | Knowledge ledger, terminology map, source inventory |
| 1 | **Intake & Framing** | Validate topic, define audience, set success criteria | Editorial brief with thesis and reader profile |
| 2 | **Outline & Angle** | Design H2/H3 structure, map sections to reader intent | Locked outline with 3 title options |
| 3 | **Draft Generation** | Write complete v1 following locked outline exactly | Full Markdown draft with all required sections |
| 4 | **Evidence & Citations** | Source every claim, flag gaps, build citation TODO | Draft v2 with inline citations and source labels |
| 5 | **GEO Optimization** | Chunk for extraction, answer-first sentences, optimize tables | Draft v3 optimized for AI selection |
| 6 | **Editorial QA** | Run 10-category checklist: structure, citations, GEO, tone | PASS/FAIL verdict with required fixes |
| 7 | **Publishing Card** | Compile metadata, tags, image spec, pre/post-publish checklists | CMS-ready publishing specification |
| 8 | **Human Approval** | Summarize changes, assess risks, request explicit decision | APPROVE / APPROVE WITH NOTES / REQUEST CHANGES |
| 9 | **Post-Publish Verify** | Test URL, links, rendering, social previews, metadata | Verification report (PASS/FAIL) |
| 10 | **Maintenance** | Identify volatile sections, set review dates, define refresh triggers | Maintenance schedule with decay indicators |

---

## 🔀 Two Ways to Run It

This repo ships with two parallel interfaces. Same workflow. Same knowledge base. Same output.

### Option A: Antigravity (`.agent/`)

The original platform. 11 workflow step files, editorial rules, skill definitions, prompt scripts, and templates.

```
Open in Antigravity → call/step-0 → follow the workflow
```

### Option B: Claude Code (`.claude/`)

An agent teams version with 6 specialist agents coordinated by a lead.

```
Open in Claude Code → @content-lead Start the pipeline for [topic]
```

| Agent | Steps | Role |
|-------|:-----:|------|
| `content-lead` | All | Orchestrates team, manages tasks, enforces quality gates |
| `knowledge-ingester` | 0 | Runs scraper, builds knowledge base |
| `content-writer` | 1-3 | Frames topic, designs outline, generates draft |
| `evidence-optimizer` | 4-5 | Citation engineering, GEO/AEO optimization |
| `editorial-qa` | 6 | 10-category QA checklist, PASS/FAIL verdict |
| `publisher` | 7-10 | Publishing card, approval flow, verification, maintenance |

---

## ⚙️ Quick Start

### 1. Clone and setup

```bash
git clone https://github.com/cheeky306/geo-content-pipeline.git
cd geo-content-pipeline
bash scripts/setup.sh
```

### 2. Add your sources

```bash
# Add research URLs (one per line)
echo "https://example.com/research-article" >> input/urls.txt

# Or drop documents directly
cp ~/research-paper.pdf input/downloads/
cp ~/internal-playbook.md input/downloads/
```

### 3. Ingest into knowledge ledger

```bash
bash scripts/ingest.sh
```

### 4. Run the pipeline

```bash
# Full run (ingest + guided generation)
bash scripts/generate.sh
```

Or open directly in your preferred platform:

- **Antigravity:** `call/step-0`
- **Claude Code:** `@content-lead Start the content pipeline for [your topic]`

---

## 🕷️ The Scraper

A Python CLI that transforms raw sources into structured knowledge.

```bash
# From URLs
python3 scraper/knowledge_ledger_agent.py --urls "https://example.com" --output ledger.md

# From documents
python3 scraper/knowledge_ledger_agent.py --folder input/downloads --output ledger.md

# Both
python3 scraper/knowledge_ledger_agent.py --urls "https://..." --folder input/downloads --output ledger.md
```

**What it does:**

| Stage | Tool | Purpose |
|-------|------|---------|
| Collect | BeautifulSoup, pdfplumber | Scrape URLs, extract PDF/text/markdown content |
| Clean | Custom normalizer | Fix encoding, normalize whitespace, repair markdown |
| Chunk | Semantic splitter | Split by headings and paragraphs for structure |
| Score | Authority scorer | Classify source type, score 0-100 based on domain + content signals |
| Extract | scikit-learn TF-IDF | Identify core topics across all sources |
| Build | Ledger generator | Produce executive index + full source content in markdown |

---

## 🗂️ Project Structure

```
geo-content-pipeline/
│
├── .agent/                            ← Antigravity interface
│   ├── workflows/step-0.md … step-10.md
│   ├── rules/rule1.md
│   └── skills/content-agent/
│       ├── SKILL.md
│       ├── scripts/haandshake-prompts.md
│       └── resources/templates.json
│
├── .claude/                           ← Claude Code interface
│   └── agents/
│       ├── content-lead.md
│       ├── knowledge-ingester.md
│       ├── content-writer.md
│       ├── evidence-optimizer.md
│       ├── editorial-qa.md
│       └── publisher.md
│
├── knowledge/brand/                   ← Brand voice & positioning
├── input/                             ← Drop zone (URLs + documents)
├── output/                            ← Generated content lands here
│   ├── drafts/                           v1 → v2 → v3
│   ├── knowledge-ledgers/                Scraper output
│   └── publishing-cards/                 CMS specs + maintenance
│
├── scraper/                           ← Python knowledge ledger tool
│   ├── collectors/                       URL + document ingestion
│   ├── processors/                       Clean, chunk, score, extract
│   └── generators/                       Ledger assembly
│
├── scripts/                           ← One-command automation
│   ├── setup.sh                          Install deps
│   ├── ingest.sh                         Run scraper on input/
│   └── generate.sh                       Full pipeline
│
├── CLAUDE.md                          ← Project instructions for Claude Code
└── docs/                              ← Architecture, workflow, teams guide
```

---

## 📋 Requirements

- **Python 3.8+** (for the scraper)
- **One of:**
  - [Antigravity](https://antigravity.dev) — for the `.agent/` workflow
  - [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — for the `.claude/` agent teams

---

## 📚 Documentation

| Doc | What's In It |
|-----|-------------|
| [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) | System diagrams, component relationships, authority scoring breakdown |
| [`docs/WORKFLOW.md`](docs/WORKFLOW.md) | Step-by-step usage guide for both platforms |
| [`docs/CLAUDE-CODE-TEAMS.md`](docs/CLAUDE-CODE-TEAMS.md) | How the 6-agent team coordinates, file handoffs, quality gates |
| [`CLAUDE.md`](CLAUDE.md) | Project-level instructions for Claude Code |

---

## 💡 Design Principles

> **Structure precedes prose.** Outline is locked before writing begins.
>
> **Evidence precedes authority.** Claims must be sourced or explicitly labeled.
>
> **Humans approve meaning.** Agents propose; humans decide intent.
>
> **Systems enforce standards.** QA gates prevent non-compliant content.
>
> **Authority compounds over time.** Maintenance preserves content value.

---

<p align="center">
  <strong>Built by <a href="https://www.linkedin.com/in/jordianfarahani/">Jordian Farahani</a> at <a href="https://haandshake.com">Haandshake</a></strong><br>
  Research-driven GEO/AEO agency.<br>
  We engineer authority in generative and answer-first search environments.
</p>

<p align="center">
  <sub>MIT License</sub>
</p>
