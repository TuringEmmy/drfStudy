from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.response import Response

"""
APIView study
"""
# /goods/(?<pk>\d+)/
class GoodsView(View):

    def post(self,request,pk):
        """
               self.kwargs: 字典，获取从url地址中提取的所有命名参数
               request: DRF框架封装的Request类的对象
                   request.data: 保存解析之后请求体的数据，相当于Django原始request对象中
                                 request.POST, request.body, request.FILES，并且已
                                 经转换成了字典数据或者类字典数据(QueryDict, OrderedDict)
                   request.query_params: 保存解析之后查询字符串数据，相当于Django原始request对象中
                                 request.GET，并且已经转换成了字典数据或者类字典数据(QueryDict,
                                 OrderedDict)
               response: 直接返回Response类对象，传入原始响应数据，DRF框架会根据客户请求将响应数据转换为
                         对应的数据格式进行返回，客户端可以通过请求头`Accpet`指定所需响应数据格式，DRF框架
                         仅支持返回html和json，默认返回json
               异常处理: 视图出现未处理异常时，DRF框架会最终进行异常处理，并返回给客户端处理之后的出错信息
               认证&权限&限流
               """
        # 抛出异常
        # raise Http404

        # 返回响应
        res_data = {
            'id':1,
            'name':'turing'
        }
        return Response(res_data)