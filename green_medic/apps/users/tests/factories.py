from django.contrib.auth.models import User
import factory
from factory.django import DjangoModelFactory

from green_medic.apps.users.models import Customer, Shopkeeper
from green_medic.apps.users.tests.fuzz import FuzzyPhoneNumber


class UserFactory(DjangoModelFactory):
    username = FuzzyPhoneNumber()

    class Meta:
        model = User


class CustomerFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Customer


class ShopkeeperFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Shopkeeper
