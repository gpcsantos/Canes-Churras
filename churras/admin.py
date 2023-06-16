from django.contrib import admin
from .models import Prato, Categoria

# Register your models here.
class ListandoProdutos(admin.ModelAdmin):
    list_display = (
        'id',
        'nome_prato',
        'pessoa',
        'categoria',
        'tempo_preparo',
        'rendimento',
        'publicado',
    )
    list_display_links = (
        'id',
        'nome_prato',
    )
    search_fields = ('nome_prato',)
    list_filter = ('categoria','pessoa',)
    list_per_page = 10
    list_editable = ('publicado','pessoa','categoria',)

admin.site.register(Prato, ListandoProdutos)
admin.site.register(Categoria)

