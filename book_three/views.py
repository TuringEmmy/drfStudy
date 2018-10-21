import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from book_three.models import BookInfo
from book_three.serializers import BookInforSerializer


# /book3/(?<pk>\d+)/
class BookDetaillView(View):
    """获取指定的图书的数据"""

    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=201)

        # 返回响应
        serializer = BookInforSerializer(book)

        return JsonResponse(serializer.data)

    def put(self, request, pk):
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
        serializer = BookInforSerializer(book, data=req_dict)
        # 数据校验
        serializer.is_valid(
            raise_exception=True
        )
        # 数据保存(更新指定的图书)
        serializer.save()

        # 返回响应:200(返回更细后的数据)
        return JsonResponse(serializer.data)

    def delete(self,request,pk):
        """删除指定图书的数据"""
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 删除图书
        book.delete()

        # 返回响应：204
        return HttpResponse(status=204)

# /book_t/
class BookListView(View):
    """获取所有图书的数据"""
    def get(self,request):
        books = BookInfo.objects.all()

        # 组织数据
        serialzer = BookInforSerializer(books,many=True)

        # 返回响应：200
        # 为了允许非dict对象被序列化，将安全参数设置为False。
        return JsonResponse(serialzer.data,safe=False)

    def post(self,request):
        """新增一本图书"""
        req_data = request.body

        req_data = request.body  # bytes
        json_str = req_data.decode()
        req_dict = json.loads(json_str)

        serilalizer = BookInforSerializer(data=req_dict)
        serilalizer.is_valid(
            raise_exception=True
        )

        serilalizer.save()

        return JsonResponse(serilalizer.data,status=201)
