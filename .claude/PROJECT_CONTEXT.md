# Project Context: Claude Code Infrastructure Demo

**IMPORTANT: Read this at the start of every session!**

---

## What This Project Is

This is a **demonstration project** showcasing Claude Code's infrastructure capabilities:
- Skills (contextual knowledge bases)
- Agents (specialized workers)
- Hooks (automation triggers)

The primary purpose is to **show how these features work**, not just to build a Python application.

---

## Critical Behavior Requirements

### 1. Always Announce Skill Usage

When a skill activates (indicated by hook messages), you MUST:

✅ **Start your response with:**
```
**Using the [skill-name] skill**, let me [task description]...
```

✅ **Reference the skill explicitly:**
- Mention which skill file you're following
- Quote specific guidelines from the skill
- Show the connection between skill content and your advice

❌ **Don't just passively use skill knowledge** - make it visible!

### 2. Make Infrastructure Visible

Since this is a demo:
- Call out when hooks run
- Explain what skills provide
- Demonstrate agent capabilities
- Show the automation in action

### 3. Example of Correct Behavior

**User:** "Review this Python code"
**Hook Output:** "📚 SKILL ACTIVATED: python-dev-guidelines"

**Your Response Should Be:**
```
**Using the python-dev-guidelines skill**, let me review this code
against our established best practices.

According to the skill's guidelines (.claude/skills/python-dev-guidelines/SKILL.md):
- ✅ Type hints are required (line 42 of SKILL.md)
- ✅ Custom exceptions improve error handling (line 58-68)
- ✅ Docstrings should explain the "why"

Your code in src/user_service.py:
[specific feedback]
```

---

## Active Skills

- **python-dev-guidelines**: Activates for .py files and Python-related prompts
  - Location: `.claude/skills/python-dev-guidelines/SKILL.md`
  - Resources: api-patterns.md, testing.md, models.md

---

## Available Agents

Located in `.claude/agents/`:
- `code-reviewer.md` - Code quality review
- `test-generator.md` - Generate pytest tests
- `error-debugger.md` - Debug errors
- `documentation-writer.md` - Create documentation

---

## Remember

This project exists to **demonstrate the infrastructure**, so always make the
automation and intelligence visible to the user!
