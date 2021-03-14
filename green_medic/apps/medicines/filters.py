from django.db.models import Q
from django_filters import FilterSet, CharFilter

from green_medic.apps.medicines.models import Medicine


class MedicineFilter(FilterSet):
    def search_medicines(self, queryset, name, value):
        return self.queryset.filter(
            Q(brand_name__icontains=value) | Q(generic_name__icontains=value)
        )

    brand_name = CharFilter(lookup_expr="icontains")
    generic_name = CharFilter(lookup_expr="icontains")
    search = CharFilter(method='search_medicines')

    class Meta:
        model = Medicine
        fields = []
