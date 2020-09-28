from django.db import models

from green_medic.apps.base.models import TimeStampedModel


class Medicine(TimeStampedModel):
    manufacturer = models.CharField(max_length=255, blank=False, null=False)
    brand_name = models.CharField(max_length=100, blank=False, null=False)
    generic_name = models.CharField(max_length=255, blank=False, null=False)
    strength = models.CharField(max_length=100, blank=True, null=True)
    dosages = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    use_for = models.CharField(max_length=50, blank=True, null=True)
    dar = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.manufacturer}, {self.brand_name}"
