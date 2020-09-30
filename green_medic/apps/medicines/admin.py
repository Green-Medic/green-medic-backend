from django.contrib import admin
from django.contrib.admin import ModelAdmin

from green_medic.apps.medicines.models import Medicine


class MedicineAdmin(ModelAdmin):
    search_fields = ('brand_name', )


admin.site.register(Medicine, MedicineAdmin)
