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

from book_four.models import BookInfo
from book_four.serializers import BookInfoSerializer


class BookListView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()

        # 序列,因为序列的结构是字典
        serializer =BookInfoSerializer(books,many=True)

        return Response(serializer.data)

    def post(self,request):
        serializer = BookInfoSerializer(data=request.data)
        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class BookDetail(APIView):
    def get(self,request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        # 序列化
        serialzer = BookInfoSerializer(book)

        return Response(serialzer.data)

    def put(self,request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise Http404

        # 更新书籍
        serializer = BookInfoSerializer(book,data=request.data)
        serializer.is_valid(
            raise_exception=True
        )

        return Response(serializer.data)

    def delete(self,request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            raise  Http404

        book.delete()

        return  Response(status=status.HTTP_204_NO_CONTENT)