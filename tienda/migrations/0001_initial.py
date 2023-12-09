# Generated by Django 5.0 on 2023-12-09 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('ubicacion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('edad', models.IntegerField()),
                ('productos', models.ManyToManyField(related_name='productos_comprados', to='tienda.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tiendas',
            field=models.ManyToManyField(related_name='productos', to='tienda.tienda'),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=150)),
                ('edad', models.IntegerField()),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='tienda.tienda')),
            ],
        ),
    ]
