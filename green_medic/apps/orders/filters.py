from django_filters import FilterSet

from green_medic.apps.orders.models import Order


class OrderFilter(FilterSet):
    class Meta:
        model = Order
        fields = ['customer', 'shopkeeper', 'status']
