# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponseRedirect
from usuarios.forms import Formulario_Usuarios_Login
from django.contrib import messages

def acceso(request):
    form = Formulario_Usuarios_Login(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)	
            return HttpResponseRedirect('/productos')
        else:
            messages.add_message(request, messages.WARNING, 'Los datos ingresados no son correctos, por favor vuelva a intentar ñandú.')
            return HttpResponseRedirect('/usuarios/acceso/')
    return render(request,"usuarios/login.html",{'form': form})


def salir(request):
    logout(request)
    return HttpResponseRedirect('/usuarios/acceso')