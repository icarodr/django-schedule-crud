from multiprocessing import context
from django.shortcuts import render
from home.models import Agenda
def index(request):
    dados = Agenda.objects.all()
    context = {
        'agenda':dados
    }
    return render(request, 'home/index.html', context)

