from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


 # 使用Django基础知识自定义RestAPI接口
# 提供操作图书数据的5个API接口
# 1. 获取所有图书的数据	GET /book5/
# 2. 新增一本图书的数据	POST /book5/

# 3. 获取指定图书的数据	GET /book5/ID/
# 4. 更新指定图书的数据	PUT /book5/ID/
# 5. 删除指定图书的数据	DELETE /book5/ID/

# /book5/
from book_five.models import BookInfo
from book_five.serializers import BookInfoSerializer


class BookListView(APIView):
    # 获取所有书
    def get(self,request):
        books = BookInfo.objects.all()

        serializer = BookInfoSerializer(books,many=True)

        return Response(serializer.data)
    # 添加但本书
    def post(self,request):
        # 反序列化
        serializer = BookInfoSerializer(data=request.data)

        serializer.is_valid()
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)

# /book5/(?P<pk>\d+)/
class BookDetailView(APIView):
    # 查询单册书
    def get(self,request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        serializer = BookInfoSerializer(book)

        return Response(serializer.data)

    # 更新但册书
    def put(self,request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        # 反序列化
        serializer = BookInfoSerializer(book,data=request.data)

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(serializer.data)

    # 删除但册书
    def delete(self,request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
