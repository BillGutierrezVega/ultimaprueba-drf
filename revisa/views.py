from django.shortcuts import render
from .forms import TiendaForm, EmpleadoForm
import requests

# Create your views here.
def ver_datos(request):
    result = requests.get('http://127.0.0.1:8000/empleados/')
    empleados = result.json()
    result = requests.get('http://127.0.0.1:8000/tiendas/')
    tiendas = result.json()
    result = requests.get('http://127.0.0.1:8000/productos/')
    productos = result.json()
    result = requests.get('http://127.0.0.1:8000/clientes/')
    clientes = result.json()
    context = {
        'empleados':empleados, 
        'tiendas':tiendas,
        'productos':productos,
        'clientes':clientes
        }
    return render(request, 'ver_datos.html', context)
    

def crear_tienda(request):
    tienda_formulario = TiendaForm()
    if request.method == 'POST':
        tienda_formulario = TiendaForm(request.POST)
        if tienda_formulario.is_valid():
            tienda_formulario.save()
            nombre = tienda_formulario.cleaned_data['nombre']
            descripcion = tienda_formulario.cleaned_data['descripcion']
            ubicacion = tienda_formulario.cleaned_data['ubicacion']
            nueva_tienda = {
                'nombre':nombre,
                'descripcion':descripcion,
                'ubicacion':ubicacion
            }
            response = requests.post('http://127.0.0.1:8000/tiendas/', json=nueva_tienda)
            if response.status_code == 201:  # 201 significa que la tienda fue creada con éxito
                tienda_formulario = TiendaForm()
            mensaje = 'Tienda creada correctamente!!!'
            context = {
                'tienda_formulario':tienda_formulario, 
                'response':response,
                'mensaje':mensaje
                }
            return render(request, 'crear_tiendas.html', context)
            
    return render(request, 'crear_tiendas.html', {'tienda_formulario':tienda_formulario})


def crear_empleado(request):
    empleado_formulario = EmpleadoForm()
    if request.method == 'POST':
        empleado_formulario = EmpleadoForm(request.POST)
        if empleado_formulario.is_valid():
            empleado_formulario.save()
            nombre = empleado_formulario.cleaned_data['nombre']
            apellido = empleado_formulario.cleaned_data['apellido']
            direccion = empleado_formulario.cleaned_data['direccion']
            edad = empleado_formulario.cleaned_data['edad']
            tienda = empleado_formulario.cleaned_data['tienda']
            nueva_empleado = {
                'nombre':nombre,
                'apellido':apellido,
                'direccion':direccion,
                'edad':edad,
                'tienda':tienda.id
            }
            response = requests.post('http://127.0.0.1:8000/empleados/', json=nueva_empleado)
            if response.status_code == 201:  # 201 significa que la tienda fue creada con éxito
                empleado_formulario = EmpleadoForm()
                mensaje = 'Empleado registrado correctamente!!!'
            else:
                mensaje = 'Empleado no registrado!!!'
            context = {
                'empleado_formulario':empleado_formulario, 
                'response':response,
                'mensaje':mensaje
                }
            return render(request, 'crear_empleado.html', context)
            
    return render(request, 'crear_empleado.html', {'empleado_formulario':empleado_formulario})
