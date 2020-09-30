from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from green_medic.apps.medicines.pagination import SetPagination15
from green_medic.apps.orders.filters import OrderFilter
from green_medic.apps.orders.models import Order
from green_medic.apps.orders.serializers import OrderSerializer


class OrderListView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('-id')
    pagination_class = SetPagination15
    filter_backends = [DjangoFilterBackend]
    filter_class = OrderFilter


class OrderRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

