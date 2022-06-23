import pytest

from users.models import CustomUser


@pytest.mark.django_db
def test_user_create():
    CustomUser.objects.create_user("testuser@test.com", "1234")
    assert CustomUser.objects.all().count() == 1


@pytest.mark.django_db
def test_should_create_user_with_username() -> None:
    user = CustomUser.objects.create_user("testuser@test.com", "1234")
    assert user.email == "testuser@test.com"


@pytest.mark.django_db
def test_should_check_password(db) -> None:
    user = CustomUser.objects.create_user("testuser@test.com", "1234")
    user.set_password("secret")
    assert user.check_password("secret") is True
