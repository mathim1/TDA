from django import forms
from .models import *

class FormProducto(forms.Form):
    nombre = forms.CharField(max_length=30)
    stock = forms.IntegerField()
    marca = forms.CharField(max_length=30)
    unidad_medida = forms.IntegerField()
    precio = forms.IntegerField()
    
class FormProductoModel(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class FormBoletaModel(forms.ModelForm):
    class Meta:
        model = Detalle_boleta
        fields = ['direccion_venta','cantidad','monto']

class FormBoleta(forms.Form):
    direccion_venta = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    monto = forms.IntegerField()



class FormFactura(forms.ModelForm):
    class Meta:
        model = Detalle_factura
        fields = ['sitio_compra','nombre_producto','cantidad','precio','proveedor']

class FormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','father_surname','mother_surname','rut','role','email','sueldo']

class FormPass(forms.ModelForm):
    class Meta:
        model = Password
        fields = '__all__'

class FormIngresoPass(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    rut = forms.CharField(label='RUT', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class VentaForm(forms.Form):
    direccion_venta = forms.CharField(max_length=40)
    cantidad = forms.IntegerField()
    nombre = forms.CharField(max_length=40)