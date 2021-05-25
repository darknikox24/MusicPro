# Generated by Django 3.1.2 on 2021-05-20 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210519_2352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insumos',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='insumos',
            name='categoria',
            field=models.IntegerField(choices=[[0, 'Instrumentos de Cuerdas'], [1, 'Percusión '], [2, 'Amplificadores '], [3, 'Accesorios varios']], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='insumos',
            name='tipo',
            field=models.IntegerField(choices=[[0, 'Guitarras '], [1, 'Bajos '], [2, 'Pianos '], [3, 'Baterías Acústicas '], [4, 'Baterías Acústicas '], [5, 'Cabezales '], [6, 'Cajas'], [7, 'Accesorios varios ']], default=0),
            preserve_default=False,
        ),
    ]