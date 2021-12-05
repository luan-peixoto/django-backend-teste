from django.db import models
from categoria.models import Categoria

# Create your models here.

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    descricao = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100) 
    imagem = models.CharField(max_length=50, blank=True)
    qtd_estoque= models.IntegerField(default=0)
    data_cadastro = models.DateField()
    preco = models.DecimalField(max_digits=5, decimal_places=2, default= 0)
    disponivel = models.BooleanField(default=False)

    class Meta: 
        db_table = 'produto'

    def __str__(self):
        return self.nome

    def get_disponivel(self): # muda o boolean de self pra 'sim' if true e 'nao' if false
        return "Sim" if (self.disponivel) else "Não"