# Generated by Django 5.0.2 on 2024-05-17 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_alter_cliente_numero_telef'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='hora_salida',
        ),
    ]