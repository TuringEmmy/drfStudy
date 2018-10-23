from django.http import Http404
from django.shortcuts import render

# Create your views here.
# 使用Django基础知识自定义RestAPI接口
# 提供操作图书数据的5个API接口
# 1. 获取所有图书的数据	GET /books/
# 2. 新增一本图书的数据	POST /books/

# 3. 获取指定图书的数据	GET /books/ID/
# 4. 更新指定图书的数据	PUT /books/ID/
# 5. 删除指定图书的数据	DELETE /books/ID/
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ViewSetMixin

from book09.models import BookInfo
from book09.serializers import BookInfoSerializer


# class BookInfoViewSet(ViewSetMixin,APIView):
class BookInfoViewSet(ViewSet):
    """视图集"""

    # GET /book09/
    def list(self, request):
        books = BookInfo.objects.all()

        # 反序列化
        serializer = BookInfoSerializer(books, many=True)

        return Response(serializer.data)

    # POST /book09/
    def create(self, request):
        # 假定客户端访问接口给服务器传递参数(btitle, bpub_date)，通过json进行传
        # 反序列化
        serializer = BookInfoSerializer(data=request.data)
        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # GET /book09/(?P<pk>\d+)/
    def retrieve(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        # 反序列化
        serializer = BookInfoSerializer(book)

        return Response(serializer.data)

    # PUT /book09/(?P<pk>\d+)/
    def update(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        # 反序列化
        serializer = BookInfoSerializer(book, data=request.data)
        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(serializer.data)

    # DELETE /book09/(?P<pk>\d+)/
    def destroy(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
