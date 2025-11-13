#!/bin/bash
#
# File Tracker Hook (Simplified)
# Tracks file modifications to maintain context
#

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
CONTEXT_FILE="$PROJECT_DIR/.claude/.file-context.txt"

# Get tool use info from environment
TOOL_NAME="${CLAUDE_TOOL_NAME:-}"
TOOL_ARGS="${CLAUDE_TOOL_ARGS:-}"

# Track file modifications
if [ "$TOOL_NAME" = "Edit" ] || [ "$TOOL_NAME" = "Write" ]; then
    # Extract file path from tool args (simplified parsing)
    FILE_PATH=$(echo "$TOOL_ARGS" | grep -o '"file_path":"[^"]*"' | cut -d'"' -f4)

    if [ -n "$FILE_PATH" ]; then
        # Log the modification with timestamp
        echo "[$(date '+%Y-%m-%d %H:%M:%S')] Modified: $FILE_PATH" >> "$CONTEXT_FILE"

        # Keep only last 50 entries
        tail -n 50 "$CONTEXT_FILE" > "$CONTEXT_FILE.tmp" && mv "$CONTEXT_FILE.tmp" "$CONTEXT_FILE"
    fi
fi

exit 0
