# -*- coding: utf-8 -*-
from django.shortcuts import render
import django
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import auth
from django.http import Http404, HttpResponseRedirect
from django import forms
from home.models import Productos
from home.forms import Formulario_Upload
from django.contrib import messages
from django.core.files.storage import FileSystemStorage


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


def home_upload(request):
    if request.method == 'POST':
        form = Formulario_Upload(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save('archivo.jpg', myfile)
            uploaded_file_url = fs.url(filename)
            messages.add_message(request, messages.SUCCESS, '<hr />OK OK.')
            return HttpResponseRedirect('/upload')
    else:    
        form = Formulario_Upload(request.POST or None)
    return render(request, "home/upload.html",{'form': form})
