from rest_framework import routers

from app_tienda.api.views import *

router = routers.DefaultRouter()
router.register(r'cliente', ClienteViewSet, base_name='clientes')
router.register(r'factura', FacturaViewSet, base_name='facturas')
router.register(r'producto', ProductoViewSet, base_name='productos')
router.register(r'orden-de-compra', OrdenDeCompraViewSet, base_name='orden-de-compra')
router.register(r'categoria', CategoriaViewSet, base_name='categoria')
