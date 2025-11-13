@"""
User service layer.
This file demonstrates service layer patterns with proper error handling.
"""

from typing import Optional, List
from datetime import datetime


class UserNotFoundError(Exception):
    """Raised when a user cannot be found"""
    pass


class UserAlreadyExistsError(Exception):
    """Raised when attempting to create a user that already exists"""
    pass


class User:
    """Simple User class for demonstration"""

    def __init__(
        self,
        email: str,
        name: str,
        id: Optional[int] = None,
        created_at: Optional[datetime] = None,
        is_active: bool = True
    ):
        self.id = id
        self.email = email
        self.name = name
        self.created_at = created_at or datetime.utcnow()
        self.is_active = is_active


class UserService:
    """
    Service for managing user operations.

    This demonstrates the service layer pattern with:
    - Clear separation of concerns
    - Custom exceptions for better error handling
    - Type hints for all methods
    - Comprehensive docstrings
    """

    def __init__(self):
        """Initialize the user service with in-memory storage"""
        self._users: dict[int, User] = {}
        self._next_id = 1
        self._email_index: dict[str, int] = {}

    def create_user(self, email: str, name: str) -> User:
        """
        Create a new user.

        Args:
            email: User's email address (must be unique)
            name: User's full name

        Returns:
            Created User object

        Raises:
            UserAlreadyExistsError: If email already exists
            ValueError: If email or name is invalid
        """
        # Validate input
        if not email or not name:
            raise ValueError("Email and name are required")

        # Check for duplicate email
        if email.lower() in self._email_index:
            raise UserAlreadyExistsError(f"User with email {email} already exists")

        # Create user
        user = User(
            id=self._next_id,
            email=email,
            name=name
        )

        # Store user
        self._users[self._next_id] = user
        self._email_index[email.lower()] = self._next_id
        self._next_id += 1

        return user

    def get_user(self, user_id: int) -> User:
        """
        Get a user by ID.

        Args:
            user_id: The user's ID

        Returns:
            User object

        Raises:
            UserNotFoundError: If user doesn't exist
        """
        user = self._users.get(user_id)
        if not user:
            raise UserNotFoundError(f"User with ID {user_id} not found")
        return user

    def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Get a user by email address.

        Args:
            email: The user's email

        Returns:
            User object if found, None otherwise
        """
        user_id = self._email_index.get(email.lower())
        if user_id is None:
            return None
        return self._users.get(user_id)

    def list_users(self, active_only: bool = False) -> List[User]:
        """
        List all users.

        Args:
            active_only: If True, only return active users

        Returns:
            List of User objects
        """
        users = list(self._users.values())

        if active_only:
            users = [u for u in users if u.is_active]

        return users

    def update_user(
        self,
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        is_active: Optional[bool] = None
    ) -> User:
        """
        Update user information.

        Args:
            user_id: The user's ID
            name: New name (optional)
            email: New email (optional)
            is_active: New active status (optional)

        Returns:
            Updated User object

        Raises:
            UserNotFoundError: If user doesn't exist
            UserAlreadyExistsError: If new email already exists
        """
        user = self.get_user(user_id)

        # Update email if provided
        if email and email != user.email:
            # Check if new email already exists
            if email.lower() in self._email_index:
                raise UserAlreadyExistsError(f"Email {email} already in use")

            # Update email index
            del self._email_index[user.email.lower()]
            self._email_index[email.lower()] = user_id
            user.email = email

        # Update other fields
        if name:
            user.name = name
        if is_active is not None:
            user.is_active = is_active

        return user

    def delete_user(self, user_id: int) -> None:
        """
        Delete a user.

        Args:
            user_id: The user's ID

        Raises:
            UserNotFoundError: If user doesn't exist
        """
        user = self.get_user(user_id)

        # Remove from storage
        del self._users[user_id]
        del self._email_index[user.email.lower()]

