# author    python
# time      18-10-23 下午12:10
# project   drtStudy
from rest_framework.routers import SimpleRouter

from book13 import views

urlpatterns=[

]


router = SimpleRouter()
router.register('book13',views.BookInfoViewSet,base_name = "Book13")
urlpatterns+=router.urls