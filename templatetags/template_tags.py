# -*- coding: utf-8 -*-
from django import template
register = template.Library()


@register.filter(name='ruta_activa')
def ruta_activa(cadena):
    return '%s' % (cadena)

