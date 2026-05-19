from django import forms
from django.core.exceptions import ValidationError
from validate_docbr import CPF, CNPJ
from email_validator import validate_email, EmailNotValidError

from .models import Cliente, Funcionario, ContaPagar
from estoque.models import Categoria, Produto


COMMON_INPUT = {'class': 'form-control-custom'}
COMMON_SELECT = {'class': 'form-control-custom'}


class BaseStyledModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            css_atual = field.widget.attrs.get('class', '')
            classes = css_atual.split()

            if 'form-control-custom' not in classes:
                classes.append('form-control-custom')

            field.widget.attrs['class'] = ' '.join(classes)
            field.widget.attrs.setdefault('autocomplete', 'off')


class ClienteForm(BaseStyledModelForm):

    email = forms.EmailField(
        error_messages={
            'invalid': 'O e-mail informado não é válido.',
            'required': 'O e-mail é obrigatório.'
        }
    )

    

    class Meta:
        model = Cliente

        fields = [
            'nome',
            'cpf_cnpj',
            'funcao',
            'nome_fantasia',
            'email',
            'telefone_fixo',
            'celular',
            'cep',
            'rua',
            'numero',
            'bairro',
            'complemento',
            'pais',
            'uf',
            'cidade',
        ]

        widgets = {

            'cpf_cnpj': forms.TextInput(attrs={
                'class': 'form-control-custom mask-cpf-cnpj',
                'placeholder': 'CPF ou CNPJ'
            }),

            'funcao': forms.Select(attrs=COMMON_SELECT),

            'email': forms.EmailInput(attrs={
                'class': 'form-control-custom',
                'placeholder': 'email@exemplo.com'
            }),

            'telefone_fixo': forms.TextInput(attrs={
                'class': 'form-control-custom mask-telefone',
                'placeholder': '(00) 0000-0000'
            }),

            'celular': forms.TextInput(attrs={
                'class': 'form-control-custom mask-celular',
                'placeholder': '(00) 00000-0000'
            }),

            'cep': forms.TextInput(attrs={
                'class': 'form-control-custom mask-cep',
                'placeholder': '00000-000'
            }),

            'uf': forms.TextInput(attrs={
                'class': 'form-control-custom mask-uf',
                'placeholder': 'SP',
                'maxlength': '2'
            }),
        }

    def clean_cpf_cnpj(self):
        valor = self.cleaned_data.get('cpf_cnpj')

        if not valor:
            return valor

        numeros = ''.join(filter(str.isdigit, valor))

        cpf = CPF()
        cnpj = CNPJ()

        if len(numeros) == 11:

            if not cpf.validate(numeros):
                raise ValidationError(
                    'O CPF informado é inválido.'
                )

        elif len(numeros) == 14:

            if not cnpj.validate(numeros):
                raise ValidationError(
                    'O CNPJ informado é inválido.'
                )

        else:
            raise ValidationError(
                'Digite um CPF ou CNPJ válido.'
            )

        return valor
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            return email

        try:
            validacao = validate_email(
                email,
                check_deliverability=True
            )

            return validacao.email

        except EmailNotValidError:
            raise ValidationError(
                'O e-mail informado não é válido.'
            )


class FuncionarioForm(BaseStyledModelForm):

    email = forms.EmailField(
        error_messages={
            'invalid': 'O e-mail informado não é válido.',
            'required': 'O e-mail é obrigatório.'
        }
    )

    class Meta:
        model = Funcionario

        fields = [
            'nome',
            'cpf',
            'cargo',
            'email',
            'telefone_fixo',
            'celular',
            'cep',
            'rua',
            'numero',
            'bairro',
            'complemento',
            'pais',
            'uf',
            'cidade',
        ]

        widgets = {

            'cpf': forms.TextInput(attrs={
                'class': 'form-control-custom mask-cpf',
                'placeholder': '000.000.000-00'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control-custom',
                'placeholder': 'email@exemplo.com'
            }),

            'telefone_fixo': forms.TextInput(attrs={
                'class': 'form-control-custom mask-telefone',
                'placeholder': '(00) 0000-0000'
            }),

            'celular': forms.TextInput(attrs={
                'class': 'form-control-custom mask-celular',
                'placeholder': '(00) 00000-0000'
            }),

            'cep': forms.TextInput(attrs={
                'class': 'form-control-custom mask-cep',
                'placeholder': '00000-000'
            }),

            'uf': forms.TextInput(attrs={
                'class': 'form-control-custom mask-uf',
                'placeholder': 'SP',
                'maxlength': '2'
            }),
        }

    def clean_cpf(self):
        valor = self.cleaned_data.get('cpf')

        if not valor:
            return valor

        numeros = ''.join(filter(str.isdigit, valor))

        cpf = CPF()

        if not cpf.validate(numeros):
            raise ValidationError(
                'O CPF informado é inválido.'
            )

        return valor
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            return email

        try:
            validacao = validate_email(
                email,
                check_deliverability=True
            )

            return validacao.email

        except EmailNotValidError:
            raise ValidationError(
                'O e-mail informado não é válido.'
            )

class ProdutoForm(BaseStyledModelForm):
    categoria_nome = forms.CharField(
        label='Categoria',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control-custom',
            'placeholder': 'Ex.: Sucata'
        })
    )
    
    # Definir os preços como CharField (aceita qualquer texto)
    preco_custo = forms.CharField(
        label='Preço de Custo',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control-custom mask-money',
            'placeholder': 'R$ 0,00'
        })
    )
    
    preco_venda = forms.CharField(
        label='Preço de Venda',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control-custom mask-money',
            'placeholder': 'R$ 0,00'
        })
    )

    class Meta:
        model = Produto
        fields = [
            'nome',
            'codigo',
            'categoria_nome',
            'unidade',
            'quantidade_estoque',
            'estoque_minimo',
            'preco_custo',
            'preco_venda',
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control-custom'}),
            'unidade': forms.Select(attrs={'class': 'form-control-custom'}),
            'quantidade_estoque': forms.NumberInput(attrs={
                'class': 'form-control-custom',
                'step': '0.01',
                'min': '0'
            }),
            'estoque_minimo': forms.NumberInput(attrs={
                'class': 'form-control-custom',
                'step': '0.01',
                'min': '0'
            }),
        }

    def clean_preco_custo(self):
        valor = self.cleaned_data.get('preco_custo', '')
        if not valor or valor.strip() == '':
            return None
        
        try:
            # Limpar: remover "R$", espaços, e converter formato brasileiro
            valor_limpo = valor.replace('R$', '').strip()
            valor_limpo = valor_limpo.replace('.', '').replace(',', '.')
            from decimal import Decimal
            return Decimal(valor_limpo)
        except Exception as e:
            raise forms.ValidationError('Preço de custo inválido. Use o formato: 5,55')

    def clean_preco_venda(self):
        valor = self.cleaned_data.get('preco_venda', '')
        if not valor or valor.strip() == '':
            return None
        
        try:
            # Limpar: remover "R$", espaços, e converter formato brasileiro
            valor_limpo = valor.replace('R$', '').strip()
            valor_limpo = valor_limpo.replace('.', '').replace(',', '.')
            from decimal import Decimal
            return Decimal(valor_limpo)
        except Exception as e:
            raise forms.ValidationError('Preço de venda inválido. Use o formato: 5,55')

    def save(self, commit=True):
        produto = super().save(commit=False)
        
        # Garantir que os preços estão como Decimal
        if self.cleaned_data.get('preco_custo'):
            produto.preco_custo = self.cleaned_data['preco_custo']
        if self.cleaned_data.get('preco_venda'):
            produto.preco_venda = self.cleaned_data['preco_venda']
        
        # Salvar categoria
        categoria_nome = self.cleaned_data.get('categoria_nome')
        if categoria_nome:
            categoria, _ = Categoria.objects.get_or_create(
                nome=categoria_nome.strip()
            )
            produto.categoria = categoria
        elif not produto.categoria_id:
            categoria, _ = Categoria.objects.get_or_create(
                nome='Geral'
            )
            produto.categoria = categoria
        
        if commit:
            produto.save()
        return produto


class ContaPagarForm(BaseStyledModelForm):

    class Meta:
        model = ContaPagar

        fields = [
            'descricao',
            'fornecedor',
            'valor',
            'vencimento',
            'status',
            'data_pagamento',
            'observacao'
        ]

        widgets = {
            'valor': forms.TextInput(attrs={
            'class': 'form-control-custom mask-money',
            'placeholder': 'R$ 0,00',
            'value': ''
        }),

            'vencimento': forms.DateInput(attrs={
                'class': 'form-control-custom',
                'type': 'date'
            }),

            'data_pagamento': forms.DateInput(attrs={
                'class': 'form-control-custom',
                'type': 'date'
            }),

            'observacao': forms.Textarea(attrs={
                'class': 'form-control-custom textarea-custom',
                'rows': 3
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['fornecedor'].queryset = Cliente.objects.filter(
            ativo=True
        )

        self.fields['fornecedor'].required = False
        self.fields['fornecedor'].label = 'Pessoa / Empresa'

        self.fields['data_pagamento'].required = False
        self.fields['observacao'].required = False