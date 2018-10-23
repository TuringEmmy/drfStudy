from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book12.models import BookInfo
from book12.serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # ====================================自定义的read方法=================================
    # PUT /book12/(?P<pk>\d+)/read/
    def read(self, request, pk):
        """更新指定图书的阅读量"""
        book = self.get_object()
        bread = request.data.get('bread')

        # 更新数据
        book.bread = bread
        book.save()

        # 创建序列化器对象
        serializer = self.get_serializer(book)

        # 返回响应
        return Response(serializer.data)

    # ======================================自定义latest方法================================
    # GET /books/latest/
    def latest(self, request):
        """获取bpub_date最新的的图书"""
        # 参数可以是字段当中任何可以比较的哦
        book = BookInfo.objects.latest('bpub_date')

        # 创建序列化
        serializer = self.get_serializer(book)

        # 返回响应
        return Response(serializer.data)
