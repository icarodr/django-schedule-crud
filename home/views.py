from multiprocessing import context
from django.shortcuts import render
from home.models import Agenda
from home.models import Curso

def index(request):
    dados = Agenda.objects.all()
    context = {
        'agenda':dados
    }
    return render(request, 'home/index.html', context)

def home_index(request):

    dadosCurso = Curso.objects.all()
    context = {
        'curso':dadosCurso
    }

    return render(request, 'home/index.html', context)

