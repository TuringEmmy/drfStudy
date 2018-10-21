# author    python
# time      18-10-21 下午7:27
# project   drtStudy


import os

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "drtStudy.settings")

import django

django.setup()

from user.User import User
from user.UserSerializer import UserSerializer

# ------------------------------------虚拟环境设置完成-------------------
if __name__ == '__main__':
    # 创建User实例对象
    user = User("turing", 23, False,'汉中')

    # 创建一个实例化器类的对象
    serializer = UserSerializer(user)

    # 获取序列化之后的字典

    print(serializer.data)
