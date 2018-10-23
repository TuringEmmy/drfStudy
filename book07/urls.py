# author    python
# time      18-10-22 下午5:15
# project   drtStudy
from django.conf.urls import url

from book07 import view

urlpatterns = [
    url(r'^book7/$', view.BookListView.as_view()),
    url(r'^book7/(?P<pk>\d+)/$', view.BookDetailView.as_view()),
]