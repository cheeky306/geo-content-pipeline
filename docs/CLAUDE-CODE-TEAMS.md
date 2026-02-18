# Claude Code Agent Teams

How the agent team orchestration works in the Claude Code version of the GEO Content Pipeline.

## Overview

The Claude Code version uses 6 specialized agents that map to the 10-step workflow. A content-lead orchestrates the team using task lists and message passing.

## Agent Team

| Agent | File | Steps | Tools |
|-------|------|-------|-------|
| **content-lead** | `.claude/agents/content-lead.md` | Orchestrator | Read, Write, Bash, Task, TaskCreate/Update/List, SendMessage |
| **knowledge-ingester** | `.claude/agents/knowledge-ingester.md` | Step 0 | Read, Write, Bash, Glob, Grep |
| **content-writer** | `.claude/agents/content-writer.md` | Steps 1-3 | Read, Write, Glob, Grep |
| **evidence-optimizer** | `.claude/agents/evidence-optimizer.md` | Steps 4-5 | Read, Write, Glob, Grep |
| **editorial-qa** | `.claude/agents/editorial-qa.md` | Step 6 | Read, Glob, Grep |
| **publisher** | `.claude/agents/publisher.md` | Steps 7-10 | Read, Write, Glob, Grep |

## How It Works

### 1. User Triggers the Pipeline

The user asks the content-lead to start:

```
@content-lead Start the content pipeline for [topic].
Type: Blog
Pillar: aeo
Audience: [audience]
Goal: [goal]
```

### 2. Content-Lead Creates Tasks

The content-lead breaks the request into tasks:

```
Task 1: Ingest knowledge sources (knowledge-ingester)
Task 2: Frame topic and create brief (content-writer)
Task 3: Design outline (content-writer)          [blocked by Task 2]
Task 4: Generate draft v1 (content-writer)        [blocked by Task 3]
Task 5: Evidence & citation pass (evidence-optimizer) [blocked by Task 4]
Task 6: GEO optimization (evidence-optimizer)     [blocked by Task 5]
Task 7: Editorial QA (editorial-qa)               [blocked by Task 6]
Task 8: Publishing card (publisher)                [blocked by Task 7]
Task 9: Human approval (publisher)                [blocked by Task 8]
Task 10: Post-publish verification (publisher)    [blocked by Task 9]
Task 11: Maintenance scheduling (publisher)       [blocked by Task 10]
```

### 3. Parallel Work Where Possible

- **knowledge-ingester** can process sources while the content-writer works on framing (Tasks 1 and 2 run in parallel)
- Sequential dependencies are enforced by task blocking

### 4. Quality Gates

Three checkpoints require human input:

1. **After outline (Task 3):** User approves structure before drafting
2. **After QA (Task 7):** Editorial QA produces PASS/FAIL
3. **After approval request (Task 9):** User explicitly approves publication

### 5. Failure Handling

If editorial QA fails:
- Content-lead routes fixes back to the responsible agent
- evidence-optimizer for citation issues
- content-writer for structural issues
- After fixes, editorial-qa re-runs

If human requests changes at approval:
- Content-lead identifies which step to return to
- Routes back to appropriate agent
- QA must pass again before re-submitting for approval

## Agent Communication

Agents communicate through:

1. **Task list** — Shared task state via TaskCreate/TaskUpdate/TaskList
2. **Messages** — Direct messages via SendMessage for coordination
3. **Files** — Shared file system (output/drafts/, output/knowledge-ledgers/)

## File Handoffs

| From | To | File |
|------|----|------|
| knowledge-ingester | content-writer | `knowledge/latest-ledger.md` |
| content-writer | evidence-optimizer | `output/drafts/[slug]-v1.md` |
| evidence-optimizer | editorial-qa | `output/drafts/[slug]-v3.md` |
| editorial-qa | publisher | QA report (inline or file) |
| publisher | user | `output/publishing-cards/[slug]-card.md` |

## Running the Team

In Claude Code, you can:

```bash
# Start with the content-lead
@content-lead Start the content pipeline for [topic]

# Or address specific agents directly
@knowledge-ingester Ingest the URLs in input/urls.txt
@content-writer Frame a blog about [topic] for [audience]
@editorial-qa Run QA on output/drafts/my-post-v3.md
```

## Shared Resources

All agents have access to:

- `knowledge/brand/haandshake-company.md` — Brand voice guide
- `.agent/workflows/` — Detailed step instructions
- `.agent/rules/rule1.md` — Editorial governance rules
- `.agent/skills/content-agent/resources/templates.json` — Structure templates
- `.agent/skills/content-agent/scripts/haandshake-prompts.md` — Prompt templates
