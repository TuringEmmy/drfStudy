# author    python
# time      18-10-22 下午4:15
# project   drtStudy
from django.conf.urls import url

from book6 import views

urlpatterns=[
    url(r'book6/$',views.BookListView.as_view()),
    url(r'book6/(?P<pk>\d+)/$',views.BookDetailView.as_view()),
]