# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'),name="home"),
    path('usuarios/', include('usuarios.urls')),
    url(r'^api/v1/', include('video.urls')),
]
