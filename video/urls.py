# -*- coding: utf-8 -*-
from django.urls import path
from django.conf.urls import url
from .views import ListaVideo, DetalleVideo

urlpatterns = [
	url(r'^videos/$', ListaVideo.as_view(), name="lista-video"),
	url(r'^videos/(?P<pk>[0-9]+)$', DetalleVideo.as_view(), name="detalle-video"),
]