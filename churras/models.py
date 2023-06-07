from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

# Create your models here.
class Prato(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_prato = models.CharField(
        max_length=100,
        verbose_name='Nome do Prato'
        )
    ingredientes = models.TextField(verbose_name='Ingredientes')
    modo_preparo = models.TextField(verbose_name='Modo de Preparo')
    tempo_preparo = models.IntegerField(verbose_name='Tempo de Preparo')
    rendimento = models.CharField(max_length=100, verbose_name="Rendimento")
    categoria = models.CharField(max_length=100, verbose_name='Categoria')
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

