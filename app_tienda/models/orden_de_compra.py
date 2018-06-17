from django.db import models
from django.db.models import Count, Sum

from app_tienda.models.producto import Producto
from app_tienda.models.usuario import Persona


class OrdenDeCompra(models.Model):
    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.IntegerField(null=False, blank=False)
    estado_compra = models.BooleanField(null=False, blank=True)

    class Meta:
        unique_together = (('cliente', 'producto'),)

    # @property
    # def count(self):
    #     return OrdenDeCompra.objects.values('producto').annotate(Count('producto'))
    # return City.objects.values('country__name').annotate(Sum('population')).objects.values('producto').annotate(count=Count('producto'))
    # return OrdenDeCompra.objects.filter(producto=self.producto).values('producto').annotate(count=Count('producto'))

    # nombre = models.CharField(blank=False, null=False, max_length=100, unique=True)
    # fecha = models.DateField(blank=False, null=False)
    # producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    # cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)
    #
    # def cantidad(self):
    #     return Producto.objects.filter(id=self.id).count()
    #
    # def precio_total(self):
    #     producto = Producto.objects.filter(id=self.id)
    #     sum = 0.0
    #
    #     for producto_aux in producto:
    #         if producto_aux.descuento is not None:
    #             sum = sum + producto_aux.precio_unitario
    #         else:
    #             sum = sum + (producto_aux.precio_unitario * (producto_aux.descuento / 100))
    #     return sum * self.cantidad()
