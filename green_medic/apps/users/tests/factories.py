from django.contrib.auth.models import User
import factory
from factory.django import DjangoModelFactory

from green_medic.apps.base.firebase.constants import TEST_CUSTOMER, TEST_SHOPKEEPER
from green_medic.apps.base.firebase.firebase import get_or_create_firebase_test_user
from green_medic.apps.users.models import Customer, Shopkeeper


firebase_customer = get_or_create_firebase_test_user(**TEST_CUSTOMER)
firebase_shopkeeper = get_or_create_firebase_test_user(**TEST_SHOPKEEPER)


class _CustomerUserFactory(DjangoModelFactory):
    username = firebase_customer.phone_number
    password = firebase_customer.uid

    class Meta:
        model = User


class _ShopkeeperUserFactory(DjangoModelFactory):
    username = firebase_shopkeeper.phone_number
    password = firebase_shopkeeper.uid

    class Meta:
        model = User


class CustomerFactory(DjangoModelFactory):
    user = factory.SubFactory(_CustomerUserFactory)

    class Meta:
        model = Customer


class ShopkeeperFactory(DjangoModelFactory):
    user = factory.SubFactory(_ShopkeeperUserFactory)
    shop_name = factory.Faker('company')
    address = factory.Faker("street_address")

    class Meta:
        model = Shopkeeper
