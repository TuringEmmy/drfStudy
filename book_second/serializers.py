# author        TuringEmmy 
# createtime    18-10-19  下午5:54
# coding=utf-8
# doc           PyCharm
from rest_framework import serializers

from book_first.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化"""

    class Meta:
        model = BookInfo
        fields = '__all__'
