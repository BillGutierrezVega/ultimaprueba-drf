from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'empleados', views.EmpleadoViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'tiendas', views.TiendaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]