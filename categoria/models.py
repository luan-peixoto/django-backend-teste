from django.db import models

# Create your models here.
# aqui ficam os modelos (classes e metodos) responsaveis por recuperar dados dos bds

class Categoria(models.Model):
    nome = models.CharField(max_length=70, db_index=True, unique=True)
    slug = models.SlugField(max_length=70) 
    # slug é o texto no fim da pagina html, ex: produtos/produto-1, 'produto-1' é o slug
    class Meta: # metadados da classe categoria
        db_table = 'categoria'
        ordering = ('nome',)

    def __str__(self):
        return self.nome
    # ao definir uma categoria da forma cat = Categoria(nome='aba', slug='bab') ao printar
    # print(cat), esse metodo faz com que o retorno de cat seja a variável nome
    # isso é importante pra algo aí na pagina de admin