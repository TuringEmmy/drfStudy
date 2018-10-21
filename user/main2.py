# author    python
# time      18-10-21 下午7:43
# project   drtStudy

import os
import os

if not os.environ.get("DJANGO_SETTINGS_MODULE"):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "drtStudy.settings")

import django

django.setup()

if __name__ == '__main__':
    req_date={
        'name':'turing',
        'age':23,
        'gender':False
    }