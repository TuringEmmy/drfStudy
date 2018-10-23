# author    python
# time      18-10-21 下午3:27
# project   drtStudy
from rest_framework import serializers

from book03.models import BookInfo



# 练习关联对象的嵌套序列化(单)
class HeroInfoSerializer(serializers.Serializer):
    """英雄模型序列化器"""
    GENDER_CHOICES=(
        (0,'男'),
        (1,'女')
    )


    # read_only =True 说明只能序列化的时候才能,即往出来区数据的
    id = serializers.IntegerField(label='Id',read_only=True)
    hname = serializers.CharField(label='姓名',max_length=20)
    hgander = serializers.ChoiceField(label='性别',choices=GENDER_CHOICES)
    hcomment = serializers.CharField(label='描述信息',max_length=200,allow_null=True)


    # # 1. 将关联对象序列化为对象主键内容
    # hbook = serializers.PrimaryKeyRelatedField(label='book',read_only=True)
    # # 2. 使用指定的序列化器激昂关联对象进行序列化
    # hbook = BookInforSerializer(label='book')
    # # 3. 将关联对象昂序列化为关联对象昂的模型类的__str__方法的返回值
    #
    # hbook = serializers.StringRelatedField(label='book')




# 这个是验证函数
def control_func(value):
    if 'turing' not in value.lower():
        raise serializers.ValidationError("图书不是关于turing的")
    return value


class BookInforSerializer(serializers.Serializer):
    """图书模型学历恶化器类"""

    id = serializers.IntegerField(label="ID",required=False)
    btitle = serializers.CharField(label='标题')
    # btitle = serializers.CharField(label='标题', validators=[control_func])

    bpub_date = serializers.DateField(label='出版日期')
    bread = serializers.IntegerField(label="阅读量",required=False)
    bcomment = serializers.IntegerField(label='评论量',required=False)
    image = serializers.ImageField(label='封面图片',required=False)

    # 重写create父类703行的父类方法
    def create(self, validated_data):
        """validated_data：校验升级后的数据字典"""
        book = BookInfo.objects.create(**validated_data)

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

    # ----------这个方法会自动带哦用-----------------下面进行对单个字段进行比较校验--------------------------------
    # def validate_btitle(self, value):
    #     """此函数会针对btitle的内容进行补偿验证"""
    #     if 'turing' not in value.lower():
    #         raise serializers.ValidationError('书籍不是关于turing的')
    #     return value

    # -----这个方法会自动调用--------------下面进行对多个字段进行比较校验-----------------------------
    #
    # def validate(self, attrs):
    #     """
    #
    #     :param attrs: 创建序列化器时传入的data数据
    #     :return:
    #     """
    #     bread = attrs['bread']
    #     bcomment = attrs['bcomment']
    #
    #     if bread < bcomment:
    #         raise serializers.ValidationError('图书阅读量必须大于评论量哦')
    #
    #     return attrs



