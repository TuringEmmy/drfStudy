from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView


from book07.SelfMixin import MyListModelMixin, MyCreateModelMixin, MyRetrieveModelMixin, MyDestroyModelMixin, \
    MyUpdateModelMixin
from book07.models import BookInfo
from book07.serializers import BookInfoSerializer


class BookListView(MyListModelMixin,
                   MyCreateModelMixin,
                   GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self, request):
        """获取所有"""
        return self.list(request)

    def post(self, request):
        """添加"""
        return self.create(request)


class BookDetailView(MyRetrieveModelMixin,
                     MyDestroyModelMixin,
                     MyUpdateModelMixin,
                     GenericAPIView):
    # 指定当前视图所使用的查询集
    queryset = BookInfo.objects.all()
    # 指定当前视图所使用的序列化器类
    serializer_class = BookInfoSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update()

    def delete(self, request, pk):
        return self.destroy(request, pk)
