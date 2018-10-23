from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from book06.SelfGenericAPIView import MyGenericAPIView

# 使用Django基础知识自定义RestAPI接口
# 提供操作图书数据的5个API接口
# 1. 获取所有图书的数据	GET /book06/
# 2. 新增一本图书的数据	POST /book06/

# 3. 获取指定图书的数据	GET /book06/ID/
# 4. 更新指定图书的数据	PUT /books/ID/
# 5. 删除指定图书的数据	DELETE /book06/ID/


from book06.models import BookInfo
from book06.serializers import BookInfoSerializer


# /book06/
class BookListView(GenericAPIView):
    # 指定当前视图所使用的查询集
    queryset = BookInfo.objects.all()
    # 指定当前视图所使用的序列化器类
    serializer_class = BookInfoSerializer

    # 获取所有书
    def get(self, request):
        books = self.get_queryset()

        serializer = self.get_serializer(books, many=True)

        return Response(serializer.data)

    # 添加但本书
    def post(self, request):
        # 反序列化
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# /book06/(?P<pk>\d+)/
class BookDetailView(GenericAPIView):
    # 指定当前视图所使用的查询集
    queryset = BookInfo.objects.all()
    # 指定当前视图所使用的序列化器类
    serializer_class = BookInfoSerializer

    # 查询单册书
    def get(self, request, pk):
        book = self.get_object()

        serializer = self.get_serializer(book)

        return Response(serializer.data)

    # 更新但册书
    def put(self, request, pk):
        book = self.get_object()

        # 反序列化
        serializer = self.get_serializer(book, data=request.data)

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(serializer.data)

    # 删除但册书
    def delete(self, request, pk):
        book = self.get_object()

        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
