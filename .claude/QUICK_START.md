# Quick Start: Ensuring Claude Uses Skills Explicitly

## The Problem
Skills can activate silently - Claude uses the knowledge but doesn't announce it.

## The Solution
We've implemented **three layers** to ensure visibility:

---

## 1. Enhanced Hook (Automatic)

**Location:** `.claude/hooks/skill-activation.sh`

The hook now outputs explicit instructions:
```
📚 SKILL ACTIVATED: python-dev-guidelines

IMPORTANT: This is a demo project showcasing Claude Code infrastructure.
You MUST explicitly announce that you are using the 'python-dev-guidelines' skill.
Start your response with: '**Using the python-dev-guidelines skill**, ...'
```

**When it triggers:** Automatically when you work with `.py` files

---

## 2. Project Context File (Manual Read)

**Location:** `.claude/PROJECT_CONTEXT.md`

At the start of a new session, ask Claude:
```
Please read @.claude/PROJECT_CONTEXT.md to understand this demo project
```

This file explains:
- This is a demo project
- Skills must be announced explicitly
- How to reference skill content
- Examples of correct behavior

---

## 3. Demo Mode Slash Command (Quick Reminder)

**Usage:** `/demo-mode`

Use this anytime in a session to remind Claude to make infrastructure visible.

---

## Recommended Workflow

### Starting a New Session

```bash
# 1. Start Claude Code
claude-code

# 2. Remind about demo mode
/demo-mode

# 3. Or manually ask
Please read @.claude/PROJECT_CONTEXT.md - this is a demo project
```

### During the Session

Just work normally! The hook will:
1. Detect Python files
2. Activate the skill
3. Instruct Claude to announce it

### If Claude Forgets

Simply type:
```
/demo-mode
```

---

## Testing the Setup

Try this:
1. Open `src/user_service.py`
2. Ask: "What are the Python best practices for this file?"
3. Watch for: **"Using the python-dev-guidelines skill"** in the response

---

## What Success Looks Like

**Good Response:**
> **Using the python-dev-guidelines skill**, let me review your code.
>
> According to the skill's guidelines (.claude/skills/python-dev-guidelines/SKILL.md),
> line 42 emphasizes always using type hints...

**Bad Response:**
> Here are some Python best practices for this file:
> - Use type hints
> - Add docstrings
> ...

---

## Files Created

- ✅ `.claude/hooks/skill-activation.sh` (enhanced)
- ✅ `.claude/PROJECT_CONTEXT.md` (project context)
- ✅ `.claude/commands/demo-mode.md` (slash command)
- ✅ `.claude/QUICK_START.md` (this file)
