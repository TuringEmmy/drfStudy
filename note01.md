### 一、DRF框架简介

Django REST framework能帮助我们简化开发REST API的工作。

### 二、web开发模式

- 前后端不分离(返回HTML网页)
- 前后端分离(只返回数据)

### 三、RestfulAPI设计风格

1. 设计风格

**域名**

```
https://api.example.com
```

**版本**

```
http://www.example.com/api/1.0/foo
```

亦可采用github的方法

```
Accept: vnd.example-com.foo+json; version=1.0
```

**路径**

- 资源作为网址，只能有名词，不能有动词，而且所用的名词往往与数据库的表名对应。
- API中的名词应该使用复数。无论子资源或者所有资源

2. 关键点

用的HTTP动词有下面四个（括号里是对应的SQL命令）。

| 请求方式           | 说明                      |
| -------------- | ----------------------- |
| GET(SELECT)    | 从服务器取出资源(一项或多项)         |
| POST(CREATE)   | 在服务器新建一个资源              |
| PUT(UPDATE)    | 在服务器更新资源(客户端提供改变后的完整资源) |
| DELETE(DELETE) | 从服务器删除资源                |

还有三个不常用的HTTP动词。

| 请求方式          | 说明                       |
| ------------- | ------------------------ |
| PATCH(UPDATE) | 在服务器更新(更新)资源(客户端提供改变的属性) |
| HEAD          | 获取资源的元数据                 |
| OPTIONS       | 获取信息，关于资源的哪些属性是客户端可以改变的  |

**过滤信息**

```
?limit=10：指定返回记录的数量
?offset=10：指定返回记录的开始位置。
?page=2&per_page=100：指定第几页，以及每页的记录数。
?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
```

> 参数的设计允许存在冗余，即允许API路径和URL参数偶尔有重复。比如，GET /zoos/ID/animals 与 GET /animals?zoo_id=ID 的含义是相同的。

**返回结果**

```
GET /collection：返回资源对象的列表（数组）
GET /collection/resource：返回单个资源对象
POST /collection：返回新生成的资源对象
PUT /collection/resource：返回完整的资源对象
PATCH /collection/resource：返回完整的资源对象
DELETE /collection/resource：返回一个空文档
```

### 四、Django自定义RestAPI接口

1. 获取所有图书和新增图书

**获取图书**

```python
def get(self, request):
    # 从数据库中查询所有的图数据
    books = BookInfo.objects.all()

    # 组织数据
    books_list = []

    for book in books:
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'image': book.image.url if book.image else ""
        }
	books_list.append(book_dict)
```

**添加图书**

```python
req_data = request.body
# 注意这里接收到的数据是bytes
json_str = req_data.decode()
# 将字符串转换成python字典
req_dict = json.loads(json_str)

# 获取数据
btitle = req_dict.get('btitle')
bpub_date = req_dict.get('bpub_date')

# 创建一本新图书并添加到数据库
book = BookInfo.objects.create(
    btitle=btitle,
    bpub_date=bpub_date
)
```

2. 获取指定图书更新删除

**更新数据**

```python
# 获取客户传递的参数
req_data = request.body
json_str = req_data.decode()
req_dict  = json.loads(json_str)

# 获取数据
btitle = req_dict.get('btitle')
bpub_date = req_dict.get('bpub_date')

# 更新指定的图书
book.btitle = btitle
book.bpub_date = bpub_date
book.save()
```

**删除数据**

````python
try:
    book = BookInfo.objects.get(pk=pk)
except BookInfo.DoesNotExist:
    return HttpResponse(status=404)

# 删除图书
book.delete()
````

3. RestAPI核心工作说明

在开发REST API的视图中，虽然每个视图具体操作的数据不同，但增、删、改、查的实现流程基本套路化，所以这部分代码也是可以复用简化编写的：

- **增**：校验请求数据 -> 执行反序列化过程 -> 保存数据库 -> 将保存的对象序列化并返回
- **删**：判断要删除的数据是否存在 -> 执行数据库删除
- **改**：判断要修改的数据是否存在 -> 校验请求的数据 -> 执行反序列化过程 -> 保存数据库 -> 将保存的对象序列化并返回
- **查**：查询数据库 -> 将数据序列化并返回

五、DRF框架

1. 功能，特点，环境安装
   - 提供了定义序列化器Serializer的方法，可以快速根据 Django ORM 或者其它库自动序列化/反序列化；
   - 提供了丰富的类视图、Mixin扩展类，简化视图的编写；
   - 丰富的定制层级：函数视图、类视图、视图集合到自动生成 API，满足各种需要；
   - 多种身份认证和权限认证方式的支持；
   - 内置了限流系统；
   - 直观的 API web 界面；
   - 可扩展性，插件丰富

首先在安装django的前提下，安装`pip install djangorestframework`, 并在setting安装`'rest_framework',`,

2. RestAPI接口示例

1) 创建序列化器(新建serializers.py,创建BookInfoSerializer)

```python
class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""
    class Meta:
        model = BookInfo
        fields = '__all__'
```

- **model** 指明该序列化器处理的数据字段从模型类BookInfo参考生成
- **fields** 指明该序列化器包含模型类中的哪些字段，'__all__'指明包含所有字段

2) 编写视图(view视图中创建BookInfoViewSet)

```
class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
```

- **queryset** 指明该视图集在查询数据时使用的查询集
- **serializer_class** 指明该视图在进行序列化或反序列化时使用的序列化器

3) 定义路由

```python
urlpatterns = [
]

router = DefaultRouter()  # 可以处理视图的路由器
router.register('bk', views.BookInfoViewSet, name='bk')  # 向路由器中注册视图集

urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
```

六、序列化器Serializer序列化

1. 作用和基本使用

**serializer不是只能为数据库模型类定义，也可以为非数据库模型类的数据定义。**serializer是独立于数据库之外的存在。

> jango REST framework中的Serializer使用类来定义，须继承自rest_framework.serializers.Serializer。

2. 案例[序列化book对象]

Django REST framework中的Serializer使用类来定义，须继承自rest_framework.serializers.Serializer。

现在以数据库模型类BookInfo为例

```python
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_date = models.DateField(verbose_name='发布日期', null=True)
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    image = models.ImageField(upload_to='booktest', verbose_name='图片', null=True)
```

对上面的模型类进行一个序列化器

```python
class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
```

3. 字段类型选项参数

| 字段                      | 字段构造方式                                   |
| ----------------------- | ---------------------------------------- |
| **BooleanField**        | BooleanField()                           |
| **NullBooleanField**    | NullBooleanField()                       |
| **CharField**           | CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True) |
| **EmailField**          | EmailField(max_length=None, min_length=None, allow_blank=False) |
| **RegexField**          | RegexField(regex, max_length=None, min_length=None, allow_blank=False) |
| **SlugField**           | SlugField(max_length=50, min*length=None, allow_blank=False) 正则字段，验证正则模式 [-a-zA-Z0-9*-]+ |
| **URLField**            | URLField(max_length=200, min_length=None, allow_blank=False) |
| **UUIDField**           | UUIDField(format='hex_verbose') format: 1) `'hex_verbose'` 如`"5ce0e9a5-5ffa-654b-cee0-1238041fb31a"` 2） `'hex'` 如 `"5ce0e9a55ffa654bcee01238041fb31a"` 3）`'int'` - 如: `"123456789012312313134124512351145145114"` 4）`'urn'` 如: `"urn:uuid:5ce0e9a5-5ffa-654b-cee0-1238041fb31a"` |
| **IPAddressField**      | IPAddressField(protocol='both', unpack_ipv4=False, **options) |
| **IntegerField**        | IntegerField(max_value=None, min_value=None) |
| **FloatField**          | FloatField(max_value=None, min_value=None) |
| **DecimalField**        | DecimalField(max_digits, decimal_places, coerce_to_string=None, max_value=None, min_value=None)max_digits: 最多位数decimal_palces: 小数点位置 |
| **DateTimeField**       | DateTimeField(format=api_settings.DATETIME_FORMAT, input_formats=None) |
| **DateField**           | DateField(format=api_settings.DATE_FORMAT, input_formats=None) |
| **TimeField**           | TimeField(format=api_settings.TIME_FORMAT, input_formats=None) |
| **DurationField**       | DurationField()                          |
| **ChoiceField**         | ChoiceField(choices)choices与Django的用法相同  |
| **MultipleChoiceField** | MultipleChoiceField(choices)             |
| **FileField**           | FileField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
| **ImageField**          | ImageField(max_length=None, allow_empty_file=False, use_url=UPLOADED_FILES_USE_URL) |
| **ListField**           | ListField(child=, min_length=None, max_length=None) |
| **DictField**           | DictField(child=)                        |

**选项参数：**

| 参数名称                | 作用       |
| ------------------- | -------- |
| **max_length**      | 最大长度     |
| **min_length**      | 最小长度     |
| **allow_blank**     | 是否允许为空   |
| **trim_whitespace** | 是否截断空白字符 |
| **max_value**       | 最大值      |
| **min_value**       | 最小值      |

**通用参数：**

| 参数名称               | 说明                         |
| ------------------ | -------------------------- |
| **read_only**      | 表明该字段仅用于序列化输出，默认False      |
| **write_only**     | 表明该字段仅用于反序列化输入，默认False     |
| **required**       | 表明该字段在反序列化时必须输入，默认True     |
| **default**        | 序列化和反序列化时使用的默认值            |
| **allow_null**     | 表明该字段是否允许传入None，默认False    |
| **validators**     | 该字段使用的验证器                  |
| **error_messages** | 包含错误编号与错误信息的字典             |
| **label**          | 用于HTML展示API页面时，显示的字段名称     |
| **help_text**      | 用于HTML展示API页面时，显示的字段帮助提示信息 |