# author    python
# time      18-10-22 下午6:09
# project   drtStudy
from django.conf.urls import url

from book8 import views

urlpatterns = {
    url(r'^book8/$', views.BookListView.as_view()),
    url(r'^book8/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
}