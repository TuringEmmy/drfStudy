# author    python
# time      18-10-24 下午4:49
# project   drtStudy
from django.conf.urls import url

from book15 import views

urlpatterns = [
    url(r'book15/$', views.BookListView.as_view()),
]
