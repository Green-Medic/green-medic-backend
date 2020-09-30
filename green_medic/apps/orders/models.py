import datetime
from decimal import Decimal

from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum, F

from green_medic.apps.base.models import TimeStampedModel
from green_medic.apps.medicines.models import Medicine
from green_medic.apps.orders.choices import OrderStatusTypes
from green_medic.apps.orders.constants import DEFAULT_SYSTEM_MESSAGE
from green_medic.apps.users.models import Customer, Shopkeeper


class MedicineQuantity(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.medicine} X {self.quantity}'


class Order(TimeStampedModel):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=255, blank=True, null=True)
    shopkeeper = models.ForeignKey(Shopkeeper, on_delete=models.SET_NULL, null=True, blank=True)
    medicines = models.ManyToManyField(MedicineQuantity, related_name='medicine_quantity')
    # keys: customer and time or shopkeeper and time
    conversation = ArrayField(models.JSONField(), default=[DEFAULT_SYSTEM_MESSAGE])
    status = models.PositiveSmallIntegerField(choices=OrderStatusTypes.choices,
                                              default=OrderStatusTypes.PENDING)
    shop_price = models.DecimalField(decimal_places=3, max_digits=12, default=0,
                                     validators=[MinValueValidator(Decimal(0.000))])

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self._prev_state = self

    def system_price(self):
        return self.medicines.aggregate(
            total_price=Sum(F('medicine__price') * F('quantity'),
                            output_field=models.FloatField())).get('total_price')

    def save(self, *args, **kwargs):
        if self.pk:
            processed_conversation = []
            for chat in self.conversation:
                chat.update({"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
                processed_conversation.append(chat)
            self.conversation = self._prev_state.conversation + processed_conversation
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.customer.user.username} -->' \
               f'{self.medicines.all()} --> ' \
               f'{self.system_price()}'
