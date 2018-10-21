# author    python
# time      18-10-21 下午3:18
# project   drtStudy

from book_three import views

urlpatterns = [

]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('book3', views.BookListView, base_name='book3')
router.register('^book3/(?<pk>\d+)/$',views.BookDetaolView.as_view()),
urlpatterns += router.urls
