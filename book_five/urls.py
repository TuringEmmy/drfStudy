# author    python
# time      18-10-22 下午3:29
# project   drtStudy
from django.conf.urls import url

from book_five import views

urlpatterns=[
    url(r'^book5/$',views.BookListView.as_view()),
    url(r'book5/(?P<pk>\d+)/$',views.BookDetailView.as_view())
]