from django.urls import path
from produto import views

app_name = "produto"

urlpatterns = [
    path('lista_produto/', views.lista_produto, name="lista_produto"),
    path('paginas/pagina1/', views.pagina1, name="pagina1"),
    path('paginas/pagina2/', views.pagina2, name="pagina2")
]