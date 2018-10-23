from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from book13.models import BookInfo
from book13.serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):
    """视图集"""

    querryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # 指定路由Router动态生成url配置项时提取参数的正则表达式
    lookup_value_regex = '\d+'

    @action(methods=['get'], detail=False)
    def latest(self, request):
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    @action(methods=['put'], detail=True)
    def read(self, request, pk):
        book = self.get_object()

        bread = request.data.get('bread')

        # 更新
        book.bread = bread

        book.save()

        serializer = self.get_serializer(book)
        return Response(serializer.data)
