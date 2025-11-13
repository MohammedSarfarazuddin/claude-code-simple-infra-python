# Quick Demo Guide

**5-minute walkthrough of AI infrastructure in action**

---

## Setup (1 minute)

```bash
cd simple
pip install -r requirements.txt
```

---

## Demo 1: Skill Auto-Activation (1 minute)

**What to do:**
1. Open `src/user_service.py` in your editor
2. Ask Claude: "What are the Python best practices in this file?"

**What happens:**
- Hook detects you're working with a `.py` file
- `python-dev-guidelines` skill auto-activates
- Claude references the skill automatically
- You get context-aware guidance

**Look for:**
```
📚 Skill Suggestion: The python-dev-guidelines skill may be helpful for this task.
```

---

## Demo 2: Use an Agent (2 minutes)

**What to do:**
Ask Claude: "Use the code-reviewer agent to review src/api.py"

**What happens:**
- Claude launches the code-reviewer agent
- Agent reads the API file
- Analyzes for best practices
- Returns comprehensive review

**You'll get:**
- Overall quality rating
- Critical/important/minor issues
- Specific recommendations
- Code examples for fixes

---

## Demo 3: Generate Tests (2 minutes)

**What to do:**
Ask Claude: "Use the test-generator agent to create tests for the create_user endpoint in api.py"

**What happens:**
- Claude launches test-generator agent
- Agent analyzes the endpoint
- Generates comprehensive tests
- Follows pytest best practices

**You'll get:**
- Happy path tests
- Error case tests
- Edge case tests
- Proper fixtures and parametrization

---

## Demo 4: Run Everything

**Run tests:**
```bash
pytest tests/test_user_service.py -v
```

**Start API:**
```bash
uvicorn src.api:app --reload
```

**Visit docs:**
```
http://localhost:8000/docs
```

**Try API:**
```bash
# Create user
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","name":"Test User","password":"Test1234"}'

# Get user
curl http://localhost:8000/users/1

# List users
curl http://localhost:8000/users
```

---

## What You Just Saw

### 1. Automatic Skill Activation
- No manual invocation needed
- Context-aware suggestions
- Always available guidance

### 2. Specialized Agents
- Complex tasks handled autonomously
- Systematic, thorough analysis
- Professional-quality output

### 3. Working Code
- Real FastAPI application
- Comprehensive tests
- Production-ready patterns

---

## Key Takeaways

**Skills:**
- Auto-activate based on file patterns
- Provide inline guidance
- Always available in background

**Agents:**
- Manually invoked for specific tasks
- Handle complex multi-step work
- Return comprehensive results

**Hooks:**
- Run automatically at events
- Enable skill auto-activation
- Track context transparently

---

## Try These Next

1. **Ask for refactoring:**
   - "Refactor the user_service.py to use dependency injection"

2. **Request documentation:**
   - "Use the documentation-writer agent to create API docs"

3. **Debug an error:**
   - Introduce a bug, then: "Use the error-debugger agent to fix this"

4. **Generate more tests:**
   - "Create integration tests for the API endpoints"

---

## Questions to Explore

**For Skills:**
- "What are the Python best practices for error handling?"
- "How should I structure Pydantic models?"
- "What testing patterns should I follow?"

**For Agents:**
- "Review all my code for security issues"
- "Generate tests for the entire service layer"
- "Create comprehensive documentation"

---

## Experiment!

The infrastructure is set up and ready. Try:

1. Creating new endpoints in `api.py`
2. Adding new methods to `user_service.py`
3. Writing new test cases
4. Asking for code reviews
5. Generating documentation

Watch how skills auto-activate and agents help with complex tasks!
