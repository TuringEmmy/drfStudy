# author    python
# time      18-10-22 下午5:15
# project   drtStudy
from django.conf.urls import url

from book7 import views

urlpatterns = [
    url(r'^book7/$', views.BookListView.as_view()),
    url(r'^book7/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
]