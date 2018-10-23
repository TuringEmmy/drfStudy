import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from book01.models import BookInfo


# ----------------------------------------------添加图书和查询图书------------------------------------
# /books/
class BookListView(View):
    # 获取所有图书的数据
    def get(self, request):
        # 从数据库中查询所有的图数据
        books = BookInfo.objects.all()

        # 组织数据
        books_list = []

        for book in books:
            book_dict = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'image': book.image.url if book.image else ""
            }
            books_list.append(book_dict)
        # 返回响应:200

        return JsonResponse(books_list, safe=False)

    # 新增一本图书的数据
    def post(self, request):
        req_data = request.body
        # 注意这里接收到的数据是bytes
        json_str = req_data.decode()
        # 将字符串转换成python字典
        req_dict = json.loads(json_str)

        # 获取数据
        btitle = req_dict.get('btitle')
        bpub_date = req_dict.get('bpub_date')

        # 创建一本新图书并添加到数据库
        book = BookInfo.objects.create(
            btitle=btitle,
            bpub_date=bpub_date
        )

        # 返回响应:201新增图书数据
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.url else ""
        }

        return JsonResponse(book_dict, status=201)


# ----------------------------------------------针对某一本书--------------------------------------
# /books/(?P<pk>\d+)/
class BookDetailView(View):
    # 获取指定图书
    def get(self, request, pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist as e:
            return HttpResponse(status=404)

        # 返回响应:200指定图书的数据
        book_dict ={
            'id':book.id,
            'btitle':book.btitle,
            'bpub_date':book.bpub_date,
            'bread':book.bread,
            'bcomment':book.bcomment,
            'image':book.image.url if book.image else ""
        }

        return JsonResponse(book_dict)

    # 更新指定图书的数据
    def put(self,request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            # 图书不存在
            return HttpResponse(status=404)

        # 获取客户传递的参数
        req_data = request.body
        json_str = req_data.decode()
        req_dict  = json.loads(json_str)

        # 获取数据
        btitle = req_dict.get('btitle')
        bpub_date = req_dict.get('bpub_date')

        # 更新指定的图书
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()

        # 返回响应:200 更新之后的图书数据
        book_dict ={
            'id':book.id,
            'btitle':book.btitle,
            'bpub_date':book.bpub_date,
            'bread':book.bcomment,
            'bcomment':book.bcomment,
            'image':book.image.url if book.image else ""
        }

        return JsonResponse(book_dict)

    # 删除指定图书的数据
    def delete(self,request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 删除图书
        book.delete()
        # 返回响应:204
        return HttpResponse(status=204)

