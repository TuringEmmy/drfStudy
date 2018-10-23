# author    python
# time      18-10-22 下午4:15
# project   drtStudy
from django.conf.urls import url

from book06 import view

urlpatterns=[
    url(r'book6/$', view.BookListView.as_view()),
    url(r'book6/(?P<pk>\d+)/$', view.BookDetailView.as_view()),
]