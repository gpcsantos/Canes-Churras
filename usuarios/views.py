from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages

from churras.models import Prato

# Create your views here.

def campo_vazio(campo):
    return not campo.strip()
    
def senhas_nao_validadas(senha, senha2):
    return senha != senha2 or len(senha)==0

def cadastro(request):
    if request.method == 'POST':
        
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if campo_vazio(nome):
            print('O campo nome não ficar em branco')
            return redirect('cadastro')
        
        if campo_vazio(email):
            print('O campo email não ficar em branco')
            return redirect('cadastro')

        if senhas_nao_validadas(senha, senha2):
            messages.error(request, 'As senha não são iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        
        messages.success(request, 'Usuário cadastrado com sucesso')

        return redirect('login')
    
    return render(request, 'cadastro.html')


def login(request):
    if request.method == 'POST':
        
        senha = request.POST['senha']
        email = request.POST['email']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')

        print(f'EMAIL: {email} | SENHA: {senha}')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')
        
        messages.error(request, 'Usuário ou senha inválidos')
        return redirect('login')

    return render(request, 'login.html')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        pratos = Prato.objects.filter(pessoa=id)\
            .filter(publicado=True)\
            .order_by('-date_prato')

        contexto = {
            'lista_pratos' : pratos,
        }
        return render(request, 'dashboard.html', contexto)
    
    return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')

def cria_prato(request):
    if request.method == 'POST':
        nome_prato = request.POST['nome-prato']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo-preparo']
        tempo_preparo = request.POST['tempo-preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_prato = request.FILES['foto-prato']

        user = get_object_or_404(User, pk=request.user.id)
        prato = Prato.objects.create(
            pessoa=user,
            nome_prato=nome_prato,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            foto_prato=foto_prato,
            publicado=True,
        )
        prato.save()
        return redirect('dashboard')

    return render(request, 'cria_prato.html')

def deleta_prato(request, prato_id):
    prato = get_object_or_404(Prato, pk=prato_id)
    prato.delete()
    return redirect('dashboard')

def edita_prato(request, prato_id):
    prato = get_object_or_404(Prato, pk=prato_id)
    
    contexto = {
        'prato': prato
    }

    return render(request, 'edita_prato.html', contexto)

def atualiza_prato(request):
    # print(f'METODO: {request.method}')
    if request.method == 'POST':
        prato_id = request.POST['prato_id']
        p = Prato.objects.get(pk=prato_id)
        p.nome_prato = request.POST['nome-prato']
        p.ingredientes = request.POST['ingredientes']
        p.modo_preparo = request.POST['modo-preparo']
        p.tempo_preparo = request.POST['tempo-preparo']
        p.rendimento = request.POST['rendimento']
        p.categoria = request.POST['categoria']
        if 'foto-prato' in request.FILES:
            p.foto_prato = request.FILES['foto-prato']
        p.save()
        return redirect('dashboard')