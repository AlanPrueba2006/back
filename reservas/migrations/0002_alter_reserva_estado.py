# Generated by Django 5.1.4 on 2025-07-08 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(choices=[('confirmada', 'Confirmada'), ('cancelacion_solicitada', 'Cancelación solicitada'), ('cancelada', 'Cancelada')], default='confirmada', max_length=30),
        ),
    ]
