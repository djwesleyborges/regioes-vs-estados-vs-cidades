from ninja import Router, ModelSchema

from apps.core.models import Regiao, Estado, Cidade

router = Router()


class RegiaoSchema(ModelSchema):
    class Config:
        model = Regiao
        model_fields = ('nome',)


class EstadoSchema(ModelSchema):

    class Config:
        model = Estado
        model_fields = '__all__'


class CidadeSchema(ModelSchema):
    class Config:
        model = Cidade
        model_fields = ('nome', 'estado')


@router.get('/regiao/{regiao_id}/', response=list[RegiaoSchema])
def get_regiao(request, regiao_id: int):
    qs = Regiao.objects.filter(id=regiao_id)
    return qs


@router.get('/regiao/{regiao_id}/estados/', response=list[EstadoSchema])
def get_estados(request, regiao_id: int):
    qs = Regiao.objects.get(id=regiao_id).get_estados()
    return qs


@router.get('/estado/{estado_id}/cidade/', response=list[CidadeSchema])
def get_cidade_by_estado(request, estado_id: int):
    qs = Cidade.objects.filter(estado_id=estado_id)
    return qs
