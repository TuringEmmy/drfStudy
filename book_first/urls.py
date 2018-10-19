# author        TuringEmmy 
# createtime    18-10-19  下午2:56
# coding=utf-8
# doc           PyCharm
from django.conf.urls import url

from book_first import views

urlpatterns = [
    url(r'books/$',views.BookListView.as_view()),
    url(r'books/(?P<pk>\d+)/$',views.BookDetailView.as_view())
]
