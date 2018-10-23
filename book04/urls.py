# author    python
# time      18-10-21 下午6:19
# project   drtStudy
from django.conf.urls import url

from book04 import views

urlpatterns=[
    url(r'book4/$',views.BookListView.as_view()),
]