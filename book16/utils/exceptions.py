# author    python
# time      18-10-24 下午5:20
# project   drtStudy
from django.db import DatabaseError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler as eh


def exception_hander(exc, context):
    """调用DRF框架原始的异常处理函数"""
    response = eh(exc, context)

    if response is None:
        # DRF框架默认不要处理此异常
        view = context['view']
        # 补充Django数据库异常处理
        if isinstance(exc, DatabaseError):
            print('[%s]: %s ' % (view, type(exc)))
            response = Response({
                "message": '无服务'
            }, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
