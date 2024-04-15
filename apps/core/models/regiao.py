from django.db import models
from .cidade import Cidade


class Regiao(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.nome

    def get_estados(self):
        return self.estados.all()

    def get_cidades(self):
        return Cidade.objects.filter(estado__regiao=self)
