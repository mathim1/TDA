from gestion.models import User,Password

def loginSinhash(rut, password):
    try:
        user = User.objects.get(rut = rut)
        contra = Password.objects.get(user = user)
        print(user.rut, contra.password_hash)
        if password == contra.password_hash:
            return True
        
        else:
            return False
        
    except Exception as e:
        print(f"Error: {e}")
        return False

