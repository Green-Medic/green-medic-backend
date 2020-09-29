from django.db.models import IntegerChoices


class OrderStatusTypes(IntegerChoices):
    PENDING = 1
    APPROVED = 2
    DONE = 3
    CANCELED = 4
