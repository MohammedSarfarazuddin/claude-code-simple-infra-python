# Agents

**4 specialized agents for Python development**

---

## Available Agents

### code-reviewer.md
**Purpose:** Review Python code for best practices and potential issues

**Use when:**
- After implementing new features
- Before creating pull requests
- Need quality assessment

**Invoke:**
```
"Use the code-reviewer agent to review [file/module]"
```

---

### test-generator.md
**Purpose:** Generate comprehensive pytest tests

**Use when:**
- Need tests for new code
- Want better coverage
- Testing edge cases

**Invoke:**
```
"Use the test-generator agent to create tests for [file/function]"
```

---

### error-debugger.md
**Purpose:** Debug and fix Python errors

**Use when:**
- Encountering runtime errors
- Tests are failing
- Need help finding root cause

**Invoke:**
```
"Use the error-debugger agent to fix [error description]"
```

---

### documentation-writer.md
**Purpose:** Create comprehensive documentation

**Use when:**
- Need API documentation
- Creating README files
- Documenting new features

**Invoke:**
```
"Use the documentation-writer agent to document [module/feature]"
```

---

## How to Use Agents

Just ask Claude to use them:

```
"Use the code-reviewer agent to review src/api.py"
"Use the test-generator agent to create tests for user_service"
"Use the error-debugger agent to debug this ValueError"
"Use the documentation-writer agent to document the API"
```

Claude will launch the agent and return comprehensive results.
