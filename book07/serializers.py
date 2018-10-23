# author    python
# time      18-10-21 下午6:22
# project   drtStudy
from rest_framework import serializers

from book04.models import BookInfo, HeroInfo


class BookInfoSerializer(serializers.ModelSerializer):
    """图书模型序列化器类"""
    class Meta:
        # 指定序列化器对应模型类
        model = BookInfo
        # 指定基于模型类的哪些字段生成序列化器类字段
        # fields = '__all__'
        # fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'image')

        exclude = ('is_delete', )

        extra_kwargs = {
            'bpub_date': {
                'required': False
            },
            'bread': {
                'min_value': 0
            },
            'bcomment': {
                'min_value': 0
            }
        }


class HeroInfoSerializer(serializers.ModelSerializer):
    """英雄模型序列化器类"""
    # hbook = BookInfoSerializer()

    class Meta:
        model = HeroInfo
        # fields = '__all__'

        exclude = ('is_delete', )
        depth = 1