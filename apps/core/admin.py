from django.contrib import admin
from .models import Cidade, Estado, Regiao

admin.site.register(Regiao)
admin.site.register(Estado)
admin.site.register(Cidade)
