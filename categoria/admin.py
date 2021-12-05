from django.contrib import admin

# Register your models here.
from .models import Categoria
# para poder acessar a tabela categoria no dashboard admin do site precisa desses dois comandos

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug'] # mostra oq vai aparecer na listagem de categorias
    search_fields = ['nome', 'slug'] # diz em quais colunas pesquisar ao escrever uma pesquisa
    prepopulated_fields = {'slug': ('nome',)} 
    # automaticamente escreve no campo 'slug' oq esta sendo escrito no campo 'nome' na hora de
    # adicionar uma categoria

admin.site.register(Categoria, CategoriaAdmin)