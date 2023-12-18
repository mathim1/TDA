from django import forms
from .models import *
import hashlib
from django.forms import ModelForm


# forms del producto
class FormProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"


# forms del cliente
class FormCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"


# forms de la boleta
class BoletaForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = "__all__"
        exclude = ["valor"]

class BoletaForm2(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = "__all__"
        exclude = ["valor", "numero_boleta"]


class BoletaUpdateForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = "__all__"
        exclude = ["numero_boleta"]


class DetalleBoletaForm(forms.ModelForm):
    class Meta:
        model = Detalle_boleta
        fields = ["cantidad", "producto", "monto"]


# forms de la factura
class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = "__all__"
        exclude = ["valor"]


class FacturaUpdateForm(forms.ModelForm):
    class Meta:
        model = Boleta
        fields = "__all__"
        exclude = ["nro_factura"]


class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = Detalle_factura
        fields = "__all__"


# forms relacionado al usuario
class LoginForm(forms.Form):
    rut = forms.CharField(label="RUT", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
            "father_surname",
            "mother_surname",
            "rut",
            "role",
            "email",
            "sueldo",
        ]


class PasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Password
        fields = ["password"]

    def save(self, commit=True):
        password_instance = super().save(commit=False)
        password = self.cleaned_data["password"]

        # Hashear la contraseña
        password_hash = hashlib.sha512(password.encode("utf-8")).hexdigest()

        # Convertir el hash a bytes y asignarlo al campo password_hash
        password_instance.password_hash = bytes.fromhex(password_hash)

        if commit:
            password_instance.save()
        return password_instance
