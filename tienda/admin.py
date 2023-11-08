from django.contrib import admin
from .models import Cliente, Compra, Marca, Producto

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Marca)
admin.site.register(Producto)

