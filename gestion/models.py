from django.db import models
import uuid


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_p = models.CharField(max_length=30)
    apellido_m = models.CharField(max_length=30)
    rut = models.IntegerField()
    email = models.EmailField()
    telefono = models.IntegerField()


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    marca = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=50)
    codigo_barra = models.UUIDField(default=uuid.uuid4, unique=True)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Boleta(models.Model):
    direccion_venta = models.CharField(max_length=50, default="")
    fecha_emision = models.DateTimeField(auto_now_add=True)
    numero_boleta = models.UUIDField(default=uuid.uuid4, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Detalle_boleta(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    monto = models.IntegerField(default=0)


class Factura(models.Model):
    sitio_compra = models.CharField(max_length=50)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    nro_factura = models.UUIDField(default=uuid.uuid4, unique=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Detalle_factura(models.Model):
    Factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.IntegerField()


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)


class User(models.Model):
    name = models.CharField(max_length=50)
    father_surname = models.CharField(max_length=50)
    mother_surname = models.CharField(max_length=50)
    rut = models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)


class Password(models.Model):
    password_hash = models.BinaryField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
