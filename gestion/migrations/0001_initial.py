# Generated by Django 4.2.7 on 2023-12-05 20:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido_p', models.CharField(max_length=30)),
                ('apellido_m', models.CharField(max_length=30)),
                ('rut', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitio_compra', models.CharField(max_length=50)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('nro_factura', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('stock', models.IntegerField(default=0)),
                ('marca', models.CharField(max_length=50)),
                ('unidad_medida', models.IntegerField(default=0)),
                ('codigo_barra', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('precio', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_factura',
            fields=[
                ('factura_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion.factura')),
                ('nombre_producto', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('proveedor', models.CharField(max_length=50)),
            ],
            bases=('gestion.factura',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('father_surname', models.CharField(max_length=50)),
                ('mother_surname', models.CharField(max_length=50)),
                ('rut', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.role')),
            ],
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_hash', models.BinaryField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestion.user')),
            ],
        ),
        
    ]
