# author    python
# time      18-10-21 下午7:27
# project   drtStudy


import os
if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',"drtStudy.settings")



import django
django.setup()

# ------------------------------------虚拟环境设置完成-------------------
if __name__ == '__main__':
    pass