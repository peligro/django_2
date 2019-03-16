# -*- coding: utf-8 -*-
from django.shortcuts import render
import django
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import auth
from django.http import Http404, HttpResponseRedirect
from home.models import Productos


def home_inicio(request):
    django_version = django.VERSION
    base = settings.BASE_DIR
    full_url = get_current_site(request)
    return render(request, "home/home.html",{'django_version': django_version, 'base': django_version})


def home_nosotros(request):
    return render(request, "home/nosotros.html",{})


def home_servicios(request):
    return render(request, "home/servicios.html",{})


def home_productos(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/usuarios/acceso/')
    else:
        productos = Productos.objects.all()
        return render(request, "home/productos.html",{'productos': productos})



def home_contacto(request):
    return render(request, "home/contacto.html",{})