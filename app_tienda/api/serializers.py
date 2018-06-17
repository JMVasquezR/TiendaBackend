from rest_framework import serializers

from app_tienda.models.factura import *
from app_tienda.models.producto import *
from app_tienda.models.usuario import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class OrdenDeCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDeCompra
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
