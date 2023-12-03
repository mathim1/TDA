from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    marca = models.CharField(max_length=50)
    unidad_medida = models.IntegerField(default=0)
    codigo_barra = models.AutoField(primary_key=True)
    precio = models.IntegerField(default=0)

    class Meta:
        managed = False


class Boleta(models.Model):
    direccion_venta = models.CharField(max_length=50, default='')
    fecha_emision = models.DateTimeField(auto_now_add=True)
    numero_boleta = models.AutoField(primary_key=True)

    class Meta:
        managed = False


class Detalle_boleta(Boleta):
    ESTADO = [
        ("HABILITADA", 'habilitada'),
        ('DESHABILITADA', 'deshabilitada')
    ]
    cantidad = models.IntegerField(default=0)
    monto = models.IntegerField(default=0)
    '''estado = models.CharField(
        max_length=20,
        choices=ESTADO,
        default='HABILITADA'
    )'''

    class Meta:
        managed = False


class Factura(models.Model):
    sitio_compra = models.CharField(max_length=50)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    nro_factura = models.AutoField(primary_key=True)

    class Meta:
        managed = False


class Detalle_factura(Factura):
    ESTADO = [
        ("HABILITADA", 'habilitada'),
        ('DESHABILITADA', 'deshabilitada')
    ]
    nombre_producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    proveedor = models.CharField(max_length=50)
    
    
    class Meta:
        managed = False


class Role(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        managed = False

    def __int__(self) -> str:
        return self.name
    

class User(models.Model):
    id = models.FloatField(primary_key=True)
    name = models.CharField(max_length=50)
    father_surname = models.CharField(max_length=50)
    mother_surname = models.CharField(max_length=50)
    rut = models.IntegerField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False



class Password(models.Model):
    id = models.FloatField(primary_key=True)
    password_hash = models.BinaryField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        managed = False
