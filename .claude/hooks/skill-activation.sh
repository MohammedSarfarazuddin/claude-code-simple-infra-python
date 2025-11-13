#!/bin/bash
#
# Skill Activation Hook (Simplified)
# Automatically suggests relevant skills based on user prompt and file context
#

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
SKILL_RULES="$PROJECT_DIR/.claude/skills/skill-rules.json"

# Get user prompt from stdin
USER_PROMPT=$(cat)

# Get working files from environment if available
WORKING_FILES="${CLAUDE_WORKING_FILES:-}"

# Simple skill matching logic
suggest_skills() {
    local suggested_skills=""

    # Check if working with Python files
    if echo "$WORKING_FILES" | grep -q "\.py"; then
        suggested_skills="python-dev-guidelines"
    fi

    # Check for Python-related keywords in prompt
    if echo "$USER_PROMPT" | grep -qiE "python|fastapi|flask|pytest|pydantic"; then
        suggested_skills="python-dev-guidelines"
    fi

    # Check for testing keywords
    if echo "$USER_PROMPT" | grep -qiE "test|testing|pytest"; then
        suggested_skills="python-dev-guidelines"
    fi

    # Output suggestion if skill should activate
    if [ -n "$suggested_skills" ]; then
        echo "📚 SKILL ACTIVATED: python-dev-guidelines"
        echo ""
        echo "IMPORTANT: This is a demo project showcasing Claude Code infrastructure."
        echo "You MUST explicitly announce that you are using the '$suggested_skills' skill."
        echo "Start your response with: '**Using the python-dev-guidelines skill**, ...'"
        echo "Reference specific sections from .claude/skills/python-dev-guidelines/SKILL.md when applicable."
        echo ""
    fi
}

# Run suggestion logic
suggest_skills

# Pass through the original prompt
echo "$USER_PROMPT"
