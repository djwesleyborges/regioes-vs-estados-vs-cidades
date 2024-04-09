from ninja import Router, ModelSchema

from apps.core.api.cidade_api import CidadeSchema
from apps.core.models import Estado

router = Router()


class EstadoSchema(ModelSchema):
    class Config:
        model = Estado
        model_fields = '__all__'


class EstadoVsCidadeSchema(ModelSchema):
    cidade: CidadeSchema

    class Config:
        model = Estado
        model_fields = '__all__'


@router.get('/estado/{estado_id}/', response=EstadoSchema)
def get_estados(request, estado_id: int):
    qs = Estado.objects.filter(id=estado_id)
    return qs


@router.get('/estado/{estado_id}/cidade/{cidade_id}', response=EstadoVsCidadeSchema)
def get_cidade_by_estado(request, estado_id: int, cidade_id: int):
    qs = Estado.objects.get(estado_id=estado_id).get_cidades()
    return qs
