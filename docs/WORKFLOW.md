# Workflow Guide

Step-by-step usage for both Antigravity and Claude Code.

## Setup

```bash
# Clone and setup
cd geo-content-pipeline
bash scripts/setup.sh
```

## Phase 1: Gather Sources

Add your research materials:

```bash
# URLs (one per line)
echo "https://example.com/research" >> input/urls.txt

# Documents (PDFs, markdown, text)
cp ~/research-paper.pdf input/downloads/
cp ~/internal-playbook.md input/downloads/
```

## Phase 2: Ingest

```bash
bash scripts/ingest.sh
```

This produces a knowledge ledger at `output/knowledge-ledgers/ledger-TIMESTAMP.md` and copies it to `knowledge/latest-ledger.md`.

## Phase 3: Run the 10-Step Pipeline

### Option A: Antigravity

1. Open the repo in Antigravity
2. Start with `call/step-0` — upload your knowledge files
3. Follow each step's human checkpoints
4. The workflow guides you through all 10 steps sequentially

### Option B: Claude Code (Agent Teams)

1. Open the repo in Claude Code
2. Ask the content-lead agent to start:
   ```
   @content-lead Start the content pipeline.
   Topic: How AI agents evaluate product descriptions
   Type: Blog
   Pillar: aeo
   Audience: WooCommerce store owners
   Goal: Help store owners optimize product descriptions for AI
   ```
3. The content-lead will:
   - Create a task list mapping to the 10 steps
   - Assign knowledge-ingester to process sources
   - Assign content-writer to frame, outline, and draft
   - Assign evidence-optimizer to add citations and optimize
   - Assign editorial-qa to validate
   - Assign publisher to generate publishing card
4. You'll be asked to approve at checkpoints (outline, QA, publish)

### Option C: Claude Code (Solo)

Follow each step manually using the workflow files:

1. Read `.agent/workflows/step-0.md` — upload knowledge
2. Read `.agent/workflows/step-1.md` — frame the topic
3. Read `.agent/workflows/step-2.md` — design the outline
4. ... continue through step-10

Reference `CLAUDE.md` for project-level instructions.

## Step-by-Step Detail

### Step 0: Knowledge Ingestion
- **Input:** Markdown files, URLs, documents
- **Output:** Knowledge summary, terminology map, source inventory
- **Checkpoint:** Verify knowledge was interpreted correctly

### Step 1: Intake & Framing
- **Input:** Topic, content type, pillar, audience, goal
- **Output:** Refined topic, reader profile, thesis, success criteria
- **Checkpoint:** Approve framing before outlining

### Step 2: Outline & Angle Validation
- **Input:** Approved framing
- **Output:** 3 title options, H2/H3 outline, section intent map
- **Checkpoint:** Approve outline before drafting (revision is cheapest here)

### Step 3: Draft Generation
- **Input:** Locked outline
- **Output:** Complete v1 draft in Markdown
- **Checkpoint:** Flag specific sections for revision

### Step 4: Evidence & Citation Pass
- **Input:** Draft v1
- **Output:** Draft v2 with citations, Citation TODO list
- **Checkpoint:** Provide missing sources or approve labels

### Step 5: GEO Optimization
- **Input:** Draft v2
- **Output:** Draft v3 optimized for extraction
- **Checkpoint:** Check for over-optimization or nuance loss

### Step 6: Editorial QA
- **Input:** Draft v3
- **Output:** PASS/FAIL verdict with fix list
- **Checkpoint:** If FAIL, fixes are applied and QA re-runs

### Step 7: Ghost Publishing Card
- **Input:** QA-approved draft
- **Output:** Complete publishing specification
- **Checkpoint:** Verify metadata accuracy

### Step 8: Human Approval
- **Input:** Draft, card, risk assessment
- **Output:** APPROVE / APPROVE WITH NOTES / REQUEST CHANGES
- **Checkpoint:** Explicit human decision required

### Step 9: Post-Publish Verification
- **Input:** Live published URL
- **Output:** Verification report (PASS/FAIL)
- **Checkpoint:** Fix any issues before promotion

### Step 10: Maintenance Scheduling
- **Input:** Published piece
- **Output:** Review dates, volatile sections, refresh triggers
- **Checkpoint:** Confirm schedule is realistic

## Output Files

After a complete run, you'll have:

```
output/
├── knowledge-ledgers/
│   └── ledger-20260217-143000.md     # Knowledge from sources
├── drafts/
│   ├── [slug]-v1.md                  # First draft
│   ├── [slug]-v2.md                  # With citations
│   └── [slug]-v3.md                  # GEO-optimized final
└── publishing-cards/
    ├── [slug]-card.md                # Ghost publishing spec
    └── [slug]-maintenance.md         # Maintenance schedule
```
