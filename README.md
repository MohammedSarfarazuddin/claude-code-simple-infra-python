# Simple Python AI Infrastructure Demo

**A minimal, working example of AI-assisted development infrastructure for Python projects.**

---

## What's This?

This is a simplified, ready-to-use demonstration of how AI agents, skills, and hooks work together to enhance Python development. This is a **working example** you can actually run and experiment with.

---

## What's Included

### .claude/ Infrastructure

```
.claude/
├── skills/
│   └── python-dev-guidelines/     # Python best practices skill
│       ├── SKILL.md               # Main skill file
│       └── resources/             # Deep-dive topics
│           ├── api-patterns.md
│           ├── testing.md
│           └── models.md
├── agents/
│   ├── code-reviewer.md           # Reviews code quality
│   ├── test-generator.md          # Generates pytest tests
│   ├── error-debugger.md          # Debugs errors
│   └── documentation-writer.md    # Creates documentation
├── hooks/
│   ├── skill-activation.sh        # Auto-activates skills
│   └── file-tracker.sh            # Tracks file changes
├── settings.json                   # Hook configuration
└── skills/skill-rules.json        # Skill activation rules
```

### Example Python Application

A simple FastAPI user management API demonstrating best practices:

```
src/
├── api.py              # FastAPI routes with proper error handling
├── user_service.py     # Service layer with custom exceptions
└── models.py           # Pydantic models with validation

tests/
└── test_user_service.py  # Comprehensive pytest tests
```

---

## Quick Start

### 1. Install Dependencies

```bash
cd simple
pip install fastapi pydantic pytest
```

### 2. Try the Demo

**Option A: Edit a Python file**
- Open `src/user_service.py` in your editor
- Ask Claude: "Review this code"
- The `python-dev-guidelines` skill should auto-activate!

**Option B: Run tests**
```bash
pytest tests/test_user_service.py -v
```

**Option C: Start the API**
```bash
uvicorn src.api:app --reload
# Visit http://localhost:8000/docs for API documentation
```

---

## How It Works

### 1. Skill Auto-Activation

When you work with `.py` files, the skill automatically activates:

```
You open: src/api.py
   ↓
Hook detects: .py file
   ↓
Skill activates: python-dev-guidelines
   ↓
Claude suggests: "The python-dev-guidelines skill may be helpful"
   ↓
You get: Automatic best practices guidance
```

### 2. Agent Invocation

Ask Claude to use specific agents for complex tasks:

```bash
# Code review
"Use the code-reviewer agent to review my API routes"

# Generate tests
"Use the test-generator agent to create tests for user_service.py"

# Debug errors
"Use the error-debugger agent to fix this ValueError"

# Create documentation
"Use the documentation-writer agent to document the API"
```

### 3. File Tracking

Every time you edit a file, the `file-tracker` hook logs it:

```
[2025-01-13 10:15:23] Modified: src/api.py
[2025-01-13 10:16:45] Modified: src/user_service.py
[2025-01-13 10:18:12] Modified: tests/test_user_service.py
```

This helps Claude understand your active context.

---

## Demo Scenarios

### Scenario 1: Code Review

```
You: "Review the user service code for best practices"

Claude:
1. Loads python-dev-guidelines skill
2. Reviews src/user_service.py
3. Checks for:
   - Type hints ✅
   - Error handling ✅
   - Docstrings ✅
   - Custom exceptions ✅
4. Provides feedback
```

### Scenario 2: Generate Tests

```
You: "Create comprehensive tests for the API routes"

Claude:
1. Uses test-generator agent
2. Analyzes src/api.py
3. Generates tests for:
   - Happy paths
   - Error cases
   - Edge cases
4. Creates complete test file
```

### Scenario 3: Fix a Bug

```
You: "I'm getting a ValueError when creating users"

Claude:
1. Uses error-debugger agent
2. Reads error traceback
3. Analyzes root cause
4. Proposes fix with explanation
5. Implements the fix
```

---

## What Triggers the Skill?

The `python-dev-guidelines` skill activates when:

**File patterns:**
- Working with `.py` files
- Editing files in `src/` or `tests/`

**Keywords in your prompts:**
- "python", "fastapi", "flask"
- "pytest", "test", "testing"
- "api", "endpoint", "route"
- "model", "validation", "pydantic"

**Code patterns:**
- Files containing `from fastapi import`
- Files containing `def test_`
- Files containing Pydantic models

---

## Customizing for Your Project

### Add More Skills

```bash
# Copy from the main showcase
cp -r ../claude-code-infrastructure-showcase/.claude/skills/your-skill \
      .claude/skills/

# Update skill-rules.json to add triggers
```

### Modify Skill Triggers

Edit `.claude/skills/skill-rules.json`:

```json
{
  "skills": {
    "python-dev-guidelines": {
      "promptTriggers": {
        "keywords": [
          "your",
          "custom",
          "keywords"
        ]
      },
      "fileTriggers": {
        "pathPatterns": [
          "your/custom/path/**/*.py"
        ]
      }
    }
  }
}
```

### Create Custom Agents

Copy an existing agent and modify:

```bash
cp .claude/agents/code-reviewer.md .claude/agents/my-custom-agent.md
# Edit my-custom-agent.md with your specific instructions
```

---

## Example Interactions

### Getting Type Hints Guidance

```
You: "Add type hints to this function"
     [editing src/api.py]

Claude: "📚 Skill Suggestion: The python-dev-guidelines skill may be helpful"

Claude: Based on Python best practices, here's the properly typed function:

def create_user(user_data: UserCreate) -> UserResponse:
    """Create a new user"""
    # implementation...
```

### Testing Best Practices

```
You: "How should I structure these tests?"
     [editing tests/test_user_service.py]

Claude: "📚 Skill Suggestion: The python-dev-guidelines skill may be helpful"

Claude: Following pytest best practices from the python-dev-guidelines:

1. Use fixtures for setup
2. Follow Arrange-Act-Assert pattern
3. Test happy path, edge cases, and errors
4. Use descriptive test names

Here's the recommended structure...
```

---

## Understanding the Infrastructure

### Skills = Contextual Guidance

- **What:** Modular knowledge bases with best practices
- **When:** Auto-activate based on context
- **How:** Hooks detect patterns and suggest skills
- **Example:** Python guidelines when editing .py files

### Agents = Specialized Workers

- **What:** Autonomous AI instances for complex tasks
- **When:** Manually invoked for specific jobs
- **How:** Claude launches them with specific instructions
- **Example:** Code reviewer agent for quality analysis

### Hooks = Automation Triggers

- **What:** Shell scripts that run at workflow events
- **When:** On prompt submit, after file edits, etc.
- **How:** Monitor activity and augment AI behavior
- **Example:** Skill activation based on file patterns

---

## Troubleshooting

### Skill Not Activating?

**Check:**
1. Is the hook executable?
   ```bash
   ls -la .claude/hooks/*.sh
   ```
2. Is settings.json configured?
   ```bash
   cat .claude/settings.json
   ```
3. Do file patterns match?
   ```bash
   cat .claude/skills/skill-rules.json
   ```

### Agent Not Found?

**Check:**
```bash
ls -la .claude/agents/
```

All agents should be `.md` files.

### Hooks Not Running?

Make them executable:
```bash
chmod +x .claude/hooks/*.sh
```

---

## Next Steps

1. **Experiment:** Edit Python files and watch skills activate
2. **Try Agents:** Ask Claude to use different agents
3. **Customize:** Modify skill triggers for your workflow
4. **Expand:** Copy more skills/agents from main showcase

---

## Key Files to Explore

| File | Purpose | Try This |
|------|---------|----------|
| `src/api.py` | FastAPI routes | Ask for code review |
| `src/user_service.py` | Service layer | Ask to generate tests |
| `tests/test_user_service.py` | Test suite | Ask to run tests |
| `.claude/skills/python-dev-guidelines/SKILL.md` | Main skill | Read best practices |
| `.claude/agents/code-reviewer.md` | Reviewer agent | Ask to review code |

---

## Requirements

```
fastapi>=0.104.0
pydantic>=2.0.0
pytest>=7.0.0
```

---

## License

MIT - Use freely in your projects

---

## Learn More

This is a simplified version of the full infrastructure showcase. See the main README for:
- More skills (backend, frontend, testing)
- More agents (10 total)
- Advanced hooks
- Complete documentation
