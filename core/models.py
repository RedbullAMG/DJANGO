from django.db import models

class Categoria(models.Model):
    idcategoria = models.IntegerField(primary_key=True, verbose_name="idcategoria")
    nombrecategoria = models.CharField(max_length=50, verbose_name='nombre categoria')

    def __str__(self):
        return self.nombrecategoria