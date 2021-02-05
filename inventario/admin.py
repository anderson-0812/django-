from django.contrib import admin

# Register your models here.
from inventario.models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')

admin.site.register(Categoria, CategoriaAdmin)