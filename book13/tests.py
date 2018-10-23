import os

from django.test import TestCase

# Create your tests here.

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drtStudy.settings")

# 让Django进行一次初始化
import django
django.setup()


# 一定要注意这两行代码的导入位置
from rest_framework.routers import SimpleRouter, DefaultRouter
from book13.views import BookInfoViewSet

if __name__ == '__main__':
    print('# 使用路由Router动态生成视图集中处理函数的url配置项')
    router = SimpleRouter()
    # router = DefaultRouter()

    # 注册路由
    router.register("demo",BookInfoViewSet,base_name='lege')

    urls = router.urls

    for url in urls:
        print(urls)