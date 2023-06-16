from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# from pessoas.models import Pessoa

# Create your models here.

## criar primeiro a classe Categorias Tem que ser a primeira
## Fazer o MIGRATE
## Rodar comandos SQL
## Corrigir Chave-Estrangeira em PRATOS
## Fazer MIGRATE
class Categoria(models.Model):
    nome_categoria = models.CharField(
        max_length=15,
        verbose_name='Categoria'
    )

    def __str__(self):
        return self.nome_categoria
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"


class Prato(models.Model):
    #não mostrar na primeira implementação
    # escolher uma hora propícia para falar de choices
    # primeira posição será armazenada no Banco, segunda posição será mostrada na combo
    
    # CATEGORIA_CHOICES = (
    #     ('Entradas', 'Entradas'),
    #     ('Churrasco', 'Churrasco'),
    #     ('Sobremesa', 'Sobremesa'),
    # )

    # pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_prato = models.CharField(
        max_length=100,
        verbose_name='Nome do Prato'
        )
    ingredientes = models.TextField(verbose_name='Ingredientes')
    modo_preparo = models.TextField(verbose_name='Modo de Preparo')
    tempo_preparo = models.IntegerField(verbose_name='Tempo de Preparo')
    rendimento = models.CharField(max_length=100, verbose_name="Rendimento")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    date_prato = models.DateTimeField(default=datetime.now, blank=True, 
                                      verbose_name='Data')
    foto_prato = models.ImageField(upload_to='pratos/%Y/%m/%d', blank=True)
    publicado = models.BooleanField(default=False)
    
    ## fazer depois como explicação para o Django-Admin
    def __str__(self):
        return self.nome_prato
    
    class Meta:
        verbose_name = 'Prato'
        verbose_name_plural = 'Pratos'

