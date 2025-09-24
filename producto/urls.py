from django.urls import path
from .views import listar_productos, crear_producto, editar_producto, eliminar_producto

urlpatterns = [
    path("", listar_productos, name="listar_productos"),
    path("crear/", crear_producto, name="crear_producto"),
    path("editar/<int:pk>/", editar_producto, name="editar_producto"),
    path("eliminar/<int:pk>/", eliminar_producto, name="eliminar_producto"),
]
