from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from book_first.models import BookInfo


class BookListView(View):
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

