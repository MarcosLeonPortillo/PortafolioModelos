from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/admin/productos', views.admin, name='admin'),
    path('tienda/admin/editar/<int:pk>', views.editar, name='editar'),
    path('tienda/admin/eliminar/<int:pk>', views.eliminar, name='eliminar'),
    path('tienda/admin/nuevo', views.nuevo, name='nuevo'),
]


