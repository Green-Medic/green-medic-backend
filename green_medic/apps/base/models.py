from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="%(class)s_created_at"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="%(class)s_updated_at"
    )

    class Meta:
        abstract = True
