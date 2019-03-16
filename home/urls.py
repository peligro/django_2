# -*- coding: utf-8 -*-
from django.urls import path
from home.views import home_inicio, home_nosotros, home_servicios, home_productos, home_contacto, home_upload

urlpatterns = [
	path('', home_inicio, name="home_inicio"),
	path('nosotros/', home_nosotros, name="home_nosotros"),
	path('servicios/', home_servicios, name="home_servicios"),
	path('productos/', home_productos, name="home_productos"),
	path('contacto/', home_contacto, name="home_contacto"),
	path('upload/', home_upload, name="home_upload"),
]