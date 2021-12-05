from django.shortcuts import render

from produto.models import Produto #importando o bd de produto

from django.core.paginator import Paginator

def lista_produto(request):
    lista_produto = Produto.objects.all().order_by('nome') #recupera todos os produtos

    paginator = Paginator(lista_produto, 2) # (obj a ser paginado, qtd de obj por pag)
    pagina = request.GET.get('pagina') # retorna os objetos da pagina atual
    page_obj = paginator.get_page(pagina) #retorna a pagina 1 do objeto

    print(lista_produto)
    print(page_obj)
    return render(request, "produto/pesquisa_produto.html", {'produtos': page_obj})

def pagina1(request):
    frase = "<b>Está frase está exibida pela pagina pagina1.html de produto</b>"
    return render(request, "produto/pagina1.html", {'frase': frase})

def pagina2(request):
    frase = "<b>Está frase está exibida pela pagina pagina2.html de produto</b>"
    return render(request, "produto/pagina2.html", {'frase': frase})