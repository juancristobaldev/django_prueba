from django.shortcuts import render, redirect, get_object_or_404
from .models import Bodega
from .forms import BodegaForm

# Listar bodegas
def listar_bodegas(request):
    bodegas = Bodega.objects.all()
    return render(request, "bodega/listar.html", {"bodegas": bodegas})

# Crear bodega
def crear_bodega(request):
    if request.method == "POST":
        form = BodegaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_bodegas")
    else:
        form = BodegaForm()
    return render(request, "bodega/crear.html", {"form": form})

# Editar bodega
def editar_bodega(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    if request.method == "POST":
        form = BodegaForm(request.POST, instance=bodega)
        if form.is_valid():
            form.save()
            return redirect("listar_bodegas")
    else:
        form = BodegaForm(instance=bodega)
    return render(request, "bodega/editar.html", {"form": form})

# Eliminar bodega
def eliminar_bodega(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    if request.method == "POST":
        bodega.delete()
        return redirect("listar_bodegas")
    return render(request, "bodega/eliminar.html", {"bodega": bodega})
