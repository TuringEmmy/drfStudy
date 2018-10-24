from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from book02.models import BookInfo
from book02.serializers import BookInfoSerializer


# 使用DRF框架定义RestAPI接口
# 提供操作图书数据的5个API接口
# 1. 获取所有图书的数据	GET /books/
# 2. 新增一本图书的数据	POST /books/

# 3. 获取指定图书的数据	GET /books/ID/
# 4. 更新指定图书的数据	PUT /books/ID/
# 5. 删除指定图书的数据	DELETE /books/ID/

class BookInfoViewSet(ModelViewSet):
    # 指定当前视图所使用的查询集
    queryset = BookInfo.objects.all()
    # 指定当前视图所使用的序列化
    serializer_class = BookInfoSerializer
    pass