from django.db import models

# Create your models here.
from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True
    )

    def _str_(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
        ##se debe parar a la categoria padre el metodo save

    class Meta:
        verbose_name_plural= "Categorias"
        ##Cuando se refiera  a este modelo en plurar se va a referir a categorias