from django.db import models

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    discipina  = models.CharField(max_length=200)
    nome_mae  = models.CharField(max_length=200, null=True, blank=True)