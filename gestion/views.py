from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import *
from gestion.models import *
from .utils.verificar_credenciales import verificar_credenciales
from .utils.verificar_nombre import verificar_nombre
from .utils.ingresarUser import ingresarUser
from .utils.redireccion import *
from .utils.ingresarDef import *
from .utils.loginSinhash import *
from django.contrib import messages


def listadoProductos(request):
    productos = Producto.objects.all()

    return render(request, 'producto/lista.html', {'productos': productos})

#hecho
def agregarProducto(request):
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            n = form.cleaned_data['nombre']
            s = form.cleaned_data['stock']
            m = form.cleaned_data['marca']
            u = form.cleaned_data['unidad_medida']
            p = form.cleaned_data['precio']
            print(n,s,m,u,p)
            ingresar_producto(n,s,m,u,p)
            return redirect('http://127.0.0.1:8000/productos/')

    else:
        form = FormProducto()

    return render(request, 'producto/agregar.html', {'form': form})

#eleminar aun no funciona
#30-11-2023: ahora si xddddddddddddddd
def eliminarProducto(request, codigo_barra):
    producto = Producto.objects.get(codigo_barra=codigo_barra)
    producto.delete()
    return redirect('/productos')

#hecho
def actualizarProducto(request, codigo_barra):
    productos = Producto.objects.get(codigo_barra=codigo_barra)
    form = FormProductoModel(instance=productos)
    if request.method == 'POST':
        form = FormProductoModel(request.POST, instance=productos)
        if form.is_valid():
            form.save()
        return listadoProductos(request)

    return render(request, 'producto/agregar.html', {'form': form})


# CRUD boleta
def listadoBoleta(request):
    facturas = Detalle_boleta.objects.all()

    return render(request, 'boleta/lista.html', {'facturas': facturas})


def agregarBoleta(request):
    if request.method == 'POST':
        form = FormBoleta(request.POST)
        if form.is_valid():
            d = form.cleaned_data['direccion_venta']
            c = form.cleaned_data['cantidad']
            m = form.cleaned_data['monto']
            ingresar_boleta(d,c,m)
            return redirect('http://127.0.0.1:8000/boletas/')

    else:
        form = FormBoleta()

    return render(request, 'boleta/agregar.html', {'form': form})


def actualizarBoleta(request, numero_boleta):
    facturas = Detalle_boleta.objects.get(numero_boleta=numero_boleta)
    form = FormBoleta(instance=facturas)
    if request.method == 'POST':
        form = FormBoleta(request.POST, instance=facturas)
        if form.is_valid():
            form.save()
        return listadoBoleta(request)

    return render(request, 'boleta/agregar.html', {'form': form})

def venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            direccion = form.cleaned_data['direccion_venta']
            cantidad = form.cleaned_data['cantidad']
            nombre = form.cleaned_data['nombre']
            print(direccion, cantidad, nombre)
            verificar_nombre(nombre,cantidad,direccion)
            
    else:
        form = VentaForm()

    return render(request, 'boleta/venta.html', {'form': form})

# CRUD factura

def listadoFactura(request):
    facturas = Detalle_factura.objects.all()

    return render(request, 'facturas/lista.html', {'facturas': facturas})


def agregarFactura(request):
    if request.method == 'POST':
        form = FormFactura(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/facturas/')

    else:
        form = FormFactura()

    return render(request, 'facturas/agregar.html', {'form': form})


def actualizarFactura(request, nro_factura):
    facturas = Detalle_boleta.objects.get(nro_factura=nro_factura)
    form = FormFactura(instance=facturas)
    if request.method == 'POST':
        form = FormFactura(request.POST, instance=facturas)
        if form.is_valid():
            form.save()
        return listadoBoleta(request)

    return render(request, 'facturas/agregar.html', {'form': form})

#empleados
def listadousers(request):
    users = User.objects.all()

    return render(request, 'empleados/lista.html', {'users': users})


def agregarUser(request):
    if request.method == 'POST':
        form = FormUser(request.POST)
        passw = FormIngresoPass(request.POST)
        if form.is_valid() and passw.is_valid():
            n = form.cleaned_data['name']
            f = form.cleaned_data['father_surname']
            m = form.cleaned_data['mother_surname']
            r = form.cleaned_data['rut']
            rl = form.cleaned_data['role']
            e = form.cleaned_data['email']
            s = form.cleaned_data['sueldo']
            p = passw.cleaned_data['password']
            print(p)
            ingresarUser(n, f, m, r, e, s,rl,p)

            return redirect('http://127.0.0.1:8000/users/')

    else:
        form = FormUser()
        passw = FormIngresoPass()

    return render(request, 'empleados/agregar.html', {'form': form, 'passw':passw})

def actualizarUser(request, rut):
    users = User.objects.get(rut = rut)
    form = FormUser(instance=users)
    if request.method == 'POST':
        form = FormUser(request.POST ,instance=users)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/users/')
    

    return render(request, 'empleados/agregar.html',{'form':form})



#inicio

def Interfaz_admin(request):

    return render(request,'Interfaz_usuario_admin.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            password = form.cleaned_data['password']
            if verificar_credenciales(rut, password):
                messages.success(request, 'Inicio de sesión exitoso.')
                redireccion(rut)
                if redireccion(rut) == True:
                    return redirect('http://127.0.0.1:8000/interfaz_admin/')  # Reemplaza 'inicio' con la ruta a donde quieras redirigir al usuario
                
                elif redireccion(rut) == False:
                    return redirect('http://127.0.0.1:8000/Interfaz_usuario_empleado/')
            else:
                messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')