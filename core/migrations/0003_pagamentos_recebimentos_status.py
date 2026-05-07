# Generated manually for StockSync

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_dados_completos_cliente_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contapagar',
            name='status',
            field=models.CharField(
                choices=[
                    ('pendente', 'Pendente'),
                    ('pago', 'Pago'),
                    ('vencido', 'Vencido'),
                    ('cancelado', 'Cancelado'),
                    ('receber', 'Receber'),
                ],
                default='pendente',
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name='contapagar',
            name='fornecedor',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='contas_pagar',
                to='core.cliente',
                verbose_name='Pessoa / Empresa',
            ),
        ),
        migrations.AlterModelOptions(
            name='contapagar',
            options={
                'ordering': ['vencimento'],
                'verbose_name': 'Pagamento / Recebimento',
                'verbose_name_plural': 'Pagamentos / Recebimentos',
            },
        ),
    ]
