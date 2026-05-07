from django.contrib import admin
from .models import Cliente, Funcionario, ContaPagar


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf_cnpj', 'funcao', 'telefone', 'ativo')
    list_filter = ('funcao', 'ativo')
    search_fields = ('nome', 'cpf_cnpj', 'telefone', 'email')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'cargo', 'telefone', 'ativo')
    list_filter = ('cargo', 'ativo')
    search_fields = ('nome', 'cpf', 'telefone', 'email')


@admin.register(ContaPagar)
class ContaPagarAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'fornecedor', 'valor', 'vencimento', 'status')
    list_filter = ('status', 'vencimento')
    search_fields = ('descricao', 'fornecedor__nome')
