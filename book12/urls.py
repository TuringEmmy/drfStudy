# author    python
# time      18-10-23 上午11:43
# project   drtStudy
from django.conf.urls import url

from book12 import views

urlpatterns = [
    url(r'^book12/$', views.BookInfoViewSet.as_view({
        'post': 'list',
        'get': 'create',
    })),
    url(r'^book12/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    url(r'book12/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({
        'put': 'read',
    }))
]
