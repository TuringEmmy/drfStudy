# author    python
# time      18-10-21 下午6:12
# project   drtStudy
from django.conf.urls import url

from goods import views

urlpatterns=[
    url(r'goods/(?P<pk>\d+)/$',views.GoodsView.as_view()),
]