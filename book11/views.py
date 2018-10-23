from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from book11.models import BookInfo
from book11.serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
