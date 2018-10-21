# author    python
# time      18-10-21 下午7:43
# project   drtStudy

import os

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "drtStudy.settings")

import django

django.setup()

from user.UserSerializer import UserSerializer


# 这个是反序列化
if __name__ == '__main__':
    req_date = {
        'name': 'turing',
        'age': 23,
        'gender': False,
        # 'address':'han'
    }

    # 创建学历恶化对象
    serializer = UserSerializer(data=req_date)

    # 校验数据,成功返回True
    res = serializer.is_valid()
    print(res)
    # 这里吧address备注,会出现数据不玩真,就会打印False

    # 获取校验失败的数据
    print(serializer.errors)
    # -----------------------------上线这两个代码的结果是相反的-------------------------------------
    # 如果校验成功:错误信息为空
    # 获取校验后的数据
    print(serializer.validated_data)
