from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    TIPO_CHOICES = (
        ('cliente', 'Cliente'),
        ('fornecedor', 'Fornecedor'),
        ('ambos', 'Ambos'),
    )

    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length=20, unique=True)
    funcao = models.CharField(max_length=20, choices=TIPO_CHOICES, default='cliente')

    nome_fantasia = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone_fixo = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)

    cep = models.CharField(max_length=20, blank=True, null=True)
    rua = models.CharField('Rua / Logradouro', max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=150, blank=True, null=True)
    pais = models.CharField('País', max_length=50, blank=True, null=True)
    uf = models.CharField('UF', max_length=2, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)

    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente / Fornecedor'
        verbose_name_plural = 'Clientes / Fornecedores'
        ordering = ['nome']

    def save(self, *args, **kwargs):
        self.endereco = self.endereco_completo
        self.telefone = self.celular or self.telefone_fixo
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    @property
    def endereco_completo(self):
        partes = [self.rua, self.numero, self.bairro, self.cidade, self.uf]
        return ', '.join([str(p) for p in partes if p])

    @property
    def badge_class(self):
        if self.funcao == 'cliente':
            return 'badge-cliente'
        if self.funcao == 'fornecedor':
            return 'badge-fornecedor'
        return 'badge-ambos'


class Funcionario(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField('CPF', max_length=14, unique=True)
    cargo = models.CharField(max_length=100)

    email = models.EmailField(blank=True, null=True)
    telefone_fixo = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)

    cep = models.CharField(max_length=20, blank=True, null=True)
    rua = models.CharField('Rua / Logradouro', max_length=150, blank=True, null=True)
    numero = models.CharField(max_length=20, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    complemento = models.CharField(max_length=150, blank=True, null=True)
    pais = models.CharField('País', max_length=50, blank=True, null=True)
    uf = models.CharField('UF', max_length=2, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)

    endereco = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_admissao = models.DateField(default=timezone.now)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']

    def save(self, *args, **kwargs):
        self.endereco = self.endereco_completo
        self.telefone = self.celular or self.telefone_fixo
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome

    @property
    def endereco_completo(self):
        partes = [self.rua, self.numero, self.bairro, self.cidade, self.uf]
        return ', '.join([str(p) for p in partes if p])


class ContaPagar(models.Model):
    STATUS_CHOICES = (
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('vencido', 'Vencido'),
        ('cancelado', 'Cancelado'),
        ('receber', 'Receber'),
    )
    movimentacao = models.ForeignKey(
    'estoque.MovimentacaoEstoque',
    on_delete=models.SET_NULL,
    null=True,
    blank=True
)

    descricao = models.CharField(max_length=150)
    fornecedor = models.ForeignKey(
        Cliente,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='contas_pagar',
        verbose_name='Pessoa / Empresa',
    )
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    vencimento = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    data_pagamento = models.DateField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Pagamento / Recebimento'
        verbose_name_plural = 'Pagamentos / Recebimentos'
        ordering = ['vencimento']

    def __str__(self):
        return f'{self.descricao} - R$ {self.valor}'

    @property
    def status_badge_class(self):
        classes = {
            'vencido': 'status-vencido',
            'pendente': 'status-pendente',
            'pago': 'status-pago',
            'cancelado': 'status-cancelado',
            'receber': 'status-receber',
        }
        return classes.get(self.status, 'status-pendente')
