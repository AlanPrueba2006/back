# Generated by Django 5.1.4 on 2025-07-08 00:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CancelacionReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_cliente', models.TextField(blank=True)),
                ('aceptada_por_admin', models.BooleanField(default=False)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('fecha_respuesta', models.DateTimeField(blank=True, null=True)),
                ('reserva', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reservas.reserva')),
            ],
        ),
    ]
