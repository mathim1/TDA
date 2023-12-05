import hashlib
import base64
from gestion.models import User, Password
import random
import os

def ingresarUser(n, f, m, r, e, s, rl, p):
    user = User()
    password = Password()

    # Genera un salt aleatorio de 16 bytes
    salt = hashlib.sha256(os.urandom(16)).hexdigest().encode('ascii')

    # Utiliza hashlib.pbkdf2_hmac para calcular el hash de la contraseña
    password_hash = hashlib.pbkdf2_hmac('sha512', p.encode('UTF-8'), salt, 100000)

    # Utiliza base64 para codificar el hash de la contraseña en una cadena de bytes de 64 bytes
    password_bytes = base64.b64encode(password_hash)[:64]

    user.id = random.randint(0, 1000)
    password.id = user.id
    user.name = n
    user.father_surname = f
    user.mother_surname= m
    user.rut = r
    user.email = e
    user.sueldo = s
    user.role = rl
    password.user = user
    password.password_hash = password_bytes
    user.save()
    password.save()

    