from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=100)
    regiao = models.ForeignKey(
        'Regiao',
        on_delete=models.CASCADE,
        related_name='estados',
    )

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def get_cidades(self):
        return self.cidades.all()
