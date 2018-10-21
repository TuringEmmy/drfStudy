# author    python
# time      18-10-21 下午6:19
# project   drtStudy
from django.conf.urls import url

from book_four import views

urlpatterns=[
    url(r'book_f/$',views.BookListView.as_view()),
]