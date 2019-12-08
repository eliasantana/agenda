from django.contrib import admin
from core.models import Evento
from core.models import Aluno

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo', 'usuario',)

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'serie')

admin.site.register(Evento, EventoAdmin)

admin.site.register(Aluno)

