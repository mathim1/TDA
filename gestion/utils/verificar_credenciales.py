import hashlib
from gestion.models import User, Password


def verificar_credenciales(rut, password):
    try:
        user = User.objects.filter(rut=rut).first()
        print(f"Usuario obtenido: {user}")

        if user:
            password_record = Password.objects.filter(user=user).first()
            print(f"Registro de contraseña obtenido: {password_record}")

            if password_record:
                stored_password_hash = password_record.password_hash

                # Convierte el hash almacenado a su representación hexadecimal
                stored_password_hash_hex = stored_password_hash.hex()

                print(f"Hash almacenado de la contraseña: {stored_password_hash_hex}")

                input_password_hash = hashlib.sha512(
                    password.encode("utf-8")
                ).hexdigest()
                print(f"Hash de la contraseña ingresada: {input_password_hash}")

                return input_password_hash == stored_password_hash_hex

        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
