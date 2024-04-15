from ninja import Router

from apps.core.api.schemas import RegiaoSchema, EstadoSchema, CidadeSchema
from apps.core.models import Regiao, Estado, Cidade

router = Router()


@router.get('/regiao/', response=list[RegiaoSchema])
def get_todas_regioes(request):
    qs = Regiao.objects.all()
    return qs


@router.get('/regiao/{regiao_id}/estados/', response=list[EstadoSchema])
def get_estados(request, regiao_id: int):
    qs = Regiao.objects.get(id=regiao_id).get_estados()
    return qs


@router.get('/estado/{estado_id}/cidade/', response=list[CidadeSchema])
def get_cidade_by_estado(request, estado_id: int):
    qs = Cidade.objects.filter(estado_id=estado_id)
    return qs


@router.get('/cidade/{cidade_id}/estado/', response=list[EstadoSchema])
def get_estado_by_cidade(request, cidade_id: int):
    qs = Cidade.objects.get(pk=cidade_id).estado
    response = [qs]
    return response


@router.get('/estado/{estado_id}/regiao/', response=list[RegiaoSchema])
def get_regiao_by_estado(request, estado_id: int):
    qs = Estado.objects.get(pk=estado_id).regiao
    response = [qs]
    return response


@router.get('/cidades/', response=list[CidadeSchema])
def get_todas_cidades(request):
    qs = Cidade.objects.all()
    return qs
