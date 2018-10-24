### DRF额外功能

1. #### 认证&权限

**认证Authentication**

DRF框架的默认全局认证方案如下:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',  # session认证
        'rest_framework.authentication.BasicAuthentication',   # 基本认证
    )
}
```

也可以在每个视图中通过设置authentication_classess属性来设置视图的认证方案:

```python
class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
```

配合权限，如果认证失败会有两种可能的返回值：

- 401 Unauthorized 未认证
- 403 Permission Denied 权限被禁止

**权限**

权限控制可以限制用户对于视图的访问和对于具体数据对象的访问。

- 在执行视图的dispatch()方法前，会先进行视图访问权限的判断
- 在通过get_object()获取具体对象时，会进行对象访问权限的判断

DRF框架提供了四个权限控制类:

- AllowAny 允许所有用户
- IsAuthenticated 仅通过认证的用户
- IsAdminUser 仅管理员用户
- IsAuthenticatedOrReadOnly 认证的用户可以完全操作，否则只能get读取

DRF框架的默认权限控制如下:

```python
'DEFAULT_PERMISSION_CLASSES': (
   'rest_framework.permissions.AllowAny', # 允许所有人
)
```

可以在配置文件中设置权限管理类，如:

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated', # 允许认证用户
    )
}
```

还可以视图中通过permission_classes属性来指定某个视图所使用的权限控制类

```python
class ExampleView(APIView):
    permission_classes = [IsAuthenticated]
```

2. #### 自定义权限控制类


> 自定义权限，需继承rest_framework.permissions.BasePermission父类

```python
class MyPermission(BasePermission):
    def has_permission(self, request, view, obj):
        return True

    def has_object_permission(self, request, view, obj):
        # 需求: id 为1或3的数据对用户可以进行访问,其他的不可以
        if obj.id in (1, 3):
            return True
        return False
```


3. #### 限流设置


DRF框架默认没有进行全局限流设置，可以在配置文件中，使用`DEFAULT_THROTTLE_CLASSES` 和 `DEFAULT_THROTTLE_RATES`进行全局配置。

| 可选限流类              | 说明                                       |
| ------------------ | ---------------------------------------- |
| AnonRateThrottle   | 限制所有匿名未认证用户，使用IP区分用户。 使用`DEFAULT_THROTTLE_RATES['anon']` 来设置频次 |
| UserRateThrottle   | 限制认证用户，使用User id 来区分。 使用`DEFAULT_THROTTLE_RATES['user']` 来设置频次 |
| ScopedRateThrottle | 限制用户对于每个视图的访问频次，使用ip或user id。            |

**限流设置**

1）针对匿名用户和认证用户分别进行限流控制

```
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        # 针对未登录(匿名)用户的限流控制类
        'rest_framework.throttling.AnonRateThrottle',
        # 针对登录(认证)用户的限流控制类
        'rest_framework.throttling.UserRateThrottle'
    ),
    # 指定限流频次
    'DEFAULT_THROTTLE_RATES': {
        # 认证用户的限流频次
        'user': '5/minute',
        # 匿名用户的限流频次
        'anon': '3/minute',
    },
}

```

`DEFAULT_THROTTLE_RATES` 可以使用 `second`, `minute`, `hour` 或`day`来指明周期

2）针对匿名用户和认证用户进行统一的限流控制

```
REST_FRAMEWORK = {
    # 针对匿名用户和认证用户进行统一的限流控制
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.ScopedRateThrottle',
    ),

    # 指定限流频次选择项
    'DEFAULT_THROTTLE_RATES': {
        'upload': '3/minute',
        'contacts': '5/minute'
    },
}
```
> 也可以在具体视图中通过throttle_classess属性来配置

4. #### 过滤&排序


添加django-fitlter扩展来增强字段进行过

在配置文件中增加过滤后端的设置：

```python
INSTALLED_APPS = [
    ...
    'django_filters',  # 需要注册应用，
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
```

在视图中添加filter_fields属性，指定可以过滤的字段

```python
class BookListView(ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    filter_fields = ('btitle', 'bread')
```

**排序**

对于列表数据，REST framework提供了**OrderingFilter**过滤器来帮助我们快速指明数据按照指定字段进行排序



在类视图中设置filter_backends，使用`rest_framework.filters.OrderingFilter`过滤器，REST framework会在请求的查询字符串参数中检查是否包含了ordering参数，如果包含了ordering参数，则按照ordering参数指明的排序字段对数据集进行排序。

```python
class Example(ListAPIView):
    queryset =ExampleInfo.objects.all()
    serializer_class = ExampleInfoSerializer
    filter_backends = [OrderingFilter]
```

5. #### 全局分页设置&关闭分页&自定义分页类


配置文件中设置全局的分页方式，如：

```
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS':  '<全局分页类>',
    'PAGE_SIZE': <页容量>  
}
```

**可选分页类**

1） **PageNumberPagination**

前端访问网址形式：

```
GET  http://api.example.org/books/?page=4

```

可以在子类中定义的属性：

- page_size 每页数目
- page_query_param 前端发送的页数关键字名，默认为"page"
- page_size_query_param 前端发送的每页数目关键字名，默认为None
- max_page_size 前端最多能设置的每页数量

2）**LimitOffsetPagination**

前端访问网址形式：

```
GET http://api.example.org/books/?limit=100&offset=400

```

可以在子类中定义的属性：

- default_limit 默认限制，默认值与`PAGE_SIZE`设置一直
- limit_query_param limit参数名，默认'limit'
- offset_query_param offset参数名，默认'offset'
- max_limit 最大limit限制，默认None

**注意：如果在视图内关闭分页功能，只需在视图内设置**

```
pagination_class = None

```

**自定义分页类**

也可通过自定义Pagination类，来为视图添加不同分页行为。在视图中通过`pagination_clas`属性来指明。

```
class StandardResultPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5

class BookListView(ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
    # 指定当前视图所使用的分页类
    pagination_class = StandardResultPagination

```

通过 `http://api.example.org/books/?page=<页码>&page_size=<页容量>` 进行访问。


6. #### DRF框架异常处理


REST framework提供了异常处理，可以出来以下异常：

- APIException 所有异常的父类
- ParseError 解析错误
- AuthenticationFailed 认证失败
- NotAuthenticated 尚未认证
- PermissionDenied 权限决绝
- NotFound 未找到
- MethodNotAllowed 请求方式不支持
- NotAcceptable 要获取的数据格式不支持
- Throttled 超过限流次数
- ValidationError 校验失败

DRF框架的默认异常处理设置如下：

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler'
}
```

**自定义异常处理**

以在DRF框架异常处理函数的基础上，补充一些其他的异常处理，比如数据库处理

```python
def exception_handler(exc, context):
    # 先调用DRF框架的默认异常处理函数
    response = drf_exception_handler(exc, context)

    if response is None:
        view = context['view']
        # 补充数据库的异常处理
        if isinstance(exc, DatabaseError):
            print('[%s]: %s' % (view, type(exc)))
            response = Response({'detail': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
```

在配置文件中声明自定义的异常处理：

```python
REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': '地址.exceptions.exception_handler'
}
```


7. #### 自动生成接口文档


REST framewrok生成接口文档需要`coreapi`库的支持。

```
pip install coreapi
```

注册

```python
urlpatterns = [
    ...
    url(r'^docs/', include_docs_urls(title='My API title'))
]
```

**文档描述说明的定义位置**

1） 单一方法的视图，可直接使用类视图的文档字符串，如

```
class BookListView(generics.ListAPIView):
    """
    返回所有图书信息.
    """

```

2）包含多个方法的视图，在类视图的文档字符串中，分开方法定义，如

```
class BookListCreateView(generics.ListCreateAPIView):
    """
    get:
    返回所有图书信息.

    post:
    新建图书.
    """

```

3）对于视图集ViewSet，仍在类视图的文档字符串中封开定义，但是应使用action名称区分，如

```
class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    list:
    返回图书列表数据

    retrieve:
    返回图书详情数据

    latest:
    返回最新的图书数据

    read:
    修改图书的阅读量
    """
```

然后按照正常网页访问路径

```
浏览器访问 127.0.0.1:8000/docs/，即可看到自动生成的接口文档。
```

#### 两点说明：

1） 视图集ViewSet中的retrieve名称，在接口文档网站中叫做read

2）参数的Description需要在模型类或序列化器类的字段中以help_text选项定义，如：

```python
class BookInfo(models.Model):
    ...
    bread = models.IntegerField(default=0, verbose_name='阅读量', help_text='阅读量')
    ...
```

或

```python
class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = ('bread', )
        extra_kwargs = {
            'bread': {
                'required': True,
                'help_text': '阅读量'
            }
        }
```