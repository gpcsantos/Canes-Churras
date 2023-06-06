from django.shortcuts import render
from .models import Prato
from django.http import HttpResponse

# Create your views here.

def index(request):
    pratos = Prato.objects.all()

    contexto = {
        'lista_pratos' : pratos,
    }

    return render(request, 'index.html', contexto)

def churrasco(request):
    return render(request, 'churrasco.html')