from django.contrib import admin

# Register your models here.
from cliente.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'CiRuc','nombres','apellidos','direccion','esRucPasaporte','estado')

admin.site.register(Cliente, ClienteAdmin)
