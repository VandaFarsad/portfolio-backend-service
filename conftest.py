from typing import Any

import pytest
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture(scope="session")
def request_factory() -> RequestFactory:
    """Create a Django RequestFactory for building test requests."""
    return RequestFactory()


@pytest.fixture()
def api_client() -> APIClient:
    """Unauthenticated DRF test client."""
    return APIClient()


@pytest.fixture()
def user(db: Any) -> User:
    """Create a regular test user."""
    return User.objects.create_user(email="test@example.com", password="testpass123")


@pytest.fixture()
def auth_client(user: User) -> APIClient:
    """Authenticated DRF test client using regular user."""
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture()
def staff_user(db: Any) -> User:
    """Create a staff test user."""
    return User.objects.create_user(
        email="staff@example.com", password="testpass123", is_staff=True, role=User.Role.MEMBER
    )


@pytest.fixture()
def staff_client(staff_user: User) -> APIClient:
    """Authenticated DRF test client using staff user."""
    client = APIClient()
    client.force_authenticate(user=staff_user)
    return client
