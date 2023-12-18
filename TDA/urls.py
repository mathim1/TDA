"""TDA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from gestion.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    # vista principal
    path("", login_view, name="login"),
    path("logout/", signout, name="logout"),
    path("interfaz_admin/", Interfaz_admin),
    path("Interfaz_empleado/", Interfaz_empleado),
    # productos
    path("productos/", listadoProductos),
    path("emp_productos/", listadoProductos_emp),
    path("agregarProducto/", crear_producto),
    path("eliminarProducto/<int:id>", eliminarProducto),
    path("actualizarProducto/<int:id>", actualizarProducto),
    # boletas
    path("boletas/", listadoBoleta),
    path("agregarBoleta/", crear_boleta),
    path("actualizarBoleta/<int:id>", actualizarBoleta),
    # path('venta/',venta),
    path("venta/", venta_productos),
    path('obtener-precios-productos/', obtener_precios_productos, name='obtener_precios_productos'),
    # facturas
    path("facturas/", listadoFactura),
    path("agregarFactura/", crear_factura),
    path("actualizarFactura/<int:id>", actualizarFactura),
    # empleados
    path("users/", listadousers),
    path("agregarUser/", create_user),
    path("actualizarUser/<int:id>", actualizarUser),
    path("eliminaruser/<int:id>", eliminarUser),
    # clientes
    path("emp_clientes/", listadoclientes_emp),
    path("admin_clientes/", listadoclientes_admin),
    path("agregarClienteEmp/", create_cliente_emp),
    path("agregarClienteAdmin/", create_cliente_admin),
    path("actualizarCliente/<int:id>", actualizarCliente),
    path("eliminarCliente/<int:id>", eliminarCliente),
]
