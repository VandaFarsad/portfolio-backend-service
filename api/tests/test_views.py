import pytest
from django.urls import reverse

from api.models import Experience, StackIcon


@pytest.mark.django_db
def test_stack_icon_list(api_client):
    """Test that the stack icon list endpoint returns 200 and data."""
    # Create test data
    StackIcon.objects.create(icon="python", icon_text="Python", order=1)
    StackIcon.objects.create(icon="django", icon_text="Django", order=2)

    url = reverse("stackicon-list")
    response = api_client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["id"] == "python"
    assert data[0]["name"] == "Python"
    assert data[1]["id"] == "django"


@pytest.mark.django_db
def test_experience_list(api_client):
    """Test that the experience list endpoint returns 200 and data."""
    # Create test data
    Experience.objects.create(
        category="work",
        start_date="2020-01-01",
        end_date="2023-01-01",
        organization="Example Corp",
        position="Software Engineer",
        stack=["python", "django"],
    )

    url = reverse("experience-list")
    response = api_client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["position"] == "Software Engineer"
    assert data[0]["organization"] == "Example Corp"
    assert "Python" in data[0]["stack"]
    assert "Django" in data[0]["stack"]


@pytest.mark.django_db
def test_stack_icon_detail(api_client):
    """Test that the stack icon detail endpoint returns 200."""
    icon = StackIcon.objects.create(icon="python", icon_text="Python", order=1)

    url = reverse("stackicon-detail", kwargs={"pk": icon.pk})
    response = api_client.get(url)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "python"
