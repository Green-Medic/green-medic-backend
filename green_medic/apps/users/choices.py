from django.db.models import IntegerChoices


class GenderTypes(IntegerChoices):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    UNSPECIFIED = 4
