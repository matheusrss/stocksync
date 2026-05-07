from decimal import Decimal
from django.utils import timezone
from calendar import monthrange
from datetime import timedelta
import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, DecimalField, ExpressionWrapper, Q, Count
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .forms import ClienteForm, FuncionarioForm, ProdutoForm, ContaPagarForm
from .models import Cliente, Funcionario, ContaPagar
from estoque.models import Produto, MovimentacaoEstoque


def moeda(valor):
    valor = valor or Decimal('0.00')
    return f'R$ {valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def numero_br(valor):
    valor = valor or Decimal('0')
    return f'{valor:,.0f}'.replace(',', '.')


def form_errors_text(form):
    erros = []
    for campo, mensagens in form.errors.items():
        label = form.fields[campo].label if campo in form.fields else campo
        erros.append(f'{label}: {"; ".join(mensagens)}')
    return ' | '.join(erros) or 'Verifique os dados informados.'


def decimal_from_request(value):
    try:
        return Decimal(str(value or '0').replace(',', '.'))
    except Exception:
        return Decimal('0')


def buscar_produto(produto_id=None, produto_busca=''):
    produto = None
    produto_busca = (produto_busca or '').strip()

    if produto_id:
        produto = Produto.objects.filter(id=produto_id, ativo=True).first()

    if not produto and produto_busca:
        produto = Produto.objects.filter(
            Q(nome__iexact=produto_busca) | Q(codigo__iexact=produto_busca),
            ativo=True,
        ).first()

    if not produto and produto_busca:
        produto = Produto.objects.filter(
            Q(nome__icontains=produto_busca) | Q(codigo__icontains=produto_busca),
            ativo=True,
        ).first()

    return produto


def registrar_movimentacao(produto, tipo, quantidade, observacao=''):
    if quantidade <= 0:
        raise ValueError('A quantidade precisa ser maior que zero.')

    if tipo in ['saida', 'venda'] and produto.quantidade_estoque < quantidade:
        raise ValueError(f'Estoque insuficiente. Estoque atual de {produto.nome}: {produto.quantidade_estoque} {produto.unidade}.')

    return MovimentacaoEstoque.objects.create(
        produto=produto,
        tipo=tipo,
        quantidade=quantidade,
        observacao=observacao,
    )

def atualizar_vencidos():
    hoje = timezone.localdate()

    ContaPagar.objects.filter(
        vencimento__lt=hoje,
        status__in=['pendente', 'receber']
    ).update(status='vencido')


@login_required
def dashboard(request):
    atualizar_vencidos()
    hoje = timezone.localdate()
    inicio_mes = hoje.replace(day=1)
    fim_mes = hoje.replace(day=monthrange(hoje.year, hoje.month)[1])
    proximos_7_dias = hoje + timedelta(days=7)

    valor_total_expr = ExpressionWrapper(
        F('quantidade_estoque') * F('preco_custo'),
        output_field=DecimalField(max_digits=14, decimal_places=2),
    )

    produtos_ativos = Produto.objects.filter(ativo=True)
    contas_ativas = ContaPagar.objects.exclude(status='cancelado')

    pagar_hoje = contas_ativas.filter(vencimento=hoje, status='pendente').aggregate(total=Sum('valor'))['total'] or Decimal('0')
    pagar_mes = contas_ativas.filter(vencimento__gte=inicio_mes, vencimento__lte=fim_mes, status='pendente').aggregate(total=Sum('valor'))['total'] or Decimal('0')
    receber_hoje = contas_ativas.filter(vencimento=hoje, status='receber').aggregate(total=Sum('valor'))['total'] or Decimal('0')
    receber_mes = contas_ativas.filter(vencimento__gte=inicio_mes, vencimento__lte=fim_mes, status='receber').aggregate(total=Sum('valor'))['total'] or Decimal('0')

    vendas_mes = ContaPagar.objects.filter(
        descricao__icontains='Venda',
        criado_em__date__gte=inicio_mes,
        criado_em__date__lte=fim_mes,
    ).exclude(status='cancelado').aggregate(total=Sum('valor'))['total'] or Decimal('0')

    compras_mes = ContaPagar.objects.filter(
        descricao__icontains='Compra',
        criado_em__date__gte=inicio_mes,
        criado_em__date__lte=fim_mes,
    ).exclude(status='cancelado').aggregate(total=Sum('valor'))['total'] or Decimal('0')

    pagos_mes = ContaPagar.objects.filter(
        status='pago',
        criado_em__date__gte=inicio_mes,
        criado_em__date__lte=fim_mes,
    ).aggregate(total=Sum('valor'))['total'] or Decimal('0')

    lucro_estimado = vendas_mes - compras_mes
    estoque_valor = produtos_ativos.aggregate(total=Sum(valor_total_expr))['total'] or Decimal('0')
    estoque_qtd = produtos_ativos.aggregate(total=Sum('quantidade_estoque'))['total'] or Decimal('0')

    produtos_baixo = produtos_ativos.filter(quantidade_estoque__lte=F('estoque_minimo')).order_by('quantidade_estoque')
    contas_vencidas = contas_ativas.filter(
        status__in=['pendente', 'receber', 'vencido'],
        vencimento__lt=hoje,
    ).order_by('vencimento')
    proximos_vencimentos = contas_ativas.filter(
        status__in=['pendente', 'receber'],
        vencimento__gte=hoje,
        vencimento__lte=proximos_7_dias,
    ).order_by('vencimento')[:6]

    ultimas_movimentacoes = MovimentacaoEstoque.objects.select_related('produto').all()[:8]
    produtos_destaque = produtos_ativos.order_by('-quantidade_estoque')[:5]

    labels_7_dias = []
    vendas_7_dias = []
    compras_7_dias = []
    for i in range(6, -1, -1):
        dia = hoje - timedelta(days=i)
        labels_7_dias.append(dia.strftime('%d/%m'))
        vendas_dia = ContaPagar.objects.filter(
            descricao__icontains='Venda',
            criado_em__date=dia,
        ).exclude(status='cancelado').aggregate(total=Sum('valor'))['total'] or Decimal('0')
        compras_dia = ContaPagar.objects.filter(
            descricao__icontains='Compra',
            criado_em__date=dia,
        ).exclude(status='cancelado').aggregate(total=Sum('valor'))['total'] or Decimal('0')
        vendas_7_dias.append(float(vendas_dia))
        compras_7_dias.append(float(compras_dia))

    status_labels = ['Receber', 'Pendente', 'Pago', 'Vencido', 'Cancelado']
    status_keys = ['receber', 'pendente', 'pago', 'vencido', 'cancelado']
    status_values = []
    for status in status_keys:
        total = ContaPagar.objects.filter(status=status).aggregate(total=Sum('valor'))['total'] or Decimal('0')
        status_values.append(float(total))

    contexto = {
        'receber_hoje': moeda(receber_hoje),
        'receber_mes': moeda(receber_mes),
        'pagar_hoje': moeda(pagar_hoje),
        'pagar_mes': moeda(pagar_mes),
        'vendas_mes': moeda(vendas_mes),
        'compras_mes': moeda(compras_mes),
        'pagos_mes': moeda(pagos_mes),
        'lucro_estimado': moeda(lucro_estimado),
        'estoque_peso': f'{numero_br(estoque_qtd)} un.',
        'estoque_valor': moeda(estoque_valor),
        'total_produtos': produtos_ativos.count(),
        'total_clientes': Cliente.objects.filter(ativo=True, funcao__in=['cliente', 'ambos']).count(),
        'total_funcionarios': Funcionario.objects.filter(ativo=True).count(),
        'total_estoque_baixo': produtos_baixo.count(),
        'total_contas_vencidas': contas_vencidas.count(),
        'total_movimentacoes_mes': MovimentacaoEstoque.objects.filter(data__date__gte=inicio_mes, data__date__lte=fim_mes).count(),
        'produtos_baixo': produtos_baixo[:6],
        'contas_vencidas': contas_vencidas[:6],
        'proximos_vencimentos': proximos_vencimentos,
        'ultimas_movimentacoes': ultimas_movimentacoes,
        'produtos_destaque': produtos_destaque,
        'chart_labels': json.dumps(labels_7_dias),
        'chart_vendas': json.dumps(vendas_7_dias),
        'chart_compras': json.dumps(compras_7_dias),
        'chart_status_labels': json.dumps(status_labels),
        'chart_status_values': json.dumps(status_values),
    }
    return render(request, 'core/dashboard.html', contexto)


@login_required
def cadastros(request):
    tipo = request.GET.get('tipo', 'clientes')
    busca = request.GET.get('busca', '').strip()

    if tipo == 'funcionarios':
        registros = Funcionario.objects.filter(ativo=True)
        if busca:
            registros = registros.filter(Q(nome__icontains=busca) | Q(cpf__icontains=busca) | Q(celular__icontains=busca) | Q(telefone__icontains=busca))
        form = FuncionarioForm()
        titulo = 'Cadastros - Funcionários'
    else:
        tipo = 'clientes'
        registros = Cliente.objects.filter(ativo=True)
        if busca:
            registros = registros.filter(Q(nome__icontains=busca) | Q(cpf_cnpj__icontains=busca) | Q(celular__icontains=busca) | Q(telefone__icontains=busca))
        form = ClienteForm()
        titulo = 'Clientes - Tabela de Cadastrados'

    return render(request, 'core/cadastros.html', {
        'tipo': tipo,
        'titulo_pagina': titulo,
        'registros': registros,
        'busca': busca,
        'form': form,
    })


@login_required
def novo_cadastro(request):
    tipo = request.POST.get('tipo', 'clientes')

    if request.method != 'POST':
        return redirect('/cadastros/')

    if tipo == 'funcionarios':
        form = FuncionarioForm(request.POST)
        registros = Funcionario.objects.filter(ativo=True)
        titulo = 'Cadastros - Funcionários'

        if form.is_valid():
            form.save()
            messages.success(request, 'Funcionário cadastrado com sucesso.')
            return redirect('/cadastros/?tipo=funcionarios')

        return render(request, 'core/cadastros.html', {
            'tipo': 'funcionarios',
            'titulo_pagina': titulo,
            'registros': registros,
            'busca': '',
            'form': form,
            'abrir_modal_novo': True,
        })

    form = ClienteForm(request.POST)
    registros = Cliente.objects.filter(ativo=True)
    titulo = 'Clientes - Tabela de Cadastrados'

    if form.is_valid():
        form.save()
        messages.success(request, 'Cliente cadastrado com sucesso.')
        return redirect('/cadastros/?tipo=clientes')

    return render(request, 'core/cadastros.html', {
        'tipo': 'clientes',
        'titulo_pagina': titulo,
        'registros': registros,
        'busca': '',
        'form': form,
        'abrir_modal_novo': True,
    })


@login_required
def estoque(request):
    produtos = Produto.objects.select_related('categoria').filter(ativo=True)
    busca = request.GET.get('busca', '').strip()
    if busca:
        produtos = produtos.filter(Q(nome__icontains=busca) | Q(codigo__icontains=busca) | Q(categoria__nome__icontains=busca))

    return render(request, 'core/estoque.html', {
        'produtos': produtos,
        'busca': busca,
        'form': ProdutoForm(),
    })


@login_required
def novo_produto(request):
    if request.method != 'POST':
        return redirect('estoque')

    form = ProdutoForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produto salvo com sucesso!')
    else:
        messages.error(request, form_errors_text(form))
    return redirect('estoque')


@login_required
def contas_pagar(request):
    atualizar_vencidos()
    contas = ContaPagar.objects.select_related('fornecedor').all()
    busca = request.GET.get('busca', '').strip()
    if busca:
        contas = contas.filter(Q(descricao__icontains=busca) | Q(fornecedor__nome__icontains=busca) | Q(status__icontains=busca))

    return render(request, 'core/contas_pagar.html', {
        'contas': contas,
        'busca': busca,
        'form': ContaPagarForm(),
    })


@login_required
def nova_conta_pagar(request):
    if request.method != 'POST':
        return redirect('contas_pagar')

    form = ContaPagarForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Pagamento/recebimento salvo com sucesso!')
    else:
        messages.error(request, form_errors_text(form))
    return redirect('contas_pagar')


@login_required
def movimentacoes_estoque(request):
    busca = request.GET.get('busca', '').strip()
    produtos = Produto.objects.select_related('categoria').filter(ativo=True).order_by('nome')
    pessoas = Cliente.objects.filter(ativo=True).order_by('nome')
    movimentacoes = MovimentacaoEstoque.objects.select_related('produto', 'produto__categoria').all()[:100]

    if busca:
        movimentacoes = MovimentacaoEstoque.objects.select_related('produto', 'produto__categoria').filter(
            Q(produto__nome__icontains=busca) |
            Q(produto__codigo__icontains=busca) |
            Q(tipo__icontains=busca) |
            Q(observacao__icontains=busca)
        )[:100]

    if request.method == 'POST':
        operacao = request.POST.get('operacao')
        produto = buscar_produto(
            produto_id=request.POST.get('produto'),
            produto_busca=request.POST.get('produto_busca', ''),
        )

        if not produto:
            messages.error(request, 'Produto não cadastrado. Cadastre o produto antes de movimentar, comprar ou vender.')
            return redirect('movimentacoes_estoque')

        quantidade = decimal_from_request(request.POST.get('quantidade'))
        observacao = request.POST.get('observacao', '').strip()

        try:
            if operacao == 'entrada':
                registrar_movimentacao(produto, 'entrada', quantidade, observacao or 'Entrada manual de estoque')
                messages.success(request, 'Entrada registrada com sucesso. As unidades foram adicionadas ao estoque.')

            elif operacao == 'saida':
                registrar_movimentacao(produto, 'saida', quantidade, observacao or 'Saída manual de estoque')
                messages.success(request, 'Saída registrada com sucesso. As unidades foram retiradas do estoque.')

            elif operacao == 'compra':
                valor = decimal_from_request(request.POST.get('valor'))
                vencimento = request.POST.get('vencimento') or timezone.localdate()
                status = request.POST.get('status') or 'pendente'
                data_pagamento = request.POST.get('data_pagamento') or None
                fornecedor_id = request.POST.get('pessoa')
                fornecedor = Cliente.objects.filter(id=fornecedor_id, ativo=True).first() if fornecedor_id else None

                if valor <= 0:
                    messages.error(request, 'Informe um valor válido para a compra.')
                    return redirect('movimentacoes_estoque')

                if status not in ['pendente', 'pago']:
                    status = 'pendente'

                registrar_movimentacao(produto, 'compra', quantidade, observacao or 'Compra de produto')
                ContaPagar.objects.create(
                    descricao=f'Compra - {produto.nome}',
                    fornecedor=fornecedor,
                    valor=valor,
                    vencimento=vencimento,
                    status=status,
                    data_pagamento=data_pagamento if status == 'pago' else None,
                    observacao=observacao,
                )
                messages.success(request, 'Compra registrada. O estoque foi atualizado e o pagamento foi lançado em Pagamentos e Recebimentos.')

            elif operacao == 'venda':
                valor = decimal_from_request(request.POST.get('valor'))
                vencimento = request.POST.get('vencimento') or timezone.localdate()
                status = request.POST.get('status') or 'receber'
                cliente_id = request.POST.get('pessoa')
                cliente = Cliente.objects.filter(id=cliente_id, ativo=True).first() if cliente_id else None

                if valor <= 0:
                    messages.error(request, 'Informe um valor válido para a venda.')
                    return redirect('movimentacoes_estoque')

                if status not in ['receber', 'pago']:
                    status = 'receber'

                registrar_movimentacao(produto, 'venda', quantidade, observacao or 'Venda de produto')
                ContaPagar.objects.create(
                    descricao=f'Venda - {produto.nome}',
                    fornecedor=cliente,
                    valor=valor,
                    vencimento=vencimento,
                    status=status,
                    data_pagamento=timezone.localdate() if status == 'pago' else None,
                    observacao=observacao,
                )

                if status == 'pago':
                    messages.success(request, 'Venda registrada como paga. O estoque foi atualizado e o pagamento entrou em Pagamentos e Recebimentos.')
                else:
                    messages.success(request, 'Venda registrada como receber. O estoque foi atualizado e o recebimento foi lançado em Pagamentos e Recebimentos.')

            else:
                messages.error(request, 'Operação inválida.')

        except ValueError as erro:
            messages.error(request, str(erro))

        return redirect('movimentacoes_estoque')

    return render(request, 'core/movimentacoes_estoque.html', {
        'produtos': produtos,
        'pessoas': pessoas,
        'movimentacoes': movimentacoes,
        'busca': busca,
    })

@login_required
def editar_cadastro(request, tipo, id):
    if tipo == 'funcionarios':
        registro = get_object_or_404(Funcionario, id=id)
        form = FuncionarioForm(request.POST or None, instance=registro)

        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('/cadastros/?tipo=funcionarios')

        return redirect('/cadastros/?tipo=funcionarios')

    registro = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=registro)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/cadastros/?tipo=clientes')

    return redirect('/cadastros/?tipo=clientes')


@login_required
def excluir_cadastro(request, tipo, id):
    if request.method == 'POST':
        if tipo == 'funcionarios':
            registro = get_object_or_404(Funcionario, id=id)
            registro.delete()
            return redirect('/cadastros/?tipo=funcionarios')

        registro = get_object_or_404(Cliente, id=id)
        registro.delete()
        return redirect('/cadastros/?tipo=clientes')

    return redirect('/cadastros/')


@login_required
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('estoque')

    return redirect('estoque')


@login_required
def excluir_produto(request, id):
    if request.method == 'POST':
        produto = get_object_or_404(Produto, id=id)
        produto.delete()

    return redirect('estoque')


@login_required
def editar_conta_pagar(request, id):
    conta = get_object_or_404(ContaPagar, id=id)
    form = ContaPagarForm(request.POST or None, instance=conta)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('contas_pagar')

    return redirect('contas_pagar')


@login_required
def excluir_conta_pagar(request, id):
    if request.method == 'POST':
        conta = get_object_or_404(ContaPagar, id=id)
        conta.delete()

    return redirect('contas_pagar')
