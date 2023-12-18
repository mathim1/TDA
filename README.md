# Gestión de Ventas y Clientes para Almacén con Oracle Cloud y Django
Este proyecto es un sistema de gestión de ventas, usuarios y clientes diseñado específicamente para pequeños almacenes. Utiliza Oracle Cloud para la gestión de base de datos y Django para el backend.

## Características
* CRUD (Crear, Leer, Actualizar, Eliminar) de usuarios y clientes.
* Manejo de boletas y facturas.
* Y más.

# Instalación
Sigue estos pasos para configurar el entorno de desarrollo:

* Instalar Django: Django es un framework de alto nivel para el desarrollo web en Python. Para instalarlo, ejecuta el siguiente comando:
`pip install django`

* Instalar cx_Oracle: cx_Oracle es un módulo de Python que permite acceder a Oracle Database. Para instalarlo, utiliza el comando:
`pip install cx_oracle`

* Instalar la librería hashlib: Hashlib se utiliza para el encriptado de contraseñas. Instálalo mediante pip con:
`pip install hashlib`

* Instalar inlineformset_factory: Este componente de Django se utiliza para trabajar con formularios inline. Asegúrate de tenerlo instalado:
`pip install django-extra-views`

* Instalar UUID: UUID se utiliza para la generación de identificadores únicos universales. Instálalo usando pip:
`pip install uuid`

* Realizar las migraciones: Las migraciones son necesarias para configurar la base de datos. Ejecuta el siguiente comando para realizarlas:
`python manage.py migrate`
Ahora el proyecto debe estar listo para ser ejecutado en tu entorno local.




