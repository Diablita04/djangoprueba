from django.db import models

""" STATUS_CHOICES = (
    (1, "SOCIO"),(2, "NO SOCIO")
) """

class Clientes (models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Apellido y Nombre")
    dni=models.BigIntegerField(max_length=200,verbose_name="DNI")
    direccion = models.CharField(max_length=200, verbose_name="Domicilio")
    correo=models.CharField(max_length=200, verbose_name="Correo electronico")
    nombrelibro = models.CharField(max_length=200, verbose_name="Nombre del libro")
    categoria=models.CharField(max_length=200, verbose_name="Categorìa")
    celular=models.BigIntegerField(verbose_name="Numero de Celular")
    fechaPrestamo=models.DateField('Fecha de Creacion',auto_now=True,auto_now_add=False)
    cantidadDias=models.SmallIntegerField('Cantidad de Dìas a Reservar',default=7)
    created = models.DateTimeField(auto_now_add=True)
    updated  =models.DateTimeField(auto_now=True)

class Meta:
    verbose_name="cliente"
    verbose_name_plural = "clientes"
    ordering = ["-created"]
    
def __str__(self):
    return self.nombre