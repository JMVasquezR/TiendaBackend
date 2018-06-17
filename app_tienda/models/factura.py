from django.db import models

from app_tienda.models.orden_de_compra import OrdenDeCompra
from app_tienda.models.usuario import Persona


class Factura(models.Model):
    orden_de_compra = models.ForeignKey(OrdenDeCompra, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Persona, on_delete=models.PROTECT)

    def cantidad_productos(self):
        return OrdenDeCompra.objects.filter(id=self.orden_de_compra).count()

    def precio_total(self):
        producto_orden = OrdenDeCompra.objects.filter(id=self.orden_de_compra)
        suma_precio = 0

        for producto in producto_orden:
            suma_precio += producto.producto.precio_unitario

        return suma_precio
