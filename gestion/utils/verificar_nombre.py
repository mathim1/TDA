from gestion.models import Producto, Detalle_boleta
import random

def verificar_nombre(n,c,d):
    try:
        p = Producto.objects.get(nombre=n)
        print(p.nombre, p.precio)
        m = c * p.precio
        b = Detalle_boleta()
        b.nombre = n
        b.monto = m
        b.cantidad = b.cantidad-c
        b.direccion_venta = d
        b.codigo_barra = random.randint(1,100000)
        b.save()

    except Exception as e:
        print(f"Error: {e}")
    