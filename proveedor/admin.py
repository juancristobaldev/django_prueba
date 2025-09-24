from django.contrib import admin

# Register your models here.
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'razon_social', 'rut', 'email', 'telefono')
    search_fields = ('razon_social', 'rut')
    list_filter = ('razon_social',)
