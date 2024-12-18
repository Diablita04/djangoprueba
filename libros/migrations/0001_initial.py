# Generated by Django 4.2.7 on 2023-11-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('autor', models.CharField(max_length=200, verbose_name='Autor')),
                ('isbn', models.CharField(max_length=200, verbose_name='ISBN')),
                ('numInvent', models.CharField(max_length=200, verbose_name='Número de inventario')),
                ('estado', models.CharField(max_length=200, verbose_name='Estado')),
                ('imagen', models.ImageField(upload_to='libros', verbose_name='Portada')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
