import pytest
from django.urls import reverse

from green_medic.apps.medicines.models import Medicine
from green_medic.apps.medicines.tests.factories import MedicineFactory


class BaseTestMedicine:
    NO_OF_MEDICINE_CREATED = 10

    @pytest.fixture
    def medicines(self):
        return MedicineFactory.create_batch(size=self.NO_OF_MEDICINE_CREATED)


class TestMedicineList(BaseTestMedicine):

    @pytest.fixture
    def url(self):
        return reverse("api:medicine:medicines_list")

    def test_medicine_list(self, medicines, client, url):

        response = client.get(url)
        assert response.status_code == 200
        assert response.data.get("count") == self.NO_OF_MEDICINE_CREATED

    def test_medicine_list_with_filter(self, medicines, client, url):
        all_medicines = Medicine.objects.all()
        brand_name = all_medicines.first().brand_name

        response = client.get(f"{url}?brand_name={brand_name}")
        assert response.status_code == 200
        assert response.data.get("count") == all_medicines.filter(brand_name__contains=brand_name).count()
