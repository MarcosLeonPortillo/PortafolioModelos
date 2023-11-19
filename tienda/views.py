from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .models import Compra
from .models import Marca
from .forms import cambiarProducto

# Create your views here.

def welcome(request):
    return render(request,'tienda/index.html', {})



def admin(request):
    Productos = Producto.objects.filter()
    return render(request, 'tienda/Productos.html', {'Productos': Productos})


def editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = cambiarProducto(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('productos')
    else:
        form = cambiarProducto(instance=producto)
    return render(request, 'tienda/editar.html', {'form': form, 'pk':pk})



def eliminar(request, pk):
    producto=Producto.objects.filter(pk=pk).delete() 
    return redirect('productos')


def nuevo(request):
    if request.method == 'POST':
        form = cambiarProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = cambiarProducto()
    
    return render(request, 'tienda/nuevo.html', {'form': form})



def compras(request):
    Compras = Compra.objects.all()
    return render(request, 'tienda/nuevo.html', {})



