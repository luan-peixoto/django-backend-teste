from django.shortcuts import render

def index(request):
    frase = "<b>Está frase está exibida pela pagina index.html de produto</b>"
    return render(request, "produto/index.html", {'frase': frase})

def pagina1(request):
    frase = "<b>Está frase está exibida pela pagina pagina1.html de produto</b>"
    return render(request, "produto/pagina1.html", {'frase': frase})

def pagina2(request):
    frase = "<b>Está frase está exibida pela pagina pagina2.html de produto</b>"
    return render(request, "produto/pagina2.html", {'frase': frase})