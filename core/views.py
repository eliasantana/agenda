from django.shortcuts import render
from core.models import Evento

# Create your views here.


def lista_eventos(request):
    usuario = request.user
    '''evento = Evento.objects.all()'''
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agendamentos.html', dados)
