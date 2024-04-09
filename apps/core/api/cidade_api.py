from ninja import Router, ModelSchema
from apps.core.models import Cidade

router = Router()


class CidadeSchema(ModelSchema):
    class Config:
        model = Cidade
        model_fields = ('nome', 'estado')


@router.get('/cidade/{cidade_id}/', response=CidadeSchema)
def get_cidades(request, cidade_id: int):
    qs = Cidade.objects.filter(cidade_id=cidade_id)
    return qs
