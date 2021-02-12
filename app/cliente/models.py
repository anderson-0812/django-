from django.db import models

from bases.models import ClaseModelo

class Cliente(ClaseModelo):
    nombres = models.CharField(
        max_length=100,
        help_text='Nombres del Cliente',
        unique=False
    )
    apellidos = models.CharField(
        max_length=100,
        help_text='Apellidos del Cliente',
        unique=False
    )
    CiRuc = models.CharField(
        max_length=13,
        help_text='Cedula / Ruc o Pasaporte del Cliente',
        unique=False
    )
    esRucPasaporte = models.BooleanField(default=False)
    direccion = models.CharField(
        max_length=13,
        help_text='Dirección del Cliente',
        unique=False
    )
    representante = models.CharField(
        max_length=100,
        help_text='Representante del Cliente',
        unique=False
    )
    firma_electronica = models.CharField(
        max_length=100,
        help_text='Firma Electronia del Cliente',
        unique=False
    )
    estado = models.BooleanField(default=True)
    ##cuando se haga referencia a ese modelo django por defecto pone un nombre en hexadecima
    ## cuando se cargue el metodo retorne la descripcion
    def __str__(self):
        return '{} {} {} {} {}'.format(self.CiRuc, self.nombres, self.apellidos, self.direccion, self.estado)

    def save(self):
        self.nombres = self.nombres.upper()
        self.apellidos = self.apellidos.upper()
        self.direccion = self.direccion.upper()
        super(Cliente, self).save()
        ##se debe parar a la categoria padre el metodo save

    class Meta:
        verbose_name_plural= "Clientes"
        ##Cuando se refiera  a este modelo en plurar se va a referir a categorias


# class Producto(ClaseModelo):
#     codigo = models.CharField(
#         max_length=20,
#         unique=True
#     )
#     codigo_barra = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=200)
#     precio = models.FloatField(default=0)
#     existencia = models.IntegerField(default=0)
#     ultima_compra = models.DateField(null=True, blank=True)

#     marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
#     unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
#     subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

#     def __str__(self):
#         return '{}'.format(self.descripcion)
    
#     def save(self):
#         self.descripcion = self.descripcion.upper()
#         super(Producto,self).save()
    
#     class Meta:
#         verbose_name_plural = "Productos"
#         unique_together = ('codigo','codigo_barra')
