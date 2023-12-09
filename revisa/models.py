from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    edad = models.IntegerField()
    tienda = models.ForeignKey('Tienda', on_delete=models.CASCADE, related_name='empleados')
    
    def __str__(self):
        return self.nombre
    

class Tienda(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    tiendas = models.ManyToManyField('Tienda', related_name='productos')
    
    def __str__(self):
        return self.nombre
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    edad = models.IntegerField()
    productos = models.ManyToManyField(Producto, related_name='productos_comprados')
    
    def __str__(self):
        return self.nombre
    