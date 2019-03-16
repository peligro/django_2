# -*- coding: utf-8 -*-
from django.urls import path
from usuarios.views import login

urlpatterns = [
	#path('', home, name="publicaciones_home"),
	path('login/',login,name="usuarios_login"),
]