# author    python
# time      18-10-23 上午11:30
# project   drtStudy
from django.conf.urls import url

from book11 import views

urlpatterns = [
    url(r'^book11/$', views.BookInfoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    url(r'^book11/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]