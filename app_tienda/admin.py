from django.contrib import admin

from app_tienda.models.orden_de_compra import OrdenDeCompra
from app_tienda.models.usuario import Cliente

admin.site.register(Cliente)
admin.site.register(OrdenDeCompra)