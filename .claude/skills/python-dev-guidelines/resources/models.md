# Data Models and Validation

**Pydantic models and ORM patterns**

---

## Pydantic Models

```python
from pydantic import BaseModel, Field, EmailStr, validator
from datetime import datetime

class UserBase(BaseModel):
    """Base user model with common fields"""
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=100)

class UserCreate(UserBase):
    """Model for creating a user"""
    password: str = Field(..., min_length=8)

    @validator('password')
    def password_strength(cls, v):
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        return v

class UserResponse(UserBase):
    """Model for user responses (no password!)"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # For SQLAlchemy compatibility
```

---

## SQLAlchemy ORM Models

```python
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    posts = relationship("Post", back_populates="author")

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
```

---

## Key Patterns

### 1. Separate Request/Response Models
- **UserCreate**: For POST requests (includes password)
- **UserUpdate**: For PATCH requests (optional fields)
- **UserResponse**: For responses (excludes password)

### 2. Use Validators for Complex Validation
```python
@validator('email')
def email_must_be_company_domain(cls, v):
    if not v.endswith('@company.com'):
        raise ValueError('Must use company email')
    return v.lower()
```

### 3. Use Field for Constraints
```python
class Product(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    price: float = Field(..., gt=0, description="Price must be positive")
    quantity: int = Field(default=0, ge=0)
```

### 4. Use Config for ORM Compatibility
```python
class Config:
    from_attributes = True  # Convert SQLAlchemy models to Pydantic
    json_encoders = {
        datetime: lambda v: v.isoformat()
    }
```
