#!/bin/bash
# Haandshake Content Copilot Process

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATES="$SKILL_DIR/resources/templates.json"
PROMPTS="$SKILL_DIR/scripts/haandshake_prompts.md"

# Load prompts and execute workflow
echo "Haandshake Content Copilot initialized"
echo "Using templates: $TEMPLATES"
echo "Using prompts: $PROMPTS"
```

**Final structure:**
```
/skills/content-agent/
  ├── SKILL.md (Haandshake documentation)
  ├── resources/
  │   └── templates.json (Haandshake templates)
  ├── scripts/
  │   ├── process.sh (execution)
  │   └── haandshake_prompts.md (workflow prompts)
  └── /workflows/
      ├── step-0.md through step-10.md (already in place)