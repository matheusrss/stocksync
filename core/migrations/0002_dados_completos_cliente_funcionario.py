# Generated for StockSys form fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField('cliente', 'nome_fantasia', models.CharField(blank=True, max_length=150, null=True)),
        migrations.AddField('cliente', 'telefone_fixo', models.CharField(blank=True, max_length=20, null=True)),
        migrations.AddField('cliente', 'celular', models.CharField(blank=True, max_length=20, null=True)),
        migrations.AddField('cliente', 'cep', models.CharField(blank=True, max_length=20, null=True)),
        migrations.AddField('cliente', 'rua', models.CharField(blank=True, max_length=150, null=True, verbose_name='Rua / Logradouro')),
        migrations.AddField('cliente', 'numero', models.CharField(blank=True, max_length=20, null=True)),
        migrations.AddField('cliente', 'bairro', models.CharField(blank=True, max_length=100, null=True)),
        migrations.AddField('cliente', 'complemento', models.CharField(blank=True, max_length=150, null=True)),
        migrations.AddField('cliente', 'pais', models.CharField(blank=True, max_length=50, null=True, verbose_name='País')),
        migrations.AddField('cliente', 'uf', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
        migrations.AddField('cliente', 'cidade', models.CharField(blank=True, max_length=100, null=True)),
        migrations.AddField('funcionario', 'telefone_fixo', models.CharField(blank=True, max_length=20, null=True)),
        migrations.AddField('funcionario', 'celular', models.CharField(blank=True, max_length=20, null=True)),
        migrations.AddField('funcionario', 'cep', models.CharField(blank=True, max_length=20, null=True)),
        migrations.AddField('funcionario', 'rua', models.CharField(blank=True, max_length=150, null=True, verbose_name='Rua / Logradouro')),
        migrations.AddField('funcionario', 'numero', models.CharField(blank=True, max_length=20, null=True)),
        migrations.AddField('funcionario', 'bairro', models.CharField(blank=True, max_length=100, null=True)),
        migrations.AddField('funcionario', 'complemento', models.CharField(blank=True, max_length=150, null=True)),
        migrations.AddField('funcionario', 'pais', models.CharField(blank=True, max_length=50, null=True, verbose_name='País')),
        migrations.AddField('funcionario', 'uf', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
        migrations.AddField('funcionario', 'cidade', models.CharField(blank=True, max_length=100, null=True)),
    ]
