"""drtStudy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('book01.urls')),
    url(r'', include('book02.urls')),
    url(r'', include('book03.urls')),
    url(r'', include('goods.urls')),
    url(r'', include('book04.urls')),
    # url(r'',include('user.urls')),
    url(r'', include('book05.urls')),
    url(r'', include('book06.urls')),
    url(r'', include('book07.urls')),
    url(r'', include('book08.urls')),
    url(r'', include('book09.urls')),
    url(r'', include('book10.urls')),
    url(r'', include('book11.urls')),
    url(r'', include('book12.urls')),
    url(r'', include('book13.urls')),
    url(r'', include('book14.urls')),
    url(r'', include('book15.urls')),
    url(r'', include('book16.urls')),
    url(r'', include('book17.urls')),
    url(r'^docs/', include_docs_urls(title='docs study'))

]
