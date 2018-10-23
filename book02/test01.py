# author        TuringEmmy 
# createtime    18-10-19  下午6:19
# coding=utf-8
# doc           PyCharm
# 设置Django的运行所依赖的环境变量
import  os
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drtStudy.settings")


from rest_framework import serializers

class User(object):
    """用户类"""
    def __init__(self,name, age):
        self.name = name
        self.age = age


class UserSerializer(serializers.Serializer):
    """用户序列化器类"""
    name = serializers.CharField()
    age = serializers.IntegerField()


if __name__ == '__main__':
    user = User('Turing',23)


    # 创建一个序列化器类的对象
    serializers = UserSerializer(user)

    # 获取序列化之后的字典数据
    print(serializers.data)