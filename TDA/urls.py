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
from gestion.views import BoletaCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('logout/', signout, name='logout'),
    path('interfaz_admin/',Interfaz_admin),
    path('Interfaz_empleado/',Interfaz_empleado),
    #productos
    path('productos/',listadoProductos),
    path('agregarProducto/',crear_producto),
    path('eliminarProducto/<int:id>',eliminarProducto),
    path('actualizarProducto/<int:id>',actualizarProducto),
    #boletas
    path('boletas/',listadoBoleta),
    path('agregarBoleta/',BoletaCreateView.as_view(), name='crear-boleta'),
    path('actualizarBoleta/<int:id>',actualizarBoleta),
    path('venta/',venta),
    #facturas
    path('facturas/',listadoFactura),
    path('agregarFactura/',create_detalle_factura),
    path('actualizarFactura/<int:id>',actualizarFactura),
    #empleados
    path('users/',listadousers),
    path('agregarUser/',create_user),
    path('actualizarUser/<int:id>',actualizarUser)
    #re_path(r'^articulo/(?P<titulo>[\w\s-]+)/$', views.articulo_detalle, name='articulo_detalle'),
]
