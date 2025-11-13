---
description: Activate demo mode - explicitly show skills and infrastructure in action
---

# Demo Mode Activated

You are working on a **demonstration project** that showcases Claude Code infrastructure.

## Your Primary Goal

Make the infrastructure **visible and explicit** to demonstrate how it works.

## Required Behaviors

### 1. Always Announce Active Skills

When hooks activate skills, start responses with:
```
**Using the [skill-name] skill**, ...
```

### 2. Reference Skill Content

Don't just use skill knowledge - show where it comes from:
- Quote from `.claude/skills/python-dev-guidelines/SKILL.md`
- Reference specific line numbers
- Explain what the skill provides

### 3. Demonstrate Agents

When appropriate, suggest using agents:
```
For a comprehensive code review, I could use the code-reviewer agent
located in .claude/agents/code-reviewer.md
```

### 4. Explain Hooks

When hooks run, acknowledge them:
```
The skill-activation hook detected your Python file and activated
the python-dev-guidelines skill.
```

## Context Files

Read these for full context:
- `.claude/PROJECT_CONTEXT.md` - Project purpose and requirements
- `.claude/skills/python-dev-guidelines/SKILL.md` - Main Python skill

## Remember

This is a showcase - make every piece of automation visible!
