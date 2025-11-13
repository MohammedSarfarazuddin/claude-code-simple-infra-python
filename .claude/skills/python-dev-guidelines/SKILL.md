---
name: python-dev-guidelines
description: Python development best practices and patterns
version: 1.0.0
---

# Python Development Guidelines

**Purpose:** Provide best practices for Python development including code organization, type hints, error handling, and testing.

---

## When to Use This Skill

This skill automatically activates when:
- Working with `.py` files
- Discussing Python code patterns
- Creating APIs with Flask/FastAPI
- Writing tests with pytest
- Implementing data models

---

## Quick Reference

### Code Organization

```python
# Good: Clear module structure
src/
  api/
    routes.py
    models.py
  services/
    user_service.py
  utils/
    helpers.py
tests/
  test_user_service.py
```

### Type Hints (Always use them!)

```python
# Good
def calculate_total(items: list[dict], tax_rate: float) -> float:
    subtotal = sum(item["price"] for item in items)
    return subtotal * (1 + tax_rate)

# Bad
def calculate_total(items, tax_rate):
    subtotal = sum(item["price"] for item in items)
    return subtotal * (1 + tax_rate)
```

### Error Handling

```python
# Good: Specific exceptions
class UserNotFoundError(Exception):
    """Raised when a user cannot be found"""
    pass

def get_user(user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise UserNotFoundError(f"User {user_id} not found")
    return user

# Bad: Generic exceptions
def get_user(user_id):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise Exception("Not found")
    return user
```

---

## Resource Files

For detailed guidance on specific topics:

- **[API Development](resources/api-patterns.md)** - Flask/FastAPI patterns
- **[Testing Strategies](resources/testing.md)** - pytest best practices
- **[Data Models](resources/models.md)** - Pydantic and ORM patterns

---

## Key Principles

1. **Always use type hints** - They catch bugs and improve IDE support
2. **Write descriptive docstrings** - Explain the "why", not the "what"
3. **Keep functions small** - Single responsibility principle
4. **Use custom exceptions** - Better error handling and debugging
5. **Test thoroughly** - Aim for 80%+ coverage on business logic

---

## Common Pitfalls to Avoid

❌ **Mutable default arguments**
```python
# Bad
def add_item(item, items=[]):
    items.append(item)
    return items

# Good
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

❌ **Catching all exceptions**
```python
# Bad
try:
    process_data()
except:
    pass

# Good
try:
    process_data()
except ValueError as e:
    logger.error(f"Invalid data: {e}")
    raise
```

❌ **Not using context managers**
```python
# Bad
file = open("data.txt")
data = file.read()
file.close()

# Good
with open("data.txt") as file:
    data = file.read()
```

---

## Next Steps

When implementing Python code:
1. Start with type hints
2. Write docstrings
3. Implement core logic
4. Add error handling
5. Write tests
6. Run linting (ruff, mypy)
