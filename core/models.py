from django.db import models

class Categoria(models.Model):
    idcategoria = models.IntegerField(primary_key=True, verbose_name="idcategoria")
    nombrecategoria = models.CharField(max_length=50, verbose_name='nombre categoria')

    def __str__(self):
        return self.nombrecategoria
    

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patentes')
    marca = models.CharField(max_length=20, verbose_name='Marca Vehículo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelos')
    categoria = models.ForeignKey(Categoria, on_delete =models.CASCADE)

    def __str__(self):
        return self.patente