"""
Data models for the application.
This file demonstrates Pydantic models for API request/response validation.
"""

from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    """Base user model with common fields"""
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=100)


class UserCreate(UserBase):
    """Model for creating a new user"""
    password: str = Field(..., min_length=8)

    @validator('password')
    def password_must_be_strong(cls, v):
        """Validate password strength"""
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError('Password must contain at least one uppercase letter')
        return v


class UserResponse(UserBase):
    """Model for user API responses (excludes password)"""
    id: int
    created_at: datetime
    is_active: bool = True

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    """Model for updating user information"""
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None


class TaskCreate(BaseModel):
    """Model for creating a task"""
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    priority: int = Field(default=1, ge=1, le=5)


class TaskResponse(TaskCreate):
    """Model for task API responses"""
    id: int
    user_id: int
    completed: bool = False
    created_at: datetime

    class Config:
        from_attributes = True
