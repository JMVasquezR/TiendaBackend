from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=100, unique=True)
    descripcion = models.CharField(blank=False, null=False, max_length=100, unique=True)


class Producto(models.Model):
    nombre = models.CharField(blank=False, null=False, max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    precio_unitario = models.FloatField(blank=False, null=False)
    descuento = models.FloatField(blank=False, null=False)
