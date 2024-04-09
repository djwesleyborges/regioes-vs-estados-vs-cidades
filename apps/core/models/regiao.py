from django.db import models


class Regiao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    def get_estados(self):
        return self.estados.all()

    def get_cidades(self):
        return [cidade.cidades.all() for cidade in self.estados.all()]
