# fixtures to be accessed globally across all tests can be put here
import pytest
from rest_framework.test import APIClient

from green_medic.apps.users.tests.factories import CustomerUserFactory, ShopkeeperUserFactory


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
def customer_user():
    return CustomerUserFactory()


@pytest.fixture
def shopkeeper_user():
    return ShopkeeperUserFactory()


@pytest.fixture
def auth_customer_client(customer_user, client):
    client.force_authenticate(customer_user)
    return client


@pytest.fixture
def auth_shopkeeper_client(shopkeeper_user, client):
    client.force_authenticate(shopkeeper_user)
    return client
