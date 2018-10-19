import json

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from book_first.models import BookInfo


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
    def post(self,request):

        req_data = request.body
        # 注意这里接收到的数据是bytes
        json_str = req_data.decode()
        # 将字符串转换成python字典
        req_dict = json.loads(json_str)

        # 获取数据
        btitle = req_dict.get('btitle')
        bpub_date = req_dict.get('bpub_date')

