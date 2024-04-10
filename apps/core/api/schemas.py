from ninja import ModelSchema

from apps.core.models import Estado, Cidade, Regiao


class RegiaoSchema(ModelSchema):
    class Config:
        model = Regiao
        model_fields = '__all__'


class EstadoSchema(ModelSchema):
    class Config:
        model = Estado
        model_fields = '__all__'


class CidadeSchema(ModelSchema):
    class Config:
        model = Cidade
        model_fields = '__all__'
