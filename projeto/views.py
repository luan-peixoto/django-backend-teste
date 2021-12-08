from django.shortcuts import render

def index(request):
    return render(request, "./index.html") # procura na pasta templates o index.html p renderizar

    