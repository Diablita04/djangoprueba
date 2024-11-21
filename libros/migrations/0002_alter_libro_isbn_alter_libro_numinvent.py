# Generated by Django 4.2.7 on 2023-11-19 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.BigIntegerField(verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='numInvent',
            field=models.IntegerField(max_length=200, verbose_name='Número de inventario'),
        ),
    ]
