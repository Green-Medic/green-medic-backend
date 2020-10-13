import pytest
from django.urls import reverse
from factory.fuzzy import FuzzyInteger
from faker import Faker
from rest_framework import status

from green_medic.apps.users.choices import StatusTypes
from green_medic.apps.users.tests.factories import \
    firebase_customer, firebase_shopkeeper, CustomerFactory, ShopkeeperFactory


class TestCustomerCreate:
    @pytest.fixture
    def customer_data(self):
        data = {
            'user': {
                'username': firebase_customer.phone_number,
                'password': firebase_customer.uid
            }
        }
        return data

    @pytest.fixture
    def customer_create_url(self):
        return reverse("api:users:customers_list_create")

    def test_create(self, customer_data, customer_create_url, client):
        response = client.post(customer_create_url, data=customer_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get('user', {}).get('username') == customer_data.get('user', {}).get('username')

    def test_create_failed(self, customer_data, customer_create_url, client):
        customer_data['user']['username'] = f"+{FuzzyInteger(low=10000000, high=9999999999).fuzz()}"
        customer_data['user']['password'] = Faker().password()
        response = client.post(customer_create_url, data=customer_data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_existing(self, customer_data, customer_create_url, client):
        customer = CustomerFactory()
        assert customer
        response = client.post(customer_create_url, data=customer_data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST


class TestShopkeeperCreate:
    @pytest.fixture
    def shopkeeper_data(self):
        data = {
            'user': {
                'username': firebase_shopkeeper.phone_number,
                'password': firebase_shopkeeper.uid,
            },
            'shop_name': Faker().company(),
            'address': Faker().address()
        }
        return data

    @pytest.fixture
    def shopkeeper_create_url(self):
        return reverse("api:users:shopkeepers_list_create")

    def test_create(self, shopkeeper_data, shopkeeper_create_url, client):
        response = client.post(shopkeeper_create_url, data=shopkeeper_data, format="json")
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data.get('user', {}).get('username') == shopkeeper_data.get('user', {}).get('username')
        assert response.data.get('shop_name') == shopkeeper_data.get('shop_name')
        assert response.data.get('status') == StatusTypes.PENDING

    def test_create_failed(self, shopkeeper_data, shopkeeper_create_url, client):
        shopkeeper_data['user']['username'] = f"+{FuzzyInteger(low=1000000, high=999999999).fuzz()}"
        shopkeeper_data['user']['password'] = Faker().password()
        response = client.post(shopkeeper_create_url, data=shopkeeper_data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_existing_shopkeeper(self, shopkeeper_data, shopkeeper_create_url, client):
        shopkeeper = ShopkeeperFactory()
        assert shopkeeper
        response = client.post(shopkeeper_create_url, data=shopkeeper_data, format="json")
        assert response.status_code == status.HTTP_400_BAD_REQUEST


# class TestCustomerView:
#     @pytest.fixture
#     def customer_list_url(self):
#         return reverse("api:users:customers_list_create")
#
#     # @pytest.fixture
#     # def shopkeeper(self):
#     #     return ShopkeeperFactory()
#
#     def test_list_view(self, client, customer_list_url):
#         shopkeeper = CustomerFactory()
#         client.force_authenticate(shopkeeper.user)
#         response = client.get(customer_list_url)
#         assert response.status_code == 200
#         assert response.data.get('result').get('count') == 1
