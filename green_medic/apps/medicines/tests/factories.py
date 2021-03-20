import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from green_medic.apps.medicines.models import Medicine


class MedicineFactory(DjangoModelFactory):
    manufacturer = factory.Faker("word")
    brand_name = factory.Faker("word")
    generic_name = factory.Faker("word")
    price = fuzzy.FuzzyDecimal(1.00, high=100.00)

    class Meta:
        model = Medicine
