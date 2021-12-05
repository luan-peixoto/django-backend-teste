from django.contrib import admin
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('', views.index, name="index"),
    path("produto/", include('produto.urls')), #quando clicar num link com /produto/, o include vai redirecionar a execucão pro arquivo urls.py da pasta produto
    path('admin/', admin.site.urls),
]


"""
como acessar a página index.html do projeto:
http://127.0.0.1:8000/

como acessar a página index.html de produto:
http://127.0.0.1:8000/produto/
"""