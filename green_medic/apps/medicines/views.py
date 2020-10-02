from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from green_medic.apps.medicines.filters import MedicineFilter
from green_medic.apps.medicines.models import Medicine
from green_medic.apps.medicines.pagination import SetPagination15
from green_medic.apps.medicines.serializers import MedicineListSerializer, MedicineRetrieveSerializer
from green_medic.apps.users.permissions import IsShopkeeperReadOnly, IsCustomerReadOnly


class MedicineListView(ListAPIView):
    serializer_class = MedicineListSerializer
    queryset = Medicine.objects.all()
    pagination_class = SetPagination15
    filter_backends = [DjangoFilterBackend]
    filter_class = MedicineFilter
    permission_classes = [IsShopkeeperReadOnly | IsCustomerReadOnly]


class MedicineRetrieveView(RetrieveAPIView):
    serializer_class = MedicineRetrieveSerializer
    queryset = Medicine.objects.all()
    permission_classes = [IsShopkeeperReadOnly | IsCustomerReadOnly]
