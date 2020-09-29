from django.contrib.postgres.fields import ArrayField, HStoreField
from django.db import models

from green_medic.apps.base.models import TimeStampedModel
from green_medic.apps.orders.choices import OrderStatusTypes
from green_medic.apps.users.models import Customer


class Order(TimeStampedModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    medicines = ArrayField(
        # keys: medicine_id, quantity
        HStoreField()
    )
    conversation = ArrayField(
        # keys: customer and shopkeeper
        HStoreField()
    )
    status = models.PositiveSmallIntegerField(choices=OrderStatusTypes.choices, default=OrderStatusTypes.PENDING)


    # @property
    # def similar_medicines(self):
    #     return Medicine.objects.filter(generic_name=self.generic_name)
    #
    # def __str__(self):
    #     return f"{self.manufacturer}, {self.brand_name}"