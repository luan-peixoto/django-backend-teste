from django.core.paginator import Paginator
from django.shortcuts import render

from produto.forms import PesquisaProdutoForm
from produto.models import Produto

def lista_produto(request):
    form = PesquisaProdutoForm(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        lista_de_produtos = Produto.objects\
                                   .filter(nome__icontains=nome)\
                                   .order_by('nome')
        paginator = Paginator(lista_de_produtos, 3)
        pagina = request.GET.get('pagina')
        page_obj = paginator.get_page(pagina)

        print(lista_de_produtos)
        print(page_obj)

        return render(request, 'produto/pesquisa_produto.html', { 'produtos': page_obj,
                                                                  'form': form,
                                                                  'nome': nome })
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar recuperar um produto.')