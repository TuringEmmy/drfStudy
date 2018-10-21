# author    python
# time      18-10-21 下午3:27
# project   drtStudy
from rest_framework import serializers



# 这个是验证函数
from book_three.models import BookInfo


def control_func(value):
    if 'django' not in value.lower():
        raise serializers.ValidationError("图书不是关于turing的")
    return value



class BookInforSerializer(serializers.Serializer):
    """图书模型学历恶化器类"""

    id = serializers.IntegerField(label="ID")
    # btitle = serializers.CharField(label='标题')
    btitle = serializers.CharField(label='标题',validators=[control_func])

    bpub_date = serializers.DateField(label='出版日期')
    bread = serializers.IntegerField(label="阅读量")
    bcomment  = serializers.IntegerField(label='评论量')
    image = serializers.ImageField(label='封面图片')


    # 重写create父类703行的父类方法
    def create(self,validated_data):
        """validated_data：校验升级后的数据字典"""
        book = BookInfo.object.create(**validated_data)

        return book
