from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Create your models here.
class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)