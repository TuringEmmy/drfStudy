### 获取动态生成的url配置列表

```
urlpatterns = [
    # url(r'^books/$', views.BookInfoViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create',
    # }), name='books-list'),
    # url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # }), name='books-detail'),
    # url(r'^books/latest/$', views.BookInfoViewSet.as_view({
    #     'get': 'latest'
    # }), name='books-latest'),
    # url(r'^books/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({
    #     'put': 'read'
    # }), name='books-read')
]

# from rest_framework.routers import SimpleRouter
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('books', views.BookInfoViewSet, base_name='books')
urlpatterns += router.urls


# list create books/ books-list
# latest books/latest/ books-latest
# retrieve update destroy books/(?P<pk>\d+)/ books-detail
# read books/(?P<pk>\d+)/read/ books-read

```
