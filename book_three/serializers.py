# author    python
# time      18-10-21 下午3:27
# project   drtStudy
from rest_framework import serializers

from book_three.models import BookInfo


# 这个是验证函数
def control_func(value):
    if 'turing' not in value.lower():
        raise serializers.ValidationError("图书不是关于turing的")
    return value


class BookInforSerializer(serializers.Serializer):
    """图书模型学历恶化器类"""

    id = serializers.IntegerField(label="ID")
    # btitle = serializers.CharField(label='标题')
    btitle = serializers.CharField(label='标题', validators=[control_func])

    bpub_date = serializers.DateField(label='出版日期')
    bread = serializers.IntegerField(label="阅读量")
    bcomment = serializers.IntegerField(label='评论量')
    image = serializers.ImageField(label='封面图片')

    # 重写create父类703行的父类方法
    def create(self, validated_data):
        """validated_data：校验升级后的数据字典"""
        book = BookInfo.object.create(**validated_data)

        return book

    # 重写update方法
    def update(self, instance, validated_data):
        """

        :param instance: 创建序列化器时传入实例对象
        :param validated_data: 教研之后的数据局字典
        :return: 当前这个实例对象
        """
        btitle = validated_data.get('btitle')
        bpub_date = validated_data.get('bpub_date', instance.bpub_date)

        # 更新数据
        instance.btitle = btitle
        instance.bpub_date = bpub_date

        instance.save()

        return instance

    # -------------------------------------------下面进行对单个字段进行比较校验--------------------------------
    def validate_btitle(self, value):
        """此函数会针对btitle的内容进行补偿验证"""
        if 'turing' not in value.lower():
            raise serializers.ValidationError('书籍不是关于turing的')
        return value

    # ---------------------------------------下面进行对多个字段进行比较校验-----------------------------

    def validate(self, attrs):
        """

        :param attrs: 创建序列化器时传入的data数据
        :return:
        """
        bread = attrs['bread']
        bcomment = attrs['bcomment']

        if bread < bcomment:
            raise serializers.ValidationError('图书阅读量必须大于评论量哦')

        return attrs
