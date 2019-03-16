from django.contrib import admin
from home.models import Productos


class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'titulo', 'epigrafe', 'fecha')
    list_filter = ('id', 'url', 'titulo', 'epigrafe', 'fecha')
    search_fields = ('id', 'url', 'titulo', 'epigrafe', 'fecha')


admin.site.register(Productos, ProductosAdmin)
