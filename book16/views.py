from django.db import DatabaseError

# Create your views here.

from rest_framework.views import APIView


# /index/
class IndexView(APIView):
    def get(self, request):
        # 手动跑出一个异常
        raise DatabaseError

        return Response({'message': 'OK'})
