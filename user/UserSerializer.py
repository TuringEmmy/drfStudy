# author    python
# time      18-10-21 下午7:25
# project   drtStudy
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """用户序列化器类"""
    name = serializers.CharField()
    age = serializers.IntegerField()
    gender=serializers.BooleanField()
    adress = serializers.CharField()
