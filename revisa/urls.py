from django.urls import path
from . import views

urlpatterns = [
    path('ver_datos', views.ver_datos, name='ver_datos'),
    path('crear_tienda', views.crear_tienda, name='crear_tienda'),
    path('crear_empleado', views.crear_empleado, name='crear_empleado'),
]