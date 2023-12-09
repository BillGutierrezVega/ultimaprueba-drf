from django import forms
from .models import Empleado, Tienda, Cliente, Producto

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = '__all__'
        

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'