# author    python
# time      18-10-24 下午5:35
# project   drtStudy
from django.conf.urls import url

from book17 import views

urlpatterns = [
    url(r'^book17/$', views.BookInfoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    url(r'^book17/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    url(r'^book17/latest/$', views.BookInfoViewSet.as_view({
        'get': 'latest'
    })),
    url(r'^book17/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({
        'put': 'read'
    }))
]