from django.contrib import admin
from home.models import Agenda
from home.models import Curso

class detAgenda(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ativo', 'data')
    list_editable = ['ativo',]
    list_per_page = 15
    search_fields = ('nome',)
    list_display_links = ('nome',)
    
admin.site.register(Agenda,detAgenda)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(Curso, CursoAdmin)