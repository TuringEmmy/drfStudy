# author    python
# time      18-10-24 下午4:52
# project   drtStudy
from rest_framework.pagination import PageNumberPagination


class StandardResultPagination(PageNumberPagination):
    # 指定默认的页容量
    page_size = 3
    # 指定传递页容量参数名称
    page_query_param = 'page_size'
    # 指定最大页容量
    max_page_size = 5
