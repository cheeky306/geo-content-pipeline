#!/bin/bash
# One-command setup for the GEO Content Pipeline
# Usage: bash scripts/setup.sh

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "======================================="
echo " GEO Content Pipeline — Setup"
echo "======================================="
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is required but not found."
    exit 1
fi

echo "Python: $(python3 --version)"

# Setup scraper
echo ""
echo "--- Setting up scraper ---"
bash "$REPO_ROOT/scraper/setup.sh"

# Verify directory structure
echo ""
echo "--- Verifying directories ---"
for dir in input input/downloads output/drafts output/knowledge-ledgers output/publishing-cards knowledge/brand; do
    if [ -d "$REPO_ROOT/$dir" ]; then
        echo "  OK: $dir/"
    else
        mkdir -p "$REPO_ROOT/$dir"
        echo "  Created: $dir/"
    fi
done

echo ""
echo "======================================="
echo " Setup complete!"
echo "======================================="
echo ""
echo "Next steps:"
echo "  1. Add URLs to input/urls.txt"
echo "  2. Drop PDFs/docs into input/downloads/"
echo "  3. Run: bash scripts/ingest.sh"
echo "  4. Run the 10-step pipeline in Antigravity or Claude Code"
echo ""
