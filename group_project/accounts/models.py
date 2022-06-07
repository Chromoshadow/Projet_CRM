from django.db import models

# Create your models here.


class Produits(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.CharField(max_length=200)
    disponibilite = models.CharField(max_length=200)