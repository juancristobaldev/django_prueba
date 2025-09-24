from django.contrib import admin

# Register your models here.
from .models import Movimiento

@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'bodega', 'tipo', 'cantidad', 'fecha', 'observacion')
    search_fields = ('producto__nombre', 'bodega__nombre', 'tipo')
    list_filter = ('tipo', 'bodega')