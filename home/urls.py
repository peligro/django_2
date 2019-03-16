# -*- coding: utf-8 -*-
from django.urls import path
from home.views import home_inicio

urlpatterns = [
	path('', home_inicio, name="home_inicio"),
	#path('home/',login,name="home_inicio"),
]