from django import forms
from .models import *
import hashlib
from django.forms import inlineformset_factory

class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
        
class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = '__all__'
    

class DetalleBoletaForm(forms.ModelForm):
    class Meta:
        model = Detalle_boleta
        fields = [ 'cantidad', 'producto', 'monto']
        

    


class FormFactura(forms.ModelForm):
    class Meta:
        model = Detalle_factura
        fields = ['sitio_compra','nombre_producto','cantidad','precio','proveedor']


class LoginForm(forms.Form):
    rut = forms.CharField(label='RUT', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class VentaForm(forms.Form):
    direccion_venta = forms.CharField(max_length=40)
    cantidad = forms.IntegerField()
    nombre = forms.CharField(max_length=40)
    
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'father_surname', 'mother_surname', 'rut', 'role', 'email', 'sueldo']
    
    

class PasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Password
        fields = ['password']

    def save(self, commit=True):
        password_instance = super().save(commit=False)
        password = self.cleaned_data['password']

        # Hashear la contraseña
        password_hash = hashlib.sha512(password.encode('utf-8')).hexdigest()

        # Convertir el hash a bytes y asignarlo al campo password_hash
        password_instance.password_hash = bytes.fromhex(password_hash)

        if commit:
            password_instance.save()
        return password_instance
    
    
