# author        TuringEmmy 
# createtime    18-10-19  下午5:27
# coding=utf-8
# doc           PyCharm
from book_second import views

urlpatterns = [

]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book_s', views.BookInfoViewSet, base_name='book_s')
urlpatterns += router.urls
