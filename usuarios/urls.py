# -*- coding: utf-8 -*-
from django.urls import path
from usuarios.views import acceso, salir

urlpatterns = [
	#path('', acceso, name="usuarios_login_"),
	path('acceso/', acceso, name="usuarios_login"),
	path('salir/', salir, name="usuarios_salir"),
]