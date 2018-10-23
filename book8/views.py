from django.shortcuts import render

# Create your views here.

# 使用Django基础知识自定义RestAPI接口
# 提供操作图书数据的5个API接口
# 1. 获取所有图书的数据	GET /books/
# 2. 新增一本图书的数据	POST /books/

# 3. 获取指定图书的数据	GET /books/ID/
# 4. 更新指定图书的数据	PUT /books/ID/
# 5. 删除指定图书的数据	DELETE /books/ID/

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, \
    UpdateModelMixin

from book8.models import BookInfo
from book8.serializers import BookInfoSerializer
from book8.SelfSmallMixin import MyListCreateAPIView, MyRetrieveUpdateDestroyAPIView


class BookListView(MyListCreateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


class BookDetailView(MyRetrieveUpdateDestroyAPIView):
    # 指定当前视图所使用的查询集
    queryset = BookInfo.objects.all()
    # 指定当前视图所使用的序列化器类
    serializer_class = BookInfoSerializer

