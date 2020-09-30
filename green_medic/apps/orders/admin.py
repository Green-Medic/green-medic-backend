from django.contrib import admin

from django.contrib.admin import ModelAdmin

from green_medic.apps.orders.models import Order, MedicineQuantity


class MedicineQuantityAdmin(ModelAdmin):
    autocomplete_fields = ['medicine']


admin.site.register(MedicineQuantity, MedicineQuantityAdmin)
admin.site.register(Order)
