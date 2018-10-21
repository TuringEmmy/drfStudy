# author    python
# time      18-10-21 下午7:53
# project   drtStudy


import os

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "drtStudy.settings")

import django

django.setup()

from user.User import User
from user.UserSerializer_for_main3 import UserSerializer

# 序列化操作
if __name__ == '__main__':
    user = User('Turing', 23, False, '咸阳国际机场')
    #  user = User('Turing', 23, False)            # 这个缺少参数就是错误的,

    print(user)
    serializer = UserSerializer(user, context={
        'a': 1,
        'b': 2
    })
    # print(serializer.errors)
    print(serializer.data)
    print(serializer.context)
