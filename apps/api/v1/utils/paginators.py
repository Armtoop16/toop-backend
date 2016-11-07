# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework.pagination import PageNumberPagination


class APIPaginator(PageNumberPagination):
    """
    Paginator class for DRF resources
    """
    page_size = 10
    page_size_query_param = 'per_page'
    max_page_size = 100
