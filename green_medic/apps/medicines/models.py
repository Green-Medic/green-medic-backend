from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from green_medic.apps.base.models import TimeStampedModel


class Medicine(TimeStampedModel):
    manufacturer = models.CharField(max_length=255, blank=False, null=False)
    brand_name = models.CharField(max_length=100, blank=False, null=False)
    generic_name = models.CharField(max_length=255, blank=False, null=False)
    strength = models.CharField(max_length=100, blank=True, null=True)
    dosages = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(decimal_places=3, max_digits=12,
                                validators=[MinValueValidator(Decimal('0.000'))])
    use_for = models.CharField(max_length=50, blank=True, null=True)
    dar = models.CharField(max_length=100, blank=True, null=True)

    @property
    def similar_medicines(self):
        return Medicine.objects.filter(generic_name=self.generic_name)

    def __str__(self):
        return f"{self.manufacturer}, {self.brand_name}"
