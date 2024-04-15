from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', api.urls),
    path('', include('apps.core.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
