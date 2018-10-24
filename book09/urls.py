# author    python
# time      18-10-23 上午9:58
# project   drtStudy
from django.conf.urls import url

from book09 import views

urlpatterns = [
    url(r'^book9/$', views.BookInfoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    url(r'^book9/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
