# author        TuringEmmy 
# createtime    18-10-19  下午5:27
# coding=utf-8
# doc           PyCharm
from book_second import views

urlpatterns = [

]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('bk', views.BookInfoViewSet, base_name='bk')
urlpatterns += router.urls
