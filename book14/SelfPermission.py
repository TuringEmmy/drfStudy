# author    python
# time      18-10-24 下午3:24
# project   drtStudy
from rest_framework.permissions import BasePermission


# 自定义ERF框架的权限控制类
class MyPermission(BasePermission):
    def has_permission(self, request, view, obj):
        """控制用户是否对使用此权限控制类的视图中的某个数据对象有访问权限"""
        return True

    def has_object_permission(self, request, view, obj):
        """控制用户是否使用此权限控制类的视图中的某个数据对象有访问权限"""
        # 需求: id 为1或3的数据对用户可以进行访问,其他的不可以
        if obj.id in (1, 3):
            return True

        return False
