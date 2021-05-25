from django.db import models

# Create your models here.



class usuario(models.Model):
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre



categoria_instrumento = [
    [0, "Instrumentos de Cuerdas"],
    [1, "Percusión "],
    [2, "Amplificadores "],
    [3, "Accesorios varios"],
]

tipo_instrumento = [
    [0, "Guitarras "],
    [1, "Bajos "],
    [2, "Pianos "],
    [3, "Baterías Acústicas "],
    [4, "Baterías Electronicas "],
    [5, "Cabezales "],
    [6, "Cajas"],
    [7, "Accesorios varios "],
]


#Este seran los Productos de Music Pro 
class Insumos(models.Model):
    nombre = models.CharField(max_length=125)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    categoria = models.IntegerField(choices=categoria_instrumento)
    tipo = models.IntegerField(choices=tipo_instrumento)
    imagen = models.ImageField(upload_to="insumos", null=True)
    def __str__(self):
        return self.nombre

