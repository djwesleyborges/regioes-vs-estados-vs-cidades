from django.core.management.base import BaseCommand
from apps.core.models.regiao import Regiao
from apps.core.models.cidade import Cidade
from apps.core.models.estado import Estado


cidades_por_estado = {
    "Norte": {
        "Amazonas": ["Manaus", "Parintins", "Manacapuru"],
        "Pará": ["Belém", "Santarém", "Ananindeua"],
        "Acre": ["Rio Branco", "Cruzeiro do Sul", "Sena Madureira"]
    },
    "Nordeste": {
        "Bahia": ["Salvador", "Feira de Santana", "Vitória da Conquista"],
        "Pernambuco": ["Recife", "Caruaru", "Petrolina"],
        "Ceará": ["Fortaleza", "Caucaia", "Juazeiro do Norte"]
    },
    "Centro-Oeste": {
        "Goiás": ["Goiânia", "Anápolis", "Rio Verde"],
        "Mato Grosso": ["Cuiabá", "Várzea Grande", "Rondonópolis"],
        "Distrito Federal": ["Brasília", "Ceilândia", "Taguatinga"]
    },
    "Sudeste": {
        "São Paulo": ["São Paulo", "Guarulhos", "Campinas"],
        "Rio de Janeiro": ["Rio de Janeiro", "São Gonçalo", "Duque de Caxias"],
        "Minas Gerais": ["Belo Horizonte", "Uberlândia", "Contagem"]
    },
    "Sul": {
        "Paraná": ["Curitiba", "Londrina", "Maringá"],
        "Santa Catarina": ["Florianópolis", "Joinville", "Blumenau"],
        "Rio Grande do Sul": ["Porto Alegre", "Caxias do Sul", "Pelotas"]
    }
}


def adiciona_itens(cidades_por_estado):
    for key, _ in cidades_por_estado.items():
        for estado, cidades in cidades_por_estado[key].items():
            regiao, _ = Regiao.objects.get_or_create(nome=key)
            estado, _ = Estado.objects.get_or_create(nome=estado, regiao=regiao)

            for cidade in cidades:
                cidade, _ = Cidade.objects.get_or_create(nome=cidade, estado=estado)


class Command(BaseCommand):
    help = "Adiciona Regiões, Estados e Cidades."

    def handle(self, *args, **options):
        adiciona_itens(cidades_por_estado)
