# author    python
# time      18-10-21 下午3:18
# project   drtStudy
from django.conf.urls import url

from book03 import views

urlpatterns = [
    url(r'book3/$', views.BookListView.as_view()),
    url(r'^book3/(?P<pk>\d+)/$', views.BookDetaillView.as_view())
]
