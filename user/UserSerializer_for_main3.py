# author    python
# time      18-10-21 下午7:25
# project   drtStudy
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    """用户序列化器类"""
    name = serializers.CharField(max_length=12,min_length=3,error_messages={
        'min_length':'你给我出来'
    })
    age = serializers.IntegerField()
    gender=serializers.BooleanField()
    address = serializers.CharField()
