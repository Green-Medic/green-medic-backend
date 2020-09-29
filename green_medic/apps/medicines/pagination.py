
from rest_framework.pagination import PageNumberPagination


class MedicineSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = "page_size"