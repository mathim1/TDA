#from gestion.models import User
from gestion.models import User, Password
import random

def ingresarUser(n, f, m, r, e, s, rl, p):
    user = User()
    password = Password()
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
    password.password_hash = p.encode('utf-8')
    user.save()
    password.save()

    