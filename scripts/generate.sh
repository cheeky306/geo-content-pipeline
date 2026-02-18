#!/bin/bash
# Full pipeline: ingest sources then guide content generation
# Usage: bash scripts/generate.sh

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "======================================="
echo " GEO Content Pipeline — Full Run"
echo "======================================="

# Step 1: Ingest
echo ""
echo "--- Phase 1: Ingestion ---"
bash "$REPO_ROOT/scripts/ingest.sh"

# Step 2: Guide the user to run the 10-step workflow
echo ""
echo "======================================="
echo " Phase 2: Content Generation"
echo "======================================="
echo ""
echo "Ingestion complete. Now run the 10-step content workflow."
echo ""
echo "OPTION A — Antigravity:"
echo "  Open this repo in Antigravity. The .agent/ directory contains"
echo "  the full workflow (step-0 through step-10). Start with:"
echo "    call/step-0"
echo ""
echo "OPTION B — Claude Code (Agent Teams):"
echo "  Open this repo in Claude Code. The content-lead agent will"
echo "  orchestrate the team. Start with:"
echo "    @content-lead Start the content pipeline for [your topic]"
echo ""
echo "OPTION C — Claude Code (Solo):"
echo "  Open this repo in Claude Code and follow the steps manually."
echo "  Reference CLAUDE.md for instructions."
echo ""
echo "The knowledge ledger is available at:"
echo "  knowledge/latest-ledger.md"
echo ""
