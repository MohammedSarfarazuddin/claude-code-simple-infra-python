"""
FastAPI application with user management endpoints.
This file demonstrates API route patterns with proper error handling.
"""

from fastapi import FastAPI, HTTPException, status
from typing import List

from models import UserCreate, UserResponse, UserUpdate
from user_service import UserService, UserNotFoundError, UserAlreadyExistsError

# Initialize FastAPI app
app = FastAPI(
    title="User Management API",
    description="Simple API demonstrating Python best practices",
    version="1.0.0"
)

# Initialize service (in production, use dependency injection)
user_service = UserService()


@app.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["users"]
)
async def create_user(user_data: UserCreate) -> UserResponse:
    """
    Create a new user.

    Args:
        user_data: User creation data including email, name, and password

    Returns:
        Created user information (excluding password)

    Raises:
        HTTPException: 400 if user already exists
    """
    try:
        user = user_service.create_user(
            email=user_data.email,
            name=user_data.name
        )
        return UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            created_at=user.created_at,
            is_active=user.is_active
        )
    except UserAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@app.get(
    "/users/{user_id}",
    response_model=UserResponse,
    tags=["users"]
)
async def get_user(user_id: int) -> UserResponse:
    """
    Get a user by ID.

    Args:
        user_id: The user's ID

    Returns:
        User information

    Raises:
        HTTPException: 404 if user not found
    """
    try:
        user = user_service.get_user(user_id)
        return UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            created_at=user.created_at,
            is_active=user.is_active
        )
    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@app.get(
    "/users",
    response_model=List[UserResponse],
    tags=["users"]
)
async def list_users(active_only: bool = False) -> List[UserResponse]:
    """
    List all users.

    Args:
        active_only: If true, only return active users

    Returns:
        List of users
    """
    users = user_service.list_users(active_only=active_only)
    return [
        UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            created_at=user.created_at,
            is_active=user.is_active
        )
        for user in users
    ]


@app.patch(
    "/users/{user_id}",
    response_model=UserResponse,
    tags=["users"]
)
async def update_user(user_id: int, user_data: UserUpdate) -> UserResponse:
    """
    Update user information.

    Args:
        user_id: The user's ID
        user_data: Fields to update

    Returns:
        Updated user information

    Raises:
        HTTPException: 404 if user not found
        HTTPException: 400 if email already in use
    """
    try:
        user = user_service.update_user(
            user_id=user_id,
            name=user_data.name,
            email=user_data.email,
            is_active=user_data.is_active
        )
        return UserResponse(
            id=user.id,
            email=user.email,
            name=user.name,
            created_at=user.created_at,
            is_active=user.is_active
        )
    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except UserAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["users"]
)
async def delete_user(user_id: int) -> None:
    """
    Delete a user.

    Args:
        user_id: The user's ID

    Raises:
        HTTPException: 404 if user not found
    """
    try:
        user_service.delete_user(user_id)
    except UserNotFoundError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
