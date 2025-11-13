# Simple Demo Structure

**Complete file listing of the simplified Python infrastructure demo**

---

## Directory Structure

```
simple/
│
├── .claude/                                    # AI Infrastructure
│   ├── skills/
│   │   ├── python-dev-guidelines/
│   │   │   ├── SKILL.md                       # Main Python skill
│   │   │   └── resources/
│   │   │       ├── api-patterns.md            # FastAPI patterns
│   │   │       ├── testing.md                 # pytest best practices
│   │   │       └── models.md                  # Pydantic models
│   │   └── skill-rules.json                   # Skill activation config
│   │
│   ├── agents/
│   │   ├── README.md                          # Agent usage guide
│   │   ├── code-reviewer.md                   # Code quality agent
│   │   ├── test-generator.md                  # Test generation agent
│   │   ├── error-debugger.md                  # Error debugging agent
│   │   └── documentation-writer.md            # Documentation agent
│   │
│   ├── hooks/
│   │   ├── skill-activation.sh                # Auto-activation hook
│   │   └── file-tracker.sh                    # File tracking hook
│   │
│   └── settings.json                           # Hook configuration
│
├── src/                                        # Python Application
│   ├── __init__.py
│   ├── api.py                                  # FastAPI routes
│   ├── models.py                               # Pydantic models
│   └── user_service.py                         # Service layer
│
├── tests/                                      # Test Suite
│   ├── __init__.py
│   └── test_user_service.py                    # Comprehensive tests
│
├── README.md                                   # Main documentation
├── DEMO_GUIDE.md                               # 5-minute demo walkthrough
├── STRUCTURE.md                                # This file
└── requirements.txt                            # Python dependencies
```

---

## File Count

**Infrastructure:**
- 1 Skill (with 3 resource files)
- 4 Agents
- 2 Hooks
- 2 Config files

**Application:**
- 3 Python modules
- 1 Test file
- 4 Documentation files

**Total:** 22 files

---

## What Each Component Does

### Skills (1 skill, 4 files)

**python-dev-guidelines/**
- `SKILL.md` - Main skill with quick reference
- `resources/api-patterns.md` - FastAPI best practices
- `resources/testing.md` - pytest strategies
- `resources/models.md` - Pydantic validation patterns

**Purpose:** Provides Python best practices automatically when working with .py files

---

### Agents (4 agents, 5 files)

1. **code-reviewer.md** - Reviews code for quality and best practices
2. **test-generator.md** - Generates comprehensive pytest tests
3. **error-debugger.md** - Debugs and fixes Python errors
4. **documentation-writer.md** - Creates documentation
5. **README.md** - Agent usage guide

**Purpose:** Handle complex development tasks autonomously

---

### Hooks (2 files)

1. **skill-activation.sh** - Detects context and suggests skills
2. **file-tracker.sh** - Logs file modifications

**Purpose:** Automate skill activation and maintain context

---

### Configuration (2 files)

1. **settings.json** - Hook configuration for Claude Code
2. **skill-rules.json** - Skill activation triggers

**Purpose:** Define when and how automation runs

---

### Python Application (4 files)

1. **api.py** - FastAPI application with user endpoints
   - POST /users - Create user
   - GET /users/{id} - Get user
   - GET /users - List users
   - PATCH /users/{id} - Update user
   - DELETE /users/{id} - Delete user
   - GET /health - Health check

2. **models.py** - Pydantic models for validation
   - UserCreate - User creation with password validation
   - UserResponse - User response without password
   - UserUpdate - Partial user updates
   - TaskCreate/TaskResponse - Example task models

3. **user_service.py** - Service layer with business logic
   - Custom exceptions (UserNotFoundError, UserAlreadyExistsError)
   - CRUD operations with validation
   - In-memory storage for demo

4. **__init__.py** - Package initialization

---

### Tests (2 files)

1. **test_user_service.py** - 17 comprehensive test cases
   - Happy path tests
   - Error case tests
   - Edge case tests
   - Update and delete tests

2. **__init__.py** - Test package initialization

---

### Documentation (4 files)

1. **README.md** - Complete guide to the demo
2. **DEMO_GUIDE.md** - 5-minute quick start
3. **STRUCTURE.md** - This file
4. **requirements.txt** - Python dependencies

---

## Key Features Demonstrated

### 1. Skill Auto-Activation
- Edit any .py file → skill suggests itself
- Use Python keywords → skill activates
- Zero manual invocation needed

### 2. Agent Specialization
- Code review with quality ratings
- Test generation with full coverage
- Error debugging with root cause analysis
- Documentation creation with examples

### 3. Best Practices Examples
- Type hints everywhere
- Custom exceptions
- Comprehensive docstrings
- Pydantic validation
- pytest fixtures and parametrize
- FastAPI dependency injection
- Proper error handling

### 4. Production Patterns
- Service layer architecture
- Request/response models
- Custom exceptions
- Arrange-Act-Assert testing
- REST API conventions

---

## Lines of Code

**Infrastructure:**
- Skills: ~1,200 lines
- Agents: ~800 lines
- Hooks: ~80 lines
- Config: ~40 lines

**Application:**
- Python code: ~450 lines
- Tests: ~280 lines
- Documentation: ~1,000 lines

**Total:** ~3,850 lines

---

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Read the documentation:**
   - Start with `README.md`
   - Try `DEMO_GUIDE.md` for quick start

3. **Experiment:**
   - Edit Python files and watch skills activate
   - Ask Claude to use agents
   - Run tests: `pytest tests/ -v`
   - Start API: `uvicorn src.api:app --reload`

---

## Extending the Demo

### Add More Skills
Copy from main showcase or create your own following the pattern

### Add More Agents
Duplicate an existing agent and customize the instructions

### Add More Hooks
Create custom hooks for your specific workflow needs

### Build More Features
The user service is just the start - add:
- Task management
- Authentication
- Database integration
- More endpoints

---

## What Makes This "Simple"?

Compared to the full showcase:
- ✅ 1 skill instead of 5
- ✅ 4 agents instead of 10
- ✅ 2 hooks instead of 6
- ✅ Working Python application
- ✅ No TypeScript/React complexity
- ✅ In-memory storage (no database)
- ✅ Focused on Python only

But still includes:
- ✅ Full skill auto-activation
- ✅ Complete agent workflow
- ✅ Production-ready patterns
- ✅ Comprehensive examples
- ✅ Ready to use immediately

---

## Next Steps

After mastering this demo:
1. Explore the full showcase for more skills and agents
2. Customize for your specific Python projects
3. Add domain-specific skills
4. Create custom agents for your workflow
5. Share your improvements!

---

**This is a complete, working demonstration of AI-assisted development infrastructure for Python.**
