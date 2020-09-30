
from rest_framework.pagination import PageNumberPagination


class SetPagination15(PageNumberPagination):
    page_size = 15
    page_size_query_param = "page_size"