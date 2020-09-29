from django_filters import FilterSet, CharFilter

from green_medic.apps.medicines.models import Medicine


class MedicineFilter(FilterSet):
    brand_name = CharFilter(lookup_expr="icontains")
    generic_name = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Medicine
        fields = []
