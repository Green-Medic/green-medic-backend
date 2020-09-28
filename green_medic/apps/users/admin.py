from django.contrib import admin

from green_medic.apps.users.models import Customer, Shopkeeper

admin.site.register(Customer)
admin.site.register(Shopkeeper)
