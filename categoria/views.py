from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm

# Listar todas las categorías
def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "categoria/listar.html", {"categorias": categorias})

# Crear una categoría
def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_categorias")
    else:
        form = CategoriaForm()
    return render(request, "categoria/crear.html", {"form": form})

# Editar una categoría
def editar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("listar_categorias")
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, "categoria/editar.html", {"form": form})

# Eliminar una categoría
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect("listar_categorias")
    return render(request, "categoria/eliminar.html", {"categoria": categoria})
