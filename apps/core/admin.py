from django.contrib import admin
from .models import Cidade, Estado, Regiao


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'regiao')
    search_fields = ('nome',)
    list_filter = ('regiao',)


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'estado')
    search_fields = ('nome',)
    list_filter = ('estado',)


admin.site.register(Regiao)
