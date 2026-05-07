from django.urls import path
from .views import (
    dashboard,
    cadastros,
    novo_cadastro,
    editar_cadastro,
    excluir_cadastro,
    estoque,
    novo_produto,
    editar_produto,
    excluir_produto,
    contas_pagar,
    nova_conta_pagar,
    editar_conta_pagar,
    excluir_conta_pagar,
    movimentacoes_estoque,
)

urlpatterns = [
    path('', dashboard, name='dashboard'),

    path('cadastros/', cadastros, name='cadastros'),
    path('cadastros/novo/', novo_cadastro, name='novo_cadastro'),
    path('cadastros/editar/<str:tipo>/<int:id>/', editar_cadastro, name='editar_cadastro'),
    path('cadastros/excluir/<str:tipo>/<int:id>/', excluir_cadastro, name='excluir_cadastro'),

    path('estoque/', estoque, name='estoque'),
    path('estoque/novo/', novo_produto, name='novo_produto'),
    path('estoque/editar/<int:id>/', editar_produto, name='editar_produto'),
    path('movimentacoes-estoque/', movimentacoes_estoque, name='movimentacoes_estoque'),
    path('estoque/excluir/<int:id>/', excluir_produto, name='excluir_produto'),

    path('contas-pagar/', contas_pagar, name='contas_pagar'),
    path('contas-pagar/nova/', nova_conta_pagar, name='nova_conta_pagar'),
    path('contas-pagar/editar/<int:id>/', editar_conta_pagar, name='editar_conta_pagar'),
    path('contas-pagar/excluir/<int:id>/', excluir_conta_pagar, name='excluir_conta_pagar'),
]
