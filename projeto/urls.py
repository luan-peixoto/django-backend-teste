from django.contrib import admin
from django.urls import path, include
from projeto import views

urlpatterns = [
    path('', views.index, name="index"),  # o name server pra qnd o href= "{% url nome_app:nomepath %}"
    path("produtod/", include('produto.urls')), #faz com que eu possa incluir urls do app produto com o endereco 'produto/app' nessa pagina
    path('admin/', admin.site.urls),
]


"""
como acessar a página index.html do projeto:
http://127.0.0.1:8000/

como acessar a página index.html de produto:
http://127.0.0.1:8000/produto/
"""