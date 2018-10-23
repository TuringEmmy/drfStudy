from django.shortcuts import render

# Create your views here.

# 提供操作图书数据的5个API接口
# 1. 获取所有图书的数据	GET /books/
# 2. 新增一本图书的数据	POST /books/

# 3. 获取指定图书的数据	GET /books/ID/
# 4. 更新指定图书的数据	PUT /books/ID/
# 5. 删除指定图书的数据	DELETE /books/ID/
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from book10.models import BookInfo
from book10.serializers import BookInfoSerializer


class BookInfoViewSet(ListModelMixin,
                      CreateModelMixin,
                      RetrieveModelMixin,
                      UpdateModelMixin,
                      DestroyModelMixin,
                      GenericViewSet):
    """视图集"""

    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
