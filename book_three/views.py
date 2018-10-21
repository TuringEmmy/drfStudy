import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

# /book3/(?<pk>\d+)/
from book_three.models import BookInfo
from book_three.serializers import BookInforSerializer


class BookDetaolView(View):
    """获取指定的图书的数据"""
    def get(self,request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=201)

        # 返回响应
        serializer = BookInforSerializer(book)

        return JsonResponse(serializer.data)

    def put(self,request,pk):
        """更新指定图书的数据"""
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 获取客户端传递得参数
        req_data = request.body
        json_str = req_data.decode()
        req_dict = json.loads(json_str)

        # 反序列化
        serializer = BookInforSerializer(book,data = req_data)
        # 数据校验
        serializer.is_valid(
            raise_exception=True
        )
        # 数据保存
        serializer.save()

        # 返回响应:200(返回更细后的数据)
        return JsonResponse(serializer.data)
class BookListView(View):
    pass