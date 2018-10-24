# author    python
# time      18-10-24 下午3:15
# project   drtStudy

from book14 import views

urlpatterns = [

]

# 路由Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book14', views.BookInfoViewSet, base_name='Book14')
urlpatterns += router.urls
