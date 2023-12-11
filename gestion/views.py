from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import *
from gestion.models import *
from .utils.verificar_credenciales import verificar_credenciales
from .utils.redireccion import *
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from extra_views import CreateWithInlinesView, InlineFormSetFactory

def listadoProductos(request):
    productos = Producto.objects.all()

    return render(request, 'producto/lista.html', {'productos': productos})

def listadoProductos_emp(request):
    productos = Producto.objects.all()

    return render(request, 'producto/lista_emp.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        form = FormProducto(request.POST)
        if form.is_valid():
            Producto.objects.create(
                nombre=form.cleaned_data['nombre'],
                stock=form.cleaned_data['stock'],
                marca=form.cleaned_data['marca'],
                unidad_medida=form.cleaned_data['unidad_medida'],
                precio=form.cleaned_data['precio']
            )
            return redirect('http://127.0.0.1:8000/productos/')
        else:
            return HttpResponse("Formulario inválido", status=400)
    else:
        form = FormProducto()

    return render(request, 'producto/agregar.html', {'form': form})

def eliminarProducto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('/productos')

#hecho
def actualizarProducto(request, id):
    producto = Producto.objects.get(id=id)
    form = FormProducto(instance=producto)
    if request.method == 'POST':
        form = FormProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/productos/')

    return render(request, 'producto/agregar.html', {'form': form})


# CRUD boleta
'''def listadoBoleta(request):
    boletas = Detalle_boleta.objects.all()

    return render(request, 'boleta/lista.html', {'boletas': boletas})


class DetalleBoletaInline(InlineFormSetFactory):
    model = Detalle_boleta
    form_class = DetalleBoletaForm
    fields = ['cantidad', 'producto', 'monto']
    extra = 1  # Número de formularios DetalleBoleta para mostrar por defecto

class BoletaCreateView(CreateWithInlinesView):
    model = Boleta
    form_class = BoletaForm
    inlines = [DetalleBoletaInline]
    template_name = 'boleta/agregar.html'
    success_url = reverse_lazy('http://127.0.0.1:8000/boletas/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Crear Boleta'
        return context


def actualizarBoleta(request, id):
    boletas = Detalle_boleta.objects.get(id=id)
    detalle_boleta_form = DetalleBoletaForm(instance=boletas)
    if request.method == 'POST':
        detalle_boleta_form = DetalleBoletaForm(request.POST, instance=boletas)
        if detalle_boleta_form.is_valid():
            detalle_boleta_form.save()
        return redirect('http://127.0.0.1:8000/boletas/')

    return render(request, 'boleta/agregar.html', {'detalle_boleta_form': detalle_boleta_form})
'''
def listadoBoleta(request):
    boletas = Boleta.objects.all()

    return render(request, 'boleta/lista.html', {'boletas': boletas})


def crear_boleta(request):
    DetalleBoletaFormSet = inlineformset_factory(Boleta, Detalle_boleta, fields=('cantidad', 'producto', 'monto'), extra=1)

    if request.method == 'POST':
        boleta_form = BoletaForm(request.POST)
        formset = DetalleBoletaFormSet(request.POST)

        if boleta_form.is_valid():
            # Primero, guarda la instancia de Boleta
            boleta = boleta_form.save(commit=False)
            boleta.save()  # Guarda la instancia de Boleta para obtener un ID

            # Luego, maneja los formularios en línea para Detalle_boleta
            formset = DetalleBoletaFormSet(request.POST, instance=boleta)
            if formset.is_valid():
                formset.save()

                # Calcular el valor total después de guardar los Detalle_boleta
                valor_total = sum([detalle.monto for detalle in boleta.detalle_boleta_set.all()])
                boleta.valor = valor_total
                boleta.save()

                return redirect('http://127.0.0.1:8000/boletas/')  

    else:
        boleta_form = BoletaForm()
        formset = DetalleBoletaFormSet()

    return render(request, 'boleta/agregar.html', {
        'boleta_form': boleta_form,
        'formset': formset,
    })    

def actualizarBoleta(request, id):
    boleta = Boleta.objects.get(id=id)
    
    boleta_form = BoletaUpdateForm(instance=boleta)

    if request.method == 'POST':
        boleta_form = BoletaUpdateForm(request.POST, instance=boleta)
        if boleta_form.is_valid():
            boleta_form.save()
            return redirect('http://127.0.0.1:8000/boletas/')

    return render(request, 'boleta/agregar.html', {'boleta_form': boleta_form})


# CRUD factura

'''def listadoFactura(request):
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


def create_detalle_factura(request):
    if request.method == 'POST':
        detalle_factura_form = FormFactura(request.POST)
        if detalle_factura_form.is_valid():
            detalle_factura_form.save()
            return redirect('http://127.0.0.1:8000/facturas/')
    else:
        detalle_factura_form = FormFactura()

    return render(request, 'facturas/agregar.html', {'detalle_factura_form': detalle_factura_form})


def actualizarFactura(request, nro_factura):
    facturas = Detalle_factura.objects.get(nro_factura=nro_factura)
    form = FormFactura(instance=facturas)
    if request.method == 'POST':
        form = FormFactura(request.POST, instance=facturas)
        if form.is_valid():
            form.save()
        return listadoBoleta(request)

    return render(request, 'facturas/agregar.html', {'form': form})'''
    
    

def listadoFactura(request):
    facturas = Factura.objects.all()

    return render(request, 'facturas/lista.html', {'facturas': facturas})


def crear_factura(request):
    DetalleFacturaFormSet = inlineformset_factory(Factura, Detalle_factura, form=DetalleFacturaForm, extra=1)

    if request.method == 'POST':
        Factura_form = FacturaForm(request.POST)
        formset = DetalleFacturaFormSet(request.POST)

        if Factura_form.is_valid():
            factura = Factura_form.save(commit=False)
            factura.save()

            formset = DetalleFacturaFormSet(request.POST, instance=factura)
            if formset.is_valid():
                formset.save()

                valor_total = sum([detalle.precio for detalle in factura.detalle_factura_set.all()])
                factura.valor = valor_total
                factura.save()

                return redirect('http://127.0.0.1:8000/facturas/')  

    else:
        factura_form = FacturaForm()
        formset = DetalleFacturaFormSet()

    return render(request, 'facturas/agregar.html', {
        'factura_form': factura_form,
        'formset': formset,
    })  


def actualizarFactura(request, id):
    factura = Factura.objects.get(id=id)
    
    factura_form = FacturaUpdateForm(instance=factura)

    if request.method == 'POST':
        factura_form = FacturaUpdateForm(request.POST, instance=factura)
        if factura_form.is_valid():
            factura_form.save()
            return redirect('http://127.0.0.1:8000/facturas/')

    return render(request, 'facturas/agregar.html', {'factura_form': factura_form})
    


#empleados
def listadousers(request):
    users = User.objects.all()

    return render(request, 'empleados/lista.html', {'users': users})


def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        password_form = PasswordForm(request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user = user_form.save()
            password = password_form.save(commit=False)
            password.user = user    
            password.save()
            return redirect('http://127.0.0.1:8000/users/')
    else:
        user_form = UserForm()
        password_form = PasswordForm()

    return render(request, 'empleados/agregar.html', {
        'form': user_form,
        'password_form':password_form})




def actualizarUser(request, rut):
    users = User.objects.get(rut = rut)
    form = UserForm(instance=users)
    if request.method == 'POST':
        form = UserForm(request.POST ,instance=users)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/users/')
    

    return render(request, 'empleados/agregar.html',{'form':form})



#inicio

def Interfaz_admin(request):

    return render(request,'Interfaz_usuario_admin.html')

def Interfaz_empleado(request):
    
    return render(request, 'Interfaz_usuario_empleado.html')

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
                    return redirect('http://127.0.0.1:8000/Interfaz_empleado/')
            else:
                messages.error(request, 'Credenciales incorrectas. Por favor, intenta de nuevo.')
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')


def listadoclientes_emp(request):
    clientes = Cliente.objects.all()
    
    return render(request, 'clientes/lista_empleado.html', {'clientes':clientes})

def listadoclientes_admin(request):
    clientes = Cliente.objects.all()
    
    return render(request, 'clientes/lista_admin.html', {'clientes':clientes})

def create_cliente_emp(request):
        if request.method == 'POST':
            form = FormCliente(request.POST)
            if form.is_valid():
                form.save()
                return redirect('http://127.0.0.1:8000/emp_clientes/')

        else:
            form = FormCliente()

        return render(request, 'clientes/agregar.html', {'form': form})
    
def create_cliente_admin(request):
        if request.method == 'POST':
            form = FormCliente(request.POST)
            if form.is_valid():
                form.save()
                return redirect('http://127.0.0.1:8000/admin_clientes/')

        else:
            form = FormCliente()

        return render(request, 'clientes/agregar.html', {'form': form})
    
    
def actualizarCliente(request, id):
    clientes = Cliente.objects.get(id = id)
    form = FormCliente(instance=clientes)
    if request.method == 'POST':
        form = FormCliente(request.POST ,instance=clientes)
        if form.is_valid():
            form.save()
        return redirect('http://127.0.0.1:8000/admin_clientes/')
    
    return render(request, 'clientes/agregar.html', {'form':form})