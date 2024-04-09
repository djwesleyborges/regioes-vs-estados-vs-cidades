from django.contrib.admin.views.decorators import staff_member_required
from ninja import NinjaAPI

from apps.core.api.cidade_api import router as cidade
from apps.core.api.estados_api import router as estado
from apps.core.api.regiao_api import router as regiao

api = NinjaAPI(csrf=True)

api.add_router('/regiao/', regiao)
api.add_router('/estado/', estado)
api.add_router('/cidade/', cidade)
