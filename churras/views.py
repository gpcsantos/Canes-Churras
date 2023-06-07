from django.shortcuts import render, get_object_or_404
from .models import Prato
from django.http import HttpResponse

# Create your views here.

def index(request):
    pratos = Prato.objects.order_by('-date_prato').filter(publicado=True)

    contexto = {
        'lista_pratos' : pratos,
    }

    return render(request, 'index.html', contexto)

def churrasco(request, prato_id):
    prato = get_object_or_404(Prato, pk=prato_id)

    contexto ={
        'prato': prato,
    }

    return render(request, 'churrasco.html', contexto)