# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import Http404, HttpResponseRedirect
#from usuarios.forms import Formulario_Usuarios_Login
from django.contrib import messages

def login(request):
    texto = "hola ñandú"
    return render(request,"usuarios/login.html",{'texto': texto})
