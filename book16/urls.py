# author    python
# time      18-10-24 下午5:08
# project   drtStudy
from django.conf.urls import url

from book16 import views

urlpatterns=[
    url(r'^book16/$',views.IndexView.as_view()),
]