from django.db import models

# Create your models here.

class Producto (models.Model):
    id_prod = models.AutoField(primary_key=True)
    nom_prod = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='', blank=True , null=True)

    def __str__(self):
        return self.nom_prod
