from django.urls import path
from .views import listar_movimientos, crear_movimiento, historial_producto, editar_movimiento, eliminar_movimiento

urlpatterns = [
    path("", listar_movimientos, name="listar_movimientos"),
    path("crear/", crear_movimiento, name="crear_movimiento"),
    path("editar/<int:pk>/", editar_movimiento, name="editar_movimiento"),
    path("eliminar/<int:pk>/", eliminar_movimiento, name="eliminar_movimiento"),
    path("historial/<int:producto_id>/", historial_producto, name="historial_producto"),
]
