from django.urls import path
from .views import listar_proveedores, crear_proveedor, editar_proveedor, eliminar_proveedor

urlpatterns = [
    path("", listar_proveedores, name="listar_proveedores"),
    path("crear/", crear_proveedor, name="crear_proveedor"),
    path("editar/<int:pk>/", editar_proveedor, name="editar_proveedor"),
    path("eliminar/<int:pk>/", eliminar_proveedor, name="eliminar_proveedor"),
]