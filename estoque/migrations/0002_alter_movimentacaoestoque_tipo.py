# Generated manually for StockSync

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentacaoestoque',
            name='tipo',
            field=models.CharField(
                choices=[
                    ('entrada', 'Entrada'),
                    ('saida', 'Saída'),
                    ('compra', 'Compra'),
                    ('venda', 'Venda'),
                ],
                max_length=20,
            ),
        ),
    ]
