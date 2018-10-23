# author        TuringEmmy 
# createtime    18-10-19  下午2:56
# coding=utf-8
# doc           PyCharm
from django.conf.urls import url

from book01 import views

urlpatterns = [
    url(r'book1/$',views.BookListView.as_view()),
    url(r'book1/(?P<pk>\d+)/$',views.BookDetailView.as_view())
]
