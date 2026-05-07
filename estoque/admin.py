from django.contrib import admin
from .models import Categoria, Produto, MovimentacaoEstoque


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ativo')
    search_fields = ('nome',)
    list_filter = ('ativo',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'quantidade_estoque', 'unidade', 'preco_custo', 'preco_venda', 'ativo')
    list_filter = ('categoria', 'ativo')
    search_fields = ('nome', 'codigo')


@admin.register(MovimentacaoEstoque)
class MovimentacaoEstoqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'produto', 'tipo', 'quantidade', 'data')
    list_filter = ('tipo', 'data')
    search_fields = ('produto__nome', 'observacao')
