from django.contrib import admin

# Register your models here.
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'nombre', 'categoria', 'proveedor', 'precio', 'stock_actual')
    search_fields = ('sku', 'nombre')
    list_filter = ('categoria', 'proveedor')
