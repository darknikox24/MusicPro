# Generated by Django 3.1.2 on 2021-05-20 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201201_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumos',
            name='descripcion',
        ),
    ]