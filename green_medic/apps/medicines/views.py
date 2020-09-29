from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend

from green_medic.apps.medicines.filters import MedicineFilter
from green_medic.apps.medicines.models import Medicine
from green_medic.apps.medicines.pagination import MedicineSetPagination
from green_medic.apps.medicines.serializers import MedicineListSerializer, MedicineRetrieveSerializer


class MedicineListView(ListAPIView):
    serializer_class = MedicineListSerializer
    queryset = Medicine.objects.all()
    pagination_class = MedicineSetPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = MedicineFilter


class MedicineRetrieveView(RetrieveAPIView):
    serializer_class = MedicineRetrieveSerializer
    queryset = Medicine.objects.all()
