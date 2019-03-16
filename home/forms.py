# -*- coding: utf-8 -*-
from django import forms


class Formulario_Upload(forms.Form):
    file = forms.FileField(required=False)
    titulo = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}))
    epigrafe = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Epígrafe'}))
