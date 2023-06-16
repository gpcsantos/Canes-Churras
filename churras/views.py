from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Prato

# Create your views here.

def index(request):
    pratos = Prato.objects.order_by('-date_prato').filter(publicado=True)
    qtde_pratos_por_pagina = 3
    paginator = Paginator(pratos, qtde_pratos_por_pagina)
    page = request.GET.get('page')
    lista_pratos_pagina = paginator.get_page(page)

    contexto = {
        'lista_pratos' : lista_pratos_pagina,
    }

    return render(request, 'index.html', contexto)

def churrasco(request, prato_id):
    ## Se der tempo no final do curso
    ## trazer a idéia do SLUG, o slugfy e o metodo save no Model 
    prato = get_object_or_404(Prato, pk=prato_id)

    contexto ={
        'prato': prato,
    }

    return render(request, 'churrasco.html', contexto)

def buscar(request):
    pratos = Prato.objects.order_by('-date_prato').filter(publicado=True)

    request_formulario = request.GET
    # print(f'POST : {request.POST}')
    # print(f'GET: {request.GET}')
    if 'buscar' in request_formulario:
        nome_a_buscar = request_formulario['buscar']
        if nome_a_buscar:
            pratos = pratos.filter(nome_prato__icontains=nome_a_buscar)
    
    contexto = {
        'lista_pratos' : pratos,
    }

    return render(request, 'buscar.html', contexto)