# author    python
# time      18-10-21 下午3:18
# project   drtStudy
from django.conf.urls import url

from book_three import views

urlpatterns = [
    url(r'book_t/$', views.BookListView.as_view()),
    url(r'^book_t/(?P<pk>\d+)/$', views.BookDetaillView.as_view())
]
