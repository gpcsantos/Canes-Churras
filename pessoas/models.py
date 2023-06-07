from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name='Pessoa',
    )
    email = models.CharField(
        max_length=200,
        verbose_name='E-mail'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
