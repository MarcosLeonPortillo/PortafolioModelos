from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/admin', views.admin, name='admin'),
    path('tienda/admin', views.editar, name="editar")
]


