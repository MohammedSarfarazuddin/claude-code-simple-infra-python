"""
Tests for user service.
This file demonstrates pytest best practices.
"""

import pytest
from src.user_service import (
    UserService,
    UserNotFoundError,
    UserAlreadyExistsError
)


class TestUserService:
    """Test suite for UserService"""

    @pytest.fixture
    def user_service(self):
        """Provide a fresh UserService instance for each test"""
        return UserService()

    @pytest.fixture
    def sample_user_data(self):
        """Provide sample user data"""
        return {
            "email": "test@example.com",
            "name": "Test User"
        }

    # Happy path tests
    def test_create_user_success(self, user_service, sample_user_data):
        """Test successful user creation"""
        # Arrange
        email = sample_user_data["email"]
        name = sample_user_data["name"]

        # Act
        user = user_service.create_user(email=email, name=name)

        # Assert
        assert user.email == email
        assert user.name == name
        assert user.id == 1
        assert user.is_active is True
        assert user.created_at is not None

    def test_get_user_success(self, user_service, sample_user_data):
        """Test retrieving an existing user"""
        # Arrange
        created_user = user_service.create_user(**sample_user_data)

        # Act
        retrieved_user = user_service.get_user(created_user.id)

        # Assert
        assert retrieved_user.id == created_user.id
        assert retrieved_user.email == created_user.email
        assert retrieved_user.name == created_user.name

    def test_list_users_returns_all(self, user_service):
        """Test listing all users"""
        # Arrange
        user_service.create_user("user1@example.com", "User 1")
        user_service.create_user("user2@example.com", "User 2")

        # Act
        users = user_service.list_users()

        # Assert
        assert len(users) == 2
        assert users[0].email == "user1@example.com"
        assert users[1].email == "user2@example.com"

    # Error case tests
    def test_create_user_duplicate_email_raises_error(
        self, user_service, sample_user_data
    ):
        """Test that duplicate email raises UserAlreadyExistsError"""
        # Arrange
        user_service.create_user(**sample_user_data)

        # Act & Assert
        with pytest.raises(
            UserAlreadyExistsError,
            match="User with email .* already exists"
        ):
            user_service.create_user(**sample_user_data)

    def test_get_user_not_found_raises_error(self, user_service):
        """Test that getting non-existent user raises UserNotFoundError"""
        # Act & Assert
        with pytest.raises(UserNotFoundError, match="User with ID 999 not found"):
            user_service.get_user(999)

    def test_create_user_empty_email_raises_error(self, user_service):
        """Test that empty email raises ValueError"""
        # Act & Assert
        with pytest.raises(ValueError, match="Email and name are required"):
            user_service.create_user("", "Test User")

    def test_create_user_empty_name_raises_error(self, user_service):
        """Test that empty name raises ValueError"""
        # Act & Assert
        with pytest.raises(ValueError, match="Email and name are required"):
            user_service.create_user("test@example.com", "")

    # Edge case tests
    def test_get_user_by_email_case_insensitive(self, user_service):
        """Test that email lookup is case-insensitive"""
        # Arrange
        user_service.create_user("Test@Example.com", "Test User")

        # Act
        user_lower = user_service.get_user_by_email("test@example.com")
        user_upper = user_service.get_user_by_email("TEST@EXAMPLE.COM")

        # Assert
        assert user_lower is not None
        assert user_upper is not None
        assert user_lower.id == user_upper.id

    def test_get_user_by_email_not_found_returns_none(self, user_service):
        """Test that non-existent email returns None"""
        # Act
        user = user_service.get_user_by_email("nonexistent@example.com")

        # Assert
        assert user is None

    def test_list_users_active_only_filter(self, user_service):
        """Test filtering for active users only"""
        # Arrange
        user1 = user_service.create_user("user1@example.com", "User 1")
        user_service.create_user("user2@example.com", "User 2")

        # Deactivate user1
        user_service.update_user(user1.id, is_active=False)

        # Act
        active_users = user_service.list_users(active_only=True)

        # Assert
        assert len(active_users) == 1
        assert active_users[0].email == "user2@example.com"

    # Update tests
    def test_update_user_name(self, user_service, sample_user_data):
        """Test updating user name"""
        # Arrange
        user = user_service.create_user(**sample_user_data)

        # Act
        updated = user_service.update_user(user.id, name="New Name")

        # Assert
        assert updated.name == "New Name"
        assert updated.email == sample_user_data["email"]

    def test_update_user_email(self, user_service, sample_user_data):
        """Test updating user email"""
        # Arrange
        user = user_service.create_user(**sample_user_data)

        # Act
        updated = user_service.update_user(user.id, email="newemail@example.com")

        # Assert
        assert updated.email == "newemail@example.com"

        # Verify old email lookup fails
        assert user_service.get_user_by_email(sample_user_data["email"]) is None

        # Verify new email lookup works
        assert user_service.get_user_by_email("newemail@example.com") is not None

    def test_update_user_duplicate_email_raises_error(self, user_service):
        """Test that updating to existing email raises error"""
        # Arrange
        user1 = user_service.create_user("user1@example.com", "User 1")
        user_service.create_user("user2@example.com", "User 2")

        # Act & Assert
        with pytest.raises(UserAlreadyExistsError, match="Email .* already in use"):
            user_service.update_user(user1.id, email="user2@example.com")

    # Delete tests
    def test_delete_user_success(self, user_service, sample_user_data):
        """Test successful user deletion"""
        # Arrange
        user = user_service.create_user(**sample_user_data)

        # Act
        user_service.delete_user(user.id)

        # Assert
        with pytest.raises(UserNotFoundError):
            user_service.get_user(user.id)

    def test_delete_user_not_found_raises_error(self, user_service):
        """Test that deleting non-existent user raises error"""
        # Act & Assert
        with pytest.raises(UserNotFoundError):
            user_service.delete_user(999)
