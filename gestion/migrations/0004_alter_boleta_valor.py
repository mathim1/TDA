# Generated by Django 5.0 on 2023-12-06 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_boleta_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]