# Generated manually for StockSys

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias', 'ordering': ['nome']},
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('codigo', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('unidade', models.CharField(default='UN', max_length=20)),
                ('preco_custo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('preco_venda', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('quantidade_estoque', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estoque_minimo', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produtos', to='estoque.categoria')),
            ],
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos', 'ordering': ['nome']},
        ),
        migrations.CreateModel(
            name='MovimentacaoEstoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('entrada', 'Entrada'), ('saida', 'Saída'), ('ajuste', 'Ajuste')], max_length=20)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacao', models.TextField(blank=True, null=True)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movimentacoes', to='estoque.produto')),
            ],
            options={'verbose_name': 'Movimentação de estoque', 'verbose_name_plural': 'Movimentações de estoque', 'ordering': ['-data']},
        ),
    ]
