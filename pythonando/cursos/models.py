from django.db import models


class Curso(models.Model):
    nome_curso = models.CharField(max_length=40)
    carga_hora = models.IntegerField()
    data_criacao = models.DateTimeField()
    ativo = models.BooleanField(default=True)
