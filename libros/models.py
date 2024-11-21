from django.db import models

class Libro(models.Model):
    titulo=models.CharField(max_length=200, verbose_name="Título")
    autor=models.CharField(max_length=200,verbose_name="Autor")
    isbn=models.BigIntegerField(verbose_name="ISBN")
    categoria=models.CharField(max_length=200, verbose_name="Categoría")
    numInvent=models.IntegerField(max_length=200,verbose_name="Número de inventario")
    estado=models.CharField(max_length=200,verbose_name="Estado")
    imagen=models.ImageField(verbose_name="Portada",upload_to="libros")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Meta:
    verbose_name="libro"
    verbose_name_plural = "libros"
    ordering = ["-created"]
    
def __str__(self):
    return self.titulo


