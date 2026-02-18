#!/bin/bash
# Ingest sources from input/ and produce knowledge ledgers
# Usage: bash scripts/ingest.sh

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRAPER_DIR="$REPO_ROOT/scraper"
INPUT_DIR="$REPO_ROOT/input"
OUTPUT_DIR="$REPO_ROOT/output/knowledge-ledgers"
KNOWLEDGE_DIR="$REPO_ROOT/knowledge"

echo "======================================="
echo " GEO Content Pipeline — Ingest"
echo "======================================="
echo ""

# Check venv exists
if [ ! -d "$SCRAPER_DIR/.venv" ]; then
    echo "Error: Scraper not set up. Run: bash scripts/setup.sh"
    exit 1
fi

# Activate venv
source "$SCRAPER_DIR/.venv/bin/activate"

# Build CLI arguments
ARGS=""

# Read URLs from urls.txt (skip comments and blank lines)
URL_FILE="$INPUT_DIR/urls.txt"
if [ -f "$URL_FILE" ]; then
    URLS=$(grep -v '^#' "$URL_FILE" | grep -v '^$' | tr '\n' ' ')
    if [ -n "$URLS" ]; then
        ARGS="$ARGS --urls $URLS"
        echo "URLs found: $(echo $URLS | wc -w | tr -d ' ')"
    fi
fi

# Check for documents in downloads/
DOWNLOAD_DIR="$INPUT_DIR/downloads"
if [ -d "$DOWNLOAD_DIR" ] && [ "$(ls -A "$DOWNLOAD_DIR" 2>/dev/null)" ]; then
    ARGS="$ARGS --folder $DOWNLOAD_DIR"
    echo "Documents found in: $DOWNLOAD_DIR"
fi

# Validate we have something to process
if [ -z "$ARGS" ]; then
    echo ""
    echo "Nothing to ingest. Add sources first:"
    echo "  - URLs:      Add to input/urls.txt (one per line)"
    echo "  - Documents:  Drop into input/downloads/"
    exit 0
fi

# Generate timestamp for output
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
OUTPUT_FILE="$OUTPUT_DIR/ledger-$TIMESTAMP.md"

echo ""
echo "Running Knowledge Ledger Agent..."
echo ""

# Run the scraper
cd "$SCRAPER_DIR"
python3 knowledge_ledger_agent.py $ARGS --output "$OUTPUT_FILE"

# Copy latest ledger to knowledge/ for the content pipeline
LATEST_LINK="$KNOWLEDGE_DIR/latest-ledger.md"
cp "$OUTPUT_FILE" "$LATEST_LINK"

echo ""
echo "======================================="
echo " Ingestion complete!"
echo "======================================="
echo "  Ledger:  $OUTPUT_FILE"
echo "  Latest:  $LATEST_LINK"
echo ""
echo "Next: Run the content pipeline using Antigravity or Claude Code."
echo ""
