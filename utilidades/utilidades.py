from django import template

register = template.Library()

def retornaTexto(texto1,texto2):
    return '%s | %s' % (texto1, texto2)

def baseURL():
    return 'http://192.168.0.2:8000/'

def retornaTexto2(texto):
    return 'valor texto'



