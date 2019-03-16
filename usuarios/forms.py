# -*- coding: utf-8 -*-
from django import forms
from django.forms import  PasswordInput


class Formulario_Usuarios_Login(forms.Form):
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(required=False, widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
