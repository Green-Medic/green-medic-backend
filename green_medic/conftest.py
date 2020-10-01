# fixtures to be accessed globally across all tests can be put here
import pytest
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def enable_db_access(db):
    """
    Global DB access to all tests.
    :param db:
    :return:
    """
    pass



@pytest.fixture
def client():
    """
    better off using rest framework's api client instead of built in django test client for pytest
    since we'll be working with developing and testing apis
    :return:
    """
    return APIClient()


@pytest.fixture
def user():
    return UserFactory(password=PASSWORD)


@pytest.fixture
def restaurant_superuser(user):
    user.is_restaurant_superuser = True
    user.save()
    return user


@pytest.fixture
def auth_client(user, client):
    client.force_authenticate(user)
    return client
