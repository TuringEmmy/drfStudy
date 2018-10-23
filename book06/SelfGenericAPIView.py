# author    python
# time      18-10-22 下午4:19
# project   drtStudy


"""这是一个自定义的MyGenericAPIView类,具体参看了GenericAPIView"""
from django.http import Http404
from rest_framework.views import APIView


class MyGenericAPIView(APIView):
    # 指定当前视图所使用的查询集,默认为None
    queryset = None
    # 指定当前视图所使用的序列化器类
    serializer_class = None

    # 指定从查询集中获取指定对象时查询字段名称,默认根据pk查询
    lookup_field = 'pk'
    # 指定从url地址中提取的参数的名称
    lookup_url_kwarg = 'pk'

    def get_serializer_class(self):
        """返回当前视图所使用的序列化器类"""
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """创建一个当前视图所使用的序列化器类对象"""

        # 获取当前视图所使用的序列化器类
        serialzer_cls = self.get_serializer_class()

        # 创建一个序列化器类的对象
        return serialzer_cls(*args, **kwargs)

    def get_queryset(self):
        """返回当前视图所使用的查询集"""
        return self.queryset.all()

    def get_object(self):
        """从当前视图所使用的查询集获取指定对象"""

        # 获取当前视图所使用的查询集
        qs = self.get_queryset()

        # 过滤条件========================================
        # filters ={
        #     'pk':self.kwargs['pk']
        # }
        # 过滤条件========================================


        filters = {
            self.lookup_field: self.kwargs[self.lookup_url_kwarg]
        }

        try:
            # 从查询集中获取指定对象
            # obj = qs.get(pk=<pk>)
            obj = qs.get(**filters)
        except Exception as e:
            raise Http404

        return obj
