# author    python
# time      18-10-22 下午6:13
# project   drtStudy
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin


class MyListCreateAPIView(ListModelMixin,
                          CreateModelMixin,
                          GenericAPIView):
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class MyRetrieveUpdateDestroyAPIView(RetrieveModelMixin,
                                     UpdateModelMixin,
                                     DestroyModelMixin,
                                     GenericAPIView):
    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
