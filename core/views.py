from django.shortcuts import render, redirect
from core.models import Evento, Aluno
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


# Create your views here.


def login_user(request):
    return render(request, 'login.html')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos")

    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agendamentos.html', dados)


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            #Realiza a alteração do registro
            #Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                       #data_evento=data_evento,
                                                       # descricao=descricao)
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo=titulo
                evento.data_evento=data_evento
                evento.descricao=descricao
                evento.save()

        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/')


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento_user = Evento.objects.get(id=id_evento)
    if usuario == evento_user.usuario:
        evento_user.delete()
    return redirect('/')


@login_required(login_url='/login/')
def aluno(request):
    return render(request, 'aluno.html')


@login_required(login_url='/login/')
def lista_alunos(request):
    aluno = Aluno.objects.all()
    dados_aluno = {'alunos': aluno}
    return render(request, 'alunos.html', dados_aluno)


@login_required(login_url='/login/')
def submit_aluno(request):
    if request.POST:
        nome = request.POST.get('nome')
        serie = request.POST.get('serie')
        Aluno.objects.create(nome=nome,
                             serie=serie)
    return redirect('/alunos/')
