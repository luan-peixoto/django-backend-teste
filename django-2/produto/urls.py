from django.urls import path
from produto import views

app_name = "produto"

urlpatterns = [
    path('', views.index, name="index"),
    path('paginas/pagina1', views.pagina1, name="pagina1"),
    path('paginas/pagina2/', views.pagina2, name="pagina2")
]