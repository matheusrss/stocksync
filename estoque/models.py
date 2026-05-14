from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Produto(models.Model):
    UNIDADE_CHOICES = (
        ('UN', 'UN - Unidade'),
        ('KG', 'KG - Quilograma'),
    )

    nome = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='produtos')
    codigo = models.CharField(max_length=50, unique=True, blank=True, null=True)

    unidade = models.CharField(
        max_length=2,
        choices=UNIDADE_CHOICES,
        default='UN'
    )

    preco_custo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantidade_estoque = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estoque_minimo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

    def __str__(self):
        return self.nome

    @property
    def valor_total_estoque(self):
        return self.quantidade_estoque * self.preco_custo


class MovimentacaoEstoque(models.Model):
    TIPO_CHOICES = (
        ('entrada', 'Entrada'),
        ('saida', 'Saída'),
        ('compra', 'Compra'),
        ('venda', 'Venda'),
    )

    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='movimentacoes')
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Movimentação de estoque'
        verbose_name_plural = 'Movimentações de estoque'
        ordering = ['-data']

    def save(self, *args, **kwargs):
        # Só altera o estoque ao criar uma nova movimentação.
        # Assim, editar um registro antigo não soma/subtrai duas vezes.
        if not self.pk:
            if self.tipo in ['entrada', 'compra']:
                self.produto.quantidade_estoque += self.quantidade
            elif self.tipo in ['saida', 'venda']:
                self.produto.quantidade_estoque -= self.quantidade

            self.produto.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.produto.nome} - {self.get_tipo_display()} - {self.quantidade}'
