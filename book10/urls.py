# author    python
# time      18-10-23 上午10:49
# project   drtStudy
from django.conf.urls import url

from book10 import views

urlpatterns = [
    url(r'^book10/$', views.BookInfoViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    url(r'^book10/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy',
    }))
]
