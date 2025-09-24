from django.shortcuts import render, redirect, get_object_or_404
from .models import Movimiento
from .forms import MovimientoForm
from producto.models import Producto
from django.contrib import messages

# Listar todos los movimientos
def listar_movimientos(request):
    movimientos = Movimiento.objects.all().order_by('-fecha')
    return render(request, "movimiento/listar.html", {"movimientos": movimientos})

# Crear un movimiento
def crear_movimiento(request):
    if request.method == "POST":
        form = MovimientoForm(request.POST)
        if form.is_valid():
            movimiento = form.save(commit=False)
            producto = movimiento.producto
            # Lógica de stock
            if movimiento.tipo == "ENTRADA":
                producto.stock_actual += movimiento.cantidad
            else:  # SALIDA o MERMA
                if producto.stock_actual - movimiento.cantidad < 0:
                    messages.error(request, "No se puede realizar el movimiento: stock insuficiente.")
                    return redirect("crear_movimiento")
                producto.stock_actual -= movimiento.cantidad

            producto.save()
            movimiento.save()
            return redirect("listar_movimientos")
    else:
        form = MovimientoForm()
    return render(request, "movimiento/crear.html", {"form": form})

# Ver histórico de un producto
def historial_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    movimientos = Movimiento.objects.filter(producto=producto).order_by('-fecha')
    return render(request, "movimiento/historial.html", {"producto": producto, "movimientos": movimientos})

# Editar un movimiento (opcional: actualizar stock también)
def editar_movimiento(request, pk):
    movimiento = get_object_or_404(Movimiento, pk=pk)
    form = MovimientoForm(request.POST or None, instance=movimiento)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("listar_movimientos")
    return render(request, "movimiento/editar.html", {"form": form})

# Eliminar un movimiento (opcional: revertir stock)
def eliminar_movimiento(request, pk):
    movimiento = get_object_or_404(Movimiento, pk=pk)
    if request.method == "POST":
        # Revertir stock antes de eliminar
        producto = movimiento.producto
        if movimiento.tipo == "ENTRADA":
            producto.stock_actual -= movimiento.cantidad
        else:
            producto.stock_actual += movimiento.cantidad
        producto.save()
        movimiento.delete()
        return redirect("listar_movimientos")
    return render(request, "movimiento/eliminar.html", {"movimiento": movimiento})
