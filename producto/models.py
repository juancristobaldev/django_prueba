from django.db import models
from categoria.models import Categoria
from proveedor.models import Proveedor
# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    stock_actual = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.sku})"