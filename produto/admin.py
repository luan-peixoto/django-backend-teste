from django.contrib import admin

# Register your models here.
from .models import Produto
# para poder acessar a tabela categoria no dashboard admin do site precisa desses dois comandos

class ProdutoAdmin(admin.ModelAdmin):
    fields = ('categoria', 'nome', 'slug', 'imagem', 'qtd_estoque', 'preco', 'disponivel')
    # define quais campos vao aparecer na pagina de cadastro de produto (no simbolo +)
    # se não botar isso vao ser todos os campos da entidade
    list_display = [ 'nome', 'categoria', 'slug', 'imagem', 'qtd_estoque', 'preco', 'disponivel'] 
    search_fields = ['nome', 'imagem'] 
    list_filter = ['categoria']
    # exibe um filtro por categoria no lado direito da tela
    list_editable = ['categoria', 'imagem', 'qtd_estoque', 'preco', 'disponivel']
    #campos que podem ser editados
    prepopulated_fields = {'slug': ('nome',)} 


admin.site.register(Produto, ProdutoAdmin)