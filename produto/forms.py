from django import forms

from produto.models import Produto
from categoria.models import Categoria
from projeto import settings

from django.core.validators import RegexValidator

class PesquisaProdutoForm(forms.Form):

    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
        required=False)

    # <input type="text" name="nome" id="id_nome" class="form-control form-control-sm" maxlength="100">


class CadastraProdutoForm(forms.ModelForm):
    # quando é feito um formulário de entrada de dados para um modelo (uma tabela do bd)
    # é necessário usar forms.ModelForm
    class Meta:
        model = Produto
        fields = ('nome', 'descricao', 'categoria', 'data_cadastro', 'preco', 'qtd_estoque', 'imagem', 'disponivel')
        # localized_fields = ('preco',) só é necessário se for feito pela forma comentada

    """ OUTRA FORMA DE ADICIONAR OS CAMPOS (SEM PRECISAR DE ARGUMENTOS QUE JA EXISTEM)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={'required': 'Campo obrigatório.',
                                            'unique': 'Nome de produto duplicado.'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['descricao'].error_messages={'required': 'Campo obrigatório'}
        self.fields['descricao'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['categoria'].error_messages={'required': 'Campo obrigatório'}
        self.fields['categoria'].queryset=Categoria.objects.all().order_by('nome')
        self.fields['categoria'].empty_label='--- Selecione uma categoria ---'
        self.fields['categoria'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['data_cadastro'].error_messages={'required': 'Campo obrigatório'}
        self.fields['data_cadastro'].input_formats=settings.DATE_INPUT_FORMATS
        self.fields['data_cadastro'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['preco'].min_value=0
        self.fields['preco'].error_messages={'required': 'Campo obrigatório.',
                                             'invalid': 'Valor inválido.',
                                             'max_digits': 'Mais de 5 dígitos no total.',
                                             'max_decimal_places': 'Mais de 2 dígitos decimais.',
                                             'max_whole_digits': 'Mais de 3 dígitos inteiros.'}
        self.fields['preco'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        self.fields['qtd_estoque'].min_value=0
        self.fields['qtd_estoque'].error_messages={
            'required': 'Campo obrigatório',
            'min_value': 'A quantidade deve ser maior ou igual a zero.'
        }
        self.fields['qtd_estoque'].widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        self.fields['imagem'].error_messages={'required': 'Campo obrigatório'}
        self.fields['imagem'].validators=[
            RegexValidator(regex='^[a-z]+\.(jpg|png|gif|bmp)$', message='Nome de imagem inválido.')]
        self.fields['imagem'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['imagem'].required = True

    
    
    """










    # override das definições padrões dos campos (adicionando código css aos inputs)

    nome = forms.CharField(
        error_messages = {'required' : 'Campo obrigatorio', 'unique' : 'Campo duplicado'},
        # caso o campo esteja vazio vai aparecer x, caso o nome ja existe vai aparecer y
        # isso se as propriedades unique e notnull foram definidas no modelo
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
    )

    # input nome passa a ser 
    # <input type="text" name="nome" id="id_nome" class="form-control form-control-sm" maxlength="100">

    descricao = forms.CharField(
        error_messages = {'required' : 'Campo obrigatorio'},
        # caso o campo esteja vazio vai aparecer x
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
    )

    # input descricao passa a ser 
    # <input type="text" name="descricao" id="id_descricao" class="form-control form-control-sm" maxlength="100">

    categoria = forms.ModelChoiceField(
        error_messages = {'required' : 'Campo obrigatorio'},
        # caso o campo esteja vazio vai aparecer x
        queryset = Categoria.objects.all().order_by('nome'),
        # define quais são os valores que vão aparecer na lista de categorias a ser selecionado
        # no caso por conta do metodo __str__(self): do modelo Categoria, serão retornados os
        # nomes de todas as categorias
        empty_label = "selecione uma categoria",
        # valor inicial da caixa de categorias
        widget=forms.Select(attrs={'class': 'form-control form-control-sm', 'maxlength': '100'}),
    )

    data_cadastro = forms.DateField(
        error_messages = {'required' : 'Campo obrigatorio', 'invalid': 'data invalida'},
        # caso o campo esteja vazio vai aparecer x, caso a data esteja errada aparece y
       
        input_formats = settings.DATE_INPUT_FORMATS,
        # formato da data a ser enviada, precisa ser definido em settings.py


        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm'})
    )

    # input data_cadastro passa a ser 
    # <input type="text" name="data_cadastro" id="id_data_cadastro" class="form-control form-control-sm" maxlength="100">

    preco = forms.DecimalField(
        localize = True,
        min_value = 0,
        # valor minimo de preco
        error_messages = {'required' : 'Campo obrigatorio', 'invalid': 'preco invalida',
        'min_value': 'O valor minimo é 0', 'max_digits' : ' atingiu numero maximo de digitos',
        'max_decimal_places': 'mais de 2 digitos decimais', 'max_whole_digits':'mais de 3 inteiros'},

        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'})

    )

    # input preco passa a ser 
    # <input type="text" name="preco" id="id_preco" onkeypress="return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44" class="form-control form-control-sm" maxlength="100">

    qtd_estoque = forms.IntegerField(
        min_value = 0,
        # valor minimo de preco
        error_messages = {'required' : 'Campo obrigatorio', 'invalid': 'preco invalida',
        'min_value': 'O valor minimo é 0', 'max_digits' : ' atingiu numero maximo de digitos',
        },

        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'})

    )

    # input qtd_estoque passa a ser 
    # <input type="text" name="qtd_estoque" id="id_qtd_estoque" onkeypress="return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44" class="form-control form-control-sm" maxlength="100">


    imagem = forms.CharField(
        error_messages = {'required' : 'Campo obrigatorio'},


        validators = [RegexValidator(regex='^[a-z]+\.(jpg|png|gif|bmp)$', message="url de imagem invalido")],

        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'max-lenght': '50'})

    )

     # <input type="text" name="qtd_estoque" id="id_qtd_estoque" class="form-control form-control-sm" maxlength="50">

    """ 
    descricao = forms.BooleanField(
        error_messages = {'required' : 'Campo obrigatorio'},
        widget=forms.CheckboxInput(),
        required = False

    descricao n muda nd entao n precisa colocar

    )"""