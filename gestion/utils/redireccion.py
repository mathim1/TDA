from gestion.models import User
from django.shortcuts import render, redirect

def redireccion(rut):
    try:
        u = User.objects.get(rut = rut)
        print(f"rol: {u.role.name}")
        if u.role.name == 'Administrador':
            return True
        elif u.role.name == 'Empleado':
            return False
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return False