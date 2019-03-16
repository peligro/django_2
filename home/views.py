# -*- coding: utf-8 -*-
from django.shortcuts import render
import django

def home_inicio(request):
    django_version = django.VERSION
    return render(request, "home/home.html",{'django_version': django_version})
