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
from django.forms import inlineformset_factory
from django.forms import formset_factory
from django.http import JsonResponse
import uuid
from decimal import Decimal


def listadoProductos(request):
    productos = Producto.objects.all()

    return render(request, "producto/lista.html", {"productos": productos})


def listadoProductos_emp(request):
    productos = Producto.objects.all()

    return render(request, "producto/lista_emp.html", {"productos": productos})


def crear_producto(request):
    if request.method == "POST":
        form = FormProducto(request.POST)
        if form.is_valid():
            Producto.objects.create(
                nombre=form.cleaned_data["nombre"],
                stock=form.cleaned_data["stock"],
                marca=form.cleaned_data["marca"],
                unidad_medida=form.cleaned_data["unidad_medida"],
                precio=form.cleaned_data["precio"],
            )
            return redirect("http://127.0.0.1:8000/productos/")
        else:
            return HttpResponse("Formulario inválido", status=400)
    else:
        form = FormProducto()

    return render(request, "producto/agregar.html", {"form": form})


def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect("/productos")


def actualizarProducto(request, id):
    producto = Producto.objects.get(id=id)
    form = FormProducto(instance=producto)
    if request.method == "POST":
        form = FormProducto(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/productos/")

    return render(request, "producto/agregar.html", {"form": form})


# CRUD Boleta
def listadoBoleta(request):
    boletas = Boleta.objects.all()

    return render(request, "boleta/lista.html", {"boletas": boletas})


def crear_boleta(request):
    DetalleBoletaFormSet = inlineformset_factory(
        Boleta, Detalle_boleta, fields=("cantidad", "producto", "monto"), extra=1
    )

    if request.method == "POST":
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
                valor_total = sum(
                    [detalle.monto for detalle in boleta.detalle_boleta_set.all()]
                )
                boleta.valor = valor_total
                boleta.save()

                return redirect("http://127.0.0.1:8000/boletas/")

    else:
        boleta_form = BoletaForm()
        formset = DetalleBoletaFormSet()

    # Aquí obtienes todos los productos de la base de datos
    productos = Producto.objects.all()

    return render(
        request,
        "boleta/agregar.html",
        {
            "boleta_form": boleta_form,
            "formset": formset,
            "productos": productos,  # Agrega los productos al contexto
        },
    )


def actualizarBoleta(request, id):
    boleta = Boleta.objects.get(id=id)

    boleta_form = BoletaUpdateForm(instance=boleta)

    if request.method == "POST":
        boleta_form = BoletaUpdateForm(request.POST, instance=boleta)
        if boleta_form.is_valid():
            boleta_form.save()
            return redirect("http://127.0.0.1:8000/boletas/")

    return render(request, "boleta/agregar.html", {"boleta_form": boleta_form})


# CRUD Factura
def listadoFactura(request):
    facturas = Factura.objects.all()

    return render(request, "facturas/lista.html", {"facturas": facturas})


def crear_factura(request):
    DetalleFacturaFormSet = inlineformset_factory(
        Factura, Detalle_factura, form=DetalleFacturaForm, extra=1
    )

    if request.method == "POST":
        Factura_form = FacturaForm(request.POST)
        formset = DetalleFacturaFormSet(request.POST)

        if Factura_form.is_valid():
            factura = Factura_form.save(commit=False)
            factura.save()

            formset = DetalleFacturaFormSet(request.POST, instance=factura)
            if formset.is_valid():
                formset.save()

                valor_total = sum(
                    [detalle.precio for detalle in factura.detalle_factura_set.all()]
                )
                factura.valor = valor_total
                factura.save()

                return redirect("http://127.0.0.1:8000/facturas/")

    else:
        factura_form = FacturaForm()
        formset = DetalleFacturaFormSet()

    return render(
        request,
        "facturas/agregar.html",
        {
            "factura_form": factura_form,
            "formset": formset,
        },
    )


def actualizarFactura(request, id):
    factura = Factura.objects.get(id=id)

    factura_form = FacturaUpdateForm(instance=factura)

    if request.method == "POST":
        factura_form = FacturaUpdateForm(request.POST, instance=factura)
        if factura_form.is_valid():
            factura_form.save()
            return redirect("http://127.0.0.1:8000/facturas/")

    return render(request, "facturas/agregar.html", {"factura_form": factura_form})


# Empleados
def listadousers(request):
    users = User.objects.all()

    return render(request, "empleados/lista.html", {"users": users})


def create_user(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        password_form = PasswordForm(request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user = user_form.save()
            password = password_form.save(commit=False)
            password.user = user
            password.save()
            return redirect("http://127.0.0.1:8000/users/")
    else:
        user_form = UserForm()
        password_form = PasswordForm()

    return render(
        request,
        "empleados/agregar.html",
        {"form": user_form, "password_form": password_form},
    )


def actualizarUser(request, id):
    users = User.objects.get(id=id)
    form = UserForm(instance=users)
    if request.method == "POST":
        form = UserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/users/")

    return render(request, "empleados/agregar.html", {"form": form})


def eliminarUser(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/users")


# Inicio
def Interfaz_admin(request):
    return render(request, "Interfaz_usuario_admin.html")


def Interfaz_empleado(request):
    return render(request, "Interfaz_usuario_empleado.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data["rut"]
            password = form.cleaned_data["password"]
            if verificar_credenciales(rut, password):
                messages.success(request, "Inicio de sesión exitoso.")
                redireccion(rut)
                if redireccion(rut) == True:
                    return redirect("http://127.0.0.1:8000/interfaz_admin/")

                elif redireccion(rut) == False:
                    return redirect("http://127.0.0.1:8000/Interfaz_empleado/")
            else:
                messages.error(
                    request, "Credenciales incorrectas. Por favor, intenta de nuevo."
                )
                return render(request, "login.html", {"form": form})
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def signout(request):
    logout(request)
    return redirect("http://127.0.0.1:8000/")


def listadoclientes_emp(request):
    clientes = Cliente.objects.all()

    return render(request, "clientes/lista_empleado.html", {"clientes": clientes})


def listadoclientes_admin(request):
    clientes = Cliente.objects.all()

    return render(request, "clientes/lista_admin.html", {"clientes": clientes})


def create_cliente_emp(request):
    if request.method == "POST":
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/emp_clientes/")

    else:
        form = FormCliente()

    return render(request, "clientes/agregar.html", {"form": form})


def create_cliente_admin(request):
    if request.method == "POST":
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/admin_clientes/")

    else:
        form = FormCliente()

    return render(request, "clientes/agregar.html", {"form": form})


def actualizarCliente(request, id):
    clientes = Cliente.objects.get(id=id)
    form = FormCliente(instance=clientes)
    if request.method == "POST":
        form = FormCliente(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/admin_clientes/")

    return render(request, "clientes/agregar.html", {"form": form})


def eliminarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("/admin_clientes")


def venta_productos(request):
    print("Inicio de la función venta_productos")
    DetalleBoletaFormSet = inlineformset_factory(
        Boleta, Detalle_boleta, form=DetalleBoletaForm, extra=1, can_delete=True
    )

    if request.method == "POST":
        print("Método POST detectado")
        boleta_form = BoletaForm2(request.POST)
        detalle_formset = DetalleBoletaFormSet(request.POST)

        print("Datos del formulario de Boleta recibidos:", request.POST)

        if boleta_form.is_valid():
            print("Formulario de Boleta válido")
            boleta = boleta_form.save(commit=False)
            boleta.numero_boleta = uuid.uuid4()  # Forzar la generación del UUID

            # No guardar aún, esperar para asignar el valor total
            detalle_formset = DetalleBoletaFormSet(request.POST, instance=boleta)
            # if detalle_formset.is_valid():
            print("Formulario de Detalle Boleta válido")
            # Temporalmente no guardamos los detalles de la boleta
            # detalle_formset.save()

            # Obtener el valor total de la venta del campo oculto
            valor_total = Decimal(request.POST.get("valor_total_venta", "0.00"))
            boleta.valor = valor_total
            boleta.save()  # Guardar la boleta con el valor total actualizado
            print(f"Boleta creada con ID: {boleta.id} y Valor total: {valor_total}")

            # Opcional: Si deseas guardar los detalles después de actualizar el valor
            # detalle_formset.save()

            return redirect("http://127.0.0.1:8000/Interfaz_empleado/")
            # else:
            # print("Errores en el formulario de Detalle Boleta:", detalle_formset.errors)
        else:
            print("Errores en el formulario de Boleta:", boleta_form.errors)
    else:
        print("Método GET o diferente de POST")
        boleta_form = BoletaForm2()
        detalle_formset = DetalleBoletaFormSet()

    context = {"boleta_form": boleta_form, "detalle_formset": detalle_formset}
    return render(request, "boleta/venta_productos.html", context)


def obtener_precios_productos(request):
    precios = {producto.id: producto.precio for producto in Producto.objects.all()}
    return JsonResponse(precios)
