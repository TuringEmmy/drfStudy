# author        TuringEmmy 
# createtime    18-10-19  下午5:27
# coding=utf-8
# doc           PyCharm
from book02 import views

urlpatterns = [

]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book2', views.BookInfoViewSet, base_name='book2')
urlpatterns += router.urls
