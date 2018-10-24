from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book17.models import BookInfo
from book17.serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):
    """
    list: 获取所有图书数据
    create: 新增一本图书数据
    retrieve: 获取指定的图书数据
    update: 更新指定的图书数据
    delete: 删除指定的图书数据
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # GET /books/latest/
    def latest(self, request):
        """获取id最新的一本图书"""
        book = BookInfo.objects.latest('id')

        # 创建序列化器对象
        serializer = self.get_serializer(book)

        # 返回响应
        return Response(serializer.data)

    # PUT /books/(?P<pk>\d+)/read/
    def read(self, request, pk):
        """更新指定图书的阅读量"""
        # 获取更新图书对象
        book = self.get_object()

        # 客户端通过json数据传递更新阅读量bread
        bread = request.data.get('bread')

        # 更新数据
        book.bread = bread
        book.save()

        # 创建序列化器对象
        serializer = self.get_serializer(book)

        # 返回响应
        return Response(serializer.data)


