# Testing Strategies with pytest

**Best practices for Python testing**

---

## Test Structure

```python
# tests/test_user_service.py
import pytest
from src.services.user_service import UserService
from src.models import User

class TestUserService:
    """Tests for UserService"""

    @pytest.fixture
    def user_service(self):
        """Provide a UserService instance for tests"""
        return UserService()

    @pytest.fixture
    def sample_user(self):
        """Provide sample user data"""
        return {
            "email": "test@example.com",
            "name": "Test User"
        }

    def test_create_user_success(self, user_service, sample_user):
        """Test successful user creation"""
        # Arrange
        email = sample_user["email"]
        name = sample_user["name"]

        # Act
        user = user_service.create_user(email=email, name=name)

        # Assert
        assert user.email == email
        assert user.name == name
        assert user.id is not None

    def test_create_user_duplicate_email(self, user_service, sample_user):
        """Test that creating duplicate user raises error"""
        # Arrange
        user_service.create_user(**sample_user)

        # Act & Assert
        with pytest.raises(ValueError, match="User already exists"):
            user_service.create_user(**sample_user)
```

---

## Key Patterns

### 1. Use Fixtures for Reusable Setup
```python
@pytest.fixture
def db_session():
    """Provide a test database session"""
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        session.close()
```

### 2. Follow Arrange-Act-Assert Pattern
```python
def test_calculate_total():
    # Arrange: Set up test data
    items = [{"price": 10}, {"price": 20}]
    tax_rate = 0.1

    # Act: Execute the function
    total = calculate_total(items, tax_rate)

    # Assert: Verify the result
    assert total == 33.0  # (10 + 20) * 1.1
```

### 3. Use Descriptive Test Names
- Good: `test_create_user_with_duplicate_email_raises_error`
- Bad: `test_user_creation`

### 4. Test Edge Cases
```python
def test_calculate_total_with_empty_list():
    """Test with empty items list"""
    assert calculate_total([], 0.1) == 0.0

def test_calculate_total_with_zero_tax():
    """Test with no tax"""
    items = [{"price": 10}]
    assert calculate_total(items, 0.0) == 10.0
```

### 5. Mock External Dependencies
```python
from unittest.mock import Mock, patch

def test_send_email(mocker):
    """Test email sending with mocked SMTP"""
    mock_smtp = mocker.patch('smtplib.SMTP')

    send_welcome_email("user@example.com")

    mock_smtp.assert_called_once()
```
