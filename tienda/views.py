from django.shortcuts import render
from .models import Producto
from .models import Compra
from django.shortcuts import get_object_or_404
from .models import Marca

# Create your views here.

def welcome(request):
    return render(request,'tienda/index.html', {})



def admin(request):
    Productos = Producto.objects.filter()
    return render(request, 'tienda/Productos.html', {'Productos': Productos})

def editar(request, pk):
    Productos = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=Producto)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('editar', pk=post.pk)
    else:
        form = PostForm(instance=Producto)
    return render(request, 'tienda/editar.html', {'Productos': Productos})
def eliminar(request):
    Productos = Producto.objects.all()                                              
    return render(request, 'tienda/editar.html', {})

def nuevo(request):
    Productos = Producto.objects.all()
    return render(request, 'tienda/nuevo.html', {})



def compras(request):
    Compras = Compra.objects.all()
    return render(request, 'tienda/nuevo.html', {})



