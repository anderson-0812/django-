from django.contrib import admin

# Register your models here.
from inv.models import Categoria
from inv.models import SubCategoria
from inv.models import Producto

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion','estado')

class SubcategoriAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria','descripcion','estado')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','descripcion','estado')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(SubCategoria, SubcategoriAdmin)
admin.site.register(Producto, ProductoAdmin)
