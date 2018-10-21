# author    python
# time      18-10-21 下午7:34
# project   drtStudy
from django.http import JsonResponse
from django.views import View


class index(View):
    def get(self,request):
        dict={
            'name':"turing"
        }
        return JsonResponse(dict)