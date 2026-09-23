import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def make_user(db):
    def _make(role, username):
        return User.objects.create_user(username=username, password="pass1234", role=role)
    return _make


@pytest.mark.django_db
def test_admin_can_access_admin_dashboard(client, make_user):
    make_user("ADMIN", "admin1")
    client.login(username="admin1", password="pass1234")
    response = client.get(reverse("admin_dashboard"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_parent_cannot_access_teacher_dashboard(client, make_user):
    make_user("PARENT", "parent1")
    client.login(username="parent1", password="pass1234")
    response = client.get(reverse("teacher_dashboard"))
    assert response.status_code == 403


@pytest.mark.django_db
def test_teacher_cannot_access_admin_dashboard(client, make_user):
    make_user("TEACHER", "teacher1")
    client.login(username="teacher1", password="pass1234")
    response = client.get(reverse("admin_dashboard"))
    assert response.status_code == 403


@pytest.mark.django_db
def test_logged_out_user_redirected_to_login(client):
    response = client.get(reverse("parent_dashboard"))
    assert response.status_code == 302
    assert "/login/" in response.url