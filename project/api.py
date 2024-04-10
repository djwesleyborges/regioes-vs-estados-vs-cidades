from ninja import NinjaAPI

from apps.core.api.endpoints import router as endpoints

api = NinjaAPI(csrf=True)

api.add_router('/', endpoints)
