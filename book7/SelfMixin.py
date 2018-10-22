# author    python
# time      18-10-22 下午5:19
# project   drtStudy


""" 自定义Mixin扩展类"""
from rest_framework import status
from rest_framework.response import Response


class MyListModelMixin(object):
    def list(self, request, *args, **kwargs):
        """获取一组数据的通用流程"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class MyCreateModelMixin(object):
    def create(self, request, *args, **kwargs):
        """创建一条数据的通用流程"""
        # 反序列化
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MyRetrieveModelMixin(object):
    def retrieve(self, request, *args, **kwargs):
        """获取指定数据"""
        obj = self.get_object()

        serizlizer = self.get_serizalizer(obj)

        return Response(serizlizer.data)


class MyUpdateModelMixin(object):
    def update(self, request, *args, **kwargs):
        obj = self.get_object()

        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(serializer.data)


class MyDestroyModelMixin(object):
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()

        obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
