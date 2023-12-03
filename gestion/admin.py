from django.contrib import admin
from .models import *

# Register your models here.
class PassAdmin(admin.ModelAdmin):
    list_display = ['password_hash','user']

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','rut','role','email']

class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre','stock','marca','unidad_medida','codigo_barra','precio']

admin.site.register(Password,PassAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Producto, ProductosAdmin)