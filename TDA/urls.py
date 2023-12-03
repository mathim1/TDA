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
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('logout/', signout, name='logout'),
    path('interfaz_admin/',Interfaz_admin),
    #productos
    path('productos/',listadoProductos),
    path('agregarProducto/',agregarProducto),
    path('eliminarProducto/<int:codigo_barra>',eliminarProducto),
    path('actualizarProducto/<int:codigo_barra>',actualizarProducto),
    #boletas
    path('boletas/',listadoBoleta),
    path('agregarBoleta/',agregarBoleta),
    path('actualizarBoleta/<int:numero_boleta>',actualizarBoleta),
    path('venta/',venta),
    #facturas
    path('facturas/',listadoFactura),
    path('agregarFactura/',agregarFactura),
    path('actualizarFactura/<int:nro_factura>',actualizarFactura),
    #empleados
    path('users/',listadousers),
    path('agregarUser/',agregarUser),
    path('actualizarUser/<int:rut>',actualizarUser)
    #re_path(r'^articulo/(?P<titulo>[\w\s-]+)/$', views.articulo_detalle, name='articulo_detalle'),
]
