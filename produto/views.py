from django.core.paginator import Paginator
from django.shortcuts import render

from produto.forms import PesquisaProdutoForm, CadastraProdutoForm
from produto.models import Produto

from django.template.defaultfilters import slugify
from django.contrib import messages


def lista_produto(request):
    form = PesquisaProdutoForm(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        lista_de_produtos = Produto.objects.filter(nome__icontains=nome).order_by('nome')
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


def cadastra_produto(request):

    if request.POST: 
        # quando o formulário de cadastro de produto for submetido (requisição_post)
        cadastra_produto_form = CadastraProdutoForm(request.POST)
        # cria uma instância de cadastro de produto
        if cadastra_produto_form.is_valid:
            # se essa instância for válida
            try:
                # tenta cadastrar o produto no bd, se ele tiver algum erro, está parte será
                # ignorada
                produto_cadastrado = cadastra_produto_form.save(commit=False)
                # cria uma instancia sem salvar no banco de dados
                produto_cadastrado.slug = slugify(produto_cadastrado.nome)
                #adicionau m slug
                produto_cadastrado.save()
                # salva no banco
                messages.add_message(request, messages.INFO, 'Produto Cadastrado com Sucesso!')
                # mensagem de sucesso ao cadastrar produto, para mostrar na pagina html usa
                # if messages

                return render(request, 'produto/exibe_produto.html', {'produto' : produto_cadastrado})
                # renderiza uma outra pagina, a de exibiçao de produto, no mesmo url /cadastra_produto
            except ValueError:
                pass
        else:
            pass
    else:
        # se não for submetido (requisição get)
        cadastra_produto_form = CadastraProdutoForm() 

    return render(request, 'produto/cadastra_produto.html', {'form' : cadastra_produto_form})