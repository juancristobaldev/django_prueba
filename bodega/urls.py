from django.urls import path
from .views import listar_bodegas, crear_bodega, editar_bodega, eliminar_bodega

urlpatterns = [
    path("", listar_bodegas, name="listar_bodegas"),
    path("crear/", crear_bodega, name="crear_bodega"),
    path("editar/<int:pk>/", editar_bodega, name="editar_bodega"),
    path("eliminar/<int:pk>/", eliminar_bodega, name="eliminar_bodega"),
]
