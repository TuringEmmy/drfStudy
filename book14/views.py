from django.shortcuts import render

# Create your views here.


# 需求
# 定义一个视图集,提供下面两个接口
# 1. 获取所有的图书数据(list)GET  /book14/
# 2. 获取指定的图书的数据(retrieve) GET /book14/(?P<pk>\d+)/
from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from book14.SelfPermission import MyPermission
from book14.models import BookInfo
from book14.serializers import BookInfoSerializer


class BookInfoViewSet(ReadOnlyModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # 指定当前视图所使用的认证方式(指定之后不在使用全局认证方案)
    authentication_classes = (SessionAuthentication,)

    # 指定当前视图所使用的权限控制方式(指定之后不在使用全局权限控制)
    # permission_classes = =(IsAuthenticated, )

    # 使用自定义的权限控制类
    permission_classes = (MyPermission,)

    # 指定当前视图所使用的限流控制类(仅针对匿名用户进行限流控制)
    # throttle_classes = (AnonRateThrottle, )

    # 指定当前视图所使用的限流频次的选择项
    throttle_scope = 'upload'