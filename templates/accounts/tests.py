import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user_with_role():
    user = User.objects.create_user(username="teacher1", password="pass1234", role="TEACHER")
    assert user.role == "TEACHER"
    assert user.check_password("pass1234")


@pytest.mark.django_db
def test_default_role_choices():
    roles = [choice[0] for choice in User.Role.choices]
    assert "ADMIN" in roles
    assert "TEACHER" in roles
    assert "PARENT" in roles