from django.shortcuts import render

def index(request):
    frase = "<b>Está frase abalblalbelbe</b>"
    return render(request, "index.html", {'frase': frase})