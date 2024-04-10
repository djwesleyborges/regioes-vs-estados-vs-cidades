from ninja.orm import create_schema

from apps.core.models import Estado, Cidade, Regiao

RegiaoSchema = create_schema(Regiao)
EstadoSchema = create_schema(Estado)
CidadeSchema = create_schema(Cidade)
