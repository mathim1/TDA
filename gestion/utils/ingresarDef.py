from gestion.models import *
import random
from datetime import datetime

def ingresar_producto(n,s,m,u,p):
    c = random.randint(0,10000)
    newproducto = Producto(n,s,m,u,c,p)
    newproducto.save()


def ingresar_boleta(d,c,m):

    f = datetime.now()
    n =  random.randint(0,10000)
    newboleta = Detalle_boleta(d,f,n,c,m)
    newboleta.save()