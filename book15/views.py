from django.shortcuts import render

# Create your views here.
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from book15.SelfPagination import StandardResultPagination
from book15.models import BookInfo
from book15.serializers import BookInfoSerializer


# /book15/
class BookListView(ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # 指定过滤的字段
    filter_fields = ('btitle', 'bread')

    # 排序
    filter_backends = (OrderingFilter,)

    # 指定排序字段
    ordering_fields = ('id', 'bread', 'bpub_date')

    # 指定当前的视图所使用的分页类
    pagination_class = StandardResultPagination
