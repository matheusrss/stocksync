# Generated manually for StockSys

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf_cnpj', models.CharField(max_length=20, unique=True, verbose_name='CPF/CNPJ')),
                ('funcao', models.CharField(choices=[('cliente', 'Cliente'), ('fornecedor', 'Fornecedor'), ('ambos', 'Ambos')], default='cliente', max_length=20)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
            options={'verbose_name': 'Cliente / Fornecedor', 'verbose_name_plural': 'Clientes / Fornecedores', 'ordering': ['nome']},
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('cargo', models.CharField(max_length=100)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('salario', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('data_admissao', models.DateField(default=django.utils.timezone.now)),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
            options={'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários', 'ordering': ['nome']},
        ),
        migrations.CreateModel(
            name='ContaPagar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vencimento', models.DateField()),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('pago', 'Pago'), ('vencido', 'Vencido'), ('cancelado', 'Cancelado')], default='pendente', max_length=20)),
                ('data_pagamento', models.DateField(blank=True, null=True)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('fornecedor', models.ForeignKey(blank=True, limit_choices_to={'funcao__in': ['fornecedor', 'ambos']}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contas_pagar', to='core.cliente')),
            ],
            options={'verbose_name': 'Conta a pagar', 'verbose_name_plural': 'Contas a pagar', 'ordering': ['vencimento']},
        ),
    ]
