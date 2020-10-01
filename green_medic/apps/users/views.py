from rest_framework.viewsets import ModelViewSet

from green_medic.apps.users.choices import StatusTypes
from green_medic.apps.users.models import Customer, Shopkeeper
from green_medic.apps.users.permissions import IsCustomer
from green_medic.apps.users.serializers import CustomerSerializer, ShopkeeperSerializer


class CustomerView(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsCustomer]


class ShopkeeperView(ModelViewSet):
    serializer_class = ShopkeeperSerializer
    queryset = Shopkeeper.objects.filter(status=StatusTypes.APPROVED)
