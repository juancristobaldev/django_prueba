from django.urls import path
from .views import listar_categorias, crear_categoria, editar_categoria, eliminar_categoria

urlpatterns = [
    # Listar todas las categorías
    path("", listar_categorias, name="listar_categorias"),

    # Crear nueva categoría
    path("crear/", crear_categoria, name="crear_categoria"),

    # Editar una categoría específica (recibe el id como pk)
    path("editar/<int:pk>/", editar_categoria, name="editar_categoria"),

    # Eliminar una categoría específica (recibe el id como pk)
    path("eliminar/<int:pk>/", eliminar_categoria, name="eliminar_categoria"),
]
