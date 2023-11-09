from django.shortcuts import render
from .models import Producto
from .models import Compra
from .models import Marca

# Create your views here.

def welcome(request):
    return render(request,'tienda/index.html', {})





def admin(request):
    Productos = Producto.objects.all()
    return render(request, 'tienda/Productos.html', {})

def editar(request):
    Productos = Producto.objects.all()
    return render(request, 'tienda/editar.html', {})

def eliminar(request):
    Productos = Producto.objects.all()
    return render(request, 'tienda/editar.html', {})

def nuevo(request):
    Productos = Producto.objects.all()
    return render(request, 'tienda/nuevo.html', {})





def compras(request):
    Compras = Compra.objects.all()
    return render(request, 'tienda/nuevo.html', {})



