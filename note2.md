### 一、序列化器Serializer

1. 反序列化使用

   在serializer文件里面

   ````python
   class BookInfoSerializer(serializers.Serializer):
       """图书数据序列化器"""
       id = serializers.IntegerField(label='ID', read_only=True)
       btitle = serializers.CharField(label='名称', max_length=20)
       bpub_date = serializers.DateField(label='发布日期', required=False)
       bread = serializers.IntegerField(label='阅读量', required=False)
       bcomment = serializers.IntegerField(label='评论量', required=False)
       image = serializers.ImageField(label='图片', required=False)
   ````

   is_valid()方法还可以在验证失败时抛出异常serializers.ValidationError，可以通过传递**raise_exception=True**参数开启，REST framework接收到此异常，会向前端返回HTTP 400 Bad Request响应

   ```python
   serializer.is_valid(
               raise_exception=True
           )
   ```

   > ​

2. 选项参数

|                       |           |
| --------------------- | --------- |
| read_only             | 只能获取      |
| label                 |           |
| max_length/min_length | 长度限制      |
| validators            | 单个字段的额外验证 |
| required              | 是否为必填项    |



### 二、序列化操作

1. 序列单个对象和多个对象,只是fields的传入参数不同(参看book_second)


```python
class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化"""

    class Meta:
        model = BookInfo
        # fields = '__all__'
        fields=('id','btitle','bpub_date','bread','bcomment','image')
```


2. 关联对象的嵌套序列化(单)


```python
# 1. 将关联对象序列化为对象主键内容
hbook = serializers.PrimaryKeyRelatedField(label='book',read_only=True)
# 2. 使用指定的序列化器激昂关联对象进行序列化
hbook = BookInforSerializer(label='book')
# 3. 将关联对象昂序列化为关联对象昂的模型类的__str__方法的返回值
hbook = serializers.StringRelatedField(label='book')
```

### 三、反序列化

1. 数据验证


反序列化的结果解释将字典转换成能存入数据库的对象对应main2函数

```python
    req_date = {
        'name': 'turing',
        'age': 23,
        'gender': False,
        # 'address':'han'
    }
    serializer = UserSerializer(data=req_date)
    res = serializer.is_valid()
    print(res)
    print(serializer.errors)
    print(serializer.validated_data)
```


2. 数据验证行为补充


**Validators**

```python
 btitle = serializers.CharField(label='名称', max_length=20, validators=[control_func])
```

其中的`control_func`为不从的验证行为，可以写在该类的上面

```python
def control_func(value):
    if 'turing' not in value.lower():
        raise serializers.ValidationError("图书不是关于Django的")
```

**validate_<field_name>**

对上面的字段进行校验也可以放在该类里面

```python
def validate_btitle(self, value):
        if 'turing' not in value.lower():
            raise serializers.ValidationError("图书不是关于turing的")
        return value
```

**validate**对多个字段进行比较校验（serializers.py）

```python
def validate(self, attrs):
        bread = attrs['bread']
        bcomment = attrs['bcomment']
        if bread < bcomment:
            raise serializers.ValidationError('阅读量小于评论量')
        return attrs
```

> 注意上面的三个方法当中，在类里面的会自动调用哦！！！


3. 书保存create和update方法实现


这个只是重写了Serializer里面的create和update的方法，在使用serizlizer之后，更新和创建都适用save函数

```python
 def create(self, validated_data):
        """validated_data：校验升级后的数据字典"""
        book = BookInfo.objects.create(**validated_data)

        return book
```

`validated_data`是校验过的数据


4. 额外参数传递和partial序列化器类


```python
serializer = UserSerializer(user, context={
        'a': 1,
        'b': 2
    })
```

在进行数据序列化的是时候，多加一个参数`context`

### 四、案例

DRF为我们提供了ModelSerializer模型类序列化器来帮助我们快速创建一个Serializer类。

ModelSerializer与常规的Serializer相同，但提供了：

- 基于模型类自动生成一系列字段
- 包含默认的create()和update()的实现

1. 使用序列器改写RestAPI接口


```python

class BookInfoSerializer(serializers.ModelSerializer):
    """图书模型序列化器类"""
    class Meta:
        # 指定序列化器对应模型类
        model = BookInfo
        # 指定基于模型类的哪些字段生成序列化器类字段
        # fields = '__all__'
        # fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'image')
```

- 使用**fields**来明确字段，`__all__`表名包含所有字段
- 使用**exclude**可以明确排除掉哪些字段
- 默认ModelSerializer使用主键作为关联字段，但是我们可以使用**depth**来简单的生成嵌套表示，depth应该是整数，表明嵌套的层级数量` depth = 1`

```python
HeroInfoSerializer():
    id = IntegerField(label='ID', read_only=True)
    hname = CharField(label='名称', max_length=20)
    hgender = ChoiceField(choices=((0, 'male'), (1, 'female')), label='性别', required=False, validators=[<django.core.valators.MinValueValidator object>, <django.core.validators.MaxValueValidator object>])
    hcomment = CharField(allow_null=True, label='描述信息', max_length=200, required=False)
    hbook = NestedSerializer(read_only=True):
        id = IntegerField(label='ID', read_only=True)
        btitle = CharField(label='名称', max_length=20)
        bpub_date = DateField(allow_null=True, label='发布日期', required=False)
        bread = IntegerField(label='阅读量', max_value=2147483647, min_value=-2147483648, required=False)
        bcomment = IntegerField(label='评论量', max_value=2147483647, min_value=-2147483648, required=False)
        image = ImageField(allow_null=True, label='图片', max_length=100, required=False)
```

- 显示指明字段`fields = ('id', 'btitle', 'bpub_date'， 'bread', 'bcomment')`

- 指明只读字段`read_only_fields = ('id', 'bread', 'bcomment')`

- 添加额外参数

  ```python
  extra_kwargs = {            
      'bread': {'min_value': 0, 'required': True},            
      'bcomment': {'min_value': 0, 'required': True},        
  }
  ```


2. 视图类APIView视图类的使用(Request和response)


```python
class BookListView(APIView):
    def get(self,request):
        books = BookInfo.objects.all()
        # 序列,因为序列的结构是字典
        serializer =BookInfoSerializer(books,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = BookInfoSerializer(data=request.data)
        serializer.is_valid(
            raise_exception=True
        )
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
```

