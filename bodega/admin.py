from django.contrib import admin

from .models import Bodega
# Register your models here.


@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ubicacion')
    search_fields = ('nombre', 'ubicacion')