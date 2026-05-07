# 📦 StockSync ERP

Sistema ERP web desenvolvido com Django para gerenciamento completo de:

* Clientes
* Funcionários
* Estoque
* Entrada e saída de produtos
* Compras e vendas
* Pagamentos e recebimentos
* Dashboard gerencial

---

# 🚀 Tecnologias Utilizadas

## Backend

* Python 3
* Django
* SQLite3

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5
* Bootstrap Icons

## Bibliotecas

* validate-docbr → validação de CPF/CNPJ
* email-validator → validação de emails
* IMask.js → máscaras automáticas de formulário

---

# 🎨 Funcionalidades

## 📊 Dashboard Inteligente

Dashboard integrado ao banco de dados com:

* Total de clientes
* Total de funcionários
* Valor total em estoque
* Produtos com estoque baixo
* Contas vencidas
* Contas a pagar
* Contas a receber
* Compras e vendas do mês
* Últimas movimentações
* Produtos em destaque
* Gráficos financeiros

---

# 👥 Clientes e Funcionários

## Funcionalidades

* Cadastro
* Edição
* Exclusão
* Busca dinâmica
* Seleção interativa na tabela
* Máscaras automáticas
* Validação de CPF/CNPJ
* Validação de email

## Validações

* CPF válido
* CNPJ válido
* Email válido
* Máscaras automáticas para:

  * CPF
  * CNPJ
  * Telefone
  * Celular
  * CEP
  * UF

---

# 📦 Estoque

## Funcionalidades

* Cadastro de produtos
* Controle de estoque
* Estoque mínimo
* Valor de custo
* Valor de venda
* Categorias automáticas
* Busca por nome ou código

---

# 🔄 Movimentações de Estoque

## Operações disponíveis

### Entrada

* Adiciona unidades ao estoque

### Saída

* Remove unidades do estoque

### Compra

* Adiciona produtos ao estoque
* Gera lançamento financeiro

### Venda

* Remove produtos do estoque
* Gera recebimento financeiro

---

# 💰 Pagamentos e Recebimentos

## Funcionalidades

* Controle financeiro
* Status automáticos
* Atualização automática de vencidos
* Cadastro manual
* Integração com compras e vendas

## Status disponíveis

| Status    | Cor      |
| --------- | -------- |
| Pago      | Verde    |
| Pendente  | Laranja  |
| Receber   | Azul     |
| Vencido   | Vermelho |
| Cancelado | Cinza    |

---

# 🗄️ Banco de Dados

O sistema utiliza SQLite integrado ao Django ORM.

## Principais tabelas

* Clientes
* Funcionários
* Produtos
* Categorias
* Contas financeiras
* Movimentações de estoque

---

# 🔐 Login e Segurança

* Sistema autenticado com Django Authentication
* Área protegida por login
* Controle de superusuário
* Proteção CSRF nos formulários

---

# 📁 Estrutura do Projeto

```text
StockSync/
│
├── config/
├── core/
├── estoque/
├── static/
├── templates/
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

# ⚙️ Instalação Completa do Projeto

# ✅ 1. Instalar Python

Baixe o Python:

https://www.python.org/downloads/

Durante a instalação:

✅ marque:

```text
Add Python to PATH
```

---

# ✅ 2. Verificar instalação do Python

Abra o terminal e execute:

```bash
python --version
```

ou:

```bash
py --version
```

---

# ✅ 3. Clonar o projeto

```bash
git clone URL_DO_REPOSITORIO
```

---

# ✅ 4. Entrar na pasta do projeto

```bash
cd StockSync
```

---

# ✅ 5. Criar ambiente virtual

## Windows

```bash
python -m venv venv
```

## Linux / Mac

```bash
python3 -m venv venv
```

---

# ✅ 6. Ativar ambiente virtual

## Windows

```bash
venv\Scripts\activate
```

## Linux / Mac

```bash
source venv/bin/activate
```

---

# ✅ 7. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# ✅ 8. Criar banco de dados

```bash
python manage.py migrate
```

---

# ✅ 9. Criar superusuário

```bash
python manage.py createsuperuser
```

Preencha:

* usuário
* email
* senha

---

# ✅ 10. Executar servidor

```bash
python manage.py runserver
```

---

# 🌐 Acesso ao sistema

Abra no navegador:

```text
http://127.0.0.1:8000
```

---

# 🔐 Login administrativo

Painel administrativo:

```text
http://127.0.0.1:8000/admin
```

Utilize o superusuário criado anteriormente.

---

# 📦 Instalação Manual das Bibliotecas

Caso necessário:

## Django

```bash
pip install django
```

## validate-docbr

```bash
pip install validate-docbr
```

## email-validator

```bash
pip install email-validator
```

---

# 🧩 Bibliotecas Utilizadas

## validate-docbr

Utilizada para validação de:

* CPF
* CNPJ

---

## email-validator

Utilizada para:

* validação de emails
* verificação de domínio
* verificação MX

---

## IMask.js

Utilizada para máscaras automáticas:

* CPF
* CNPJ
* telefone
* celular
* CEP
* valores monetários

---

# 🔄 Comandos úteis

## Criar migrations

Quando alterar models.py:

```bash
python manage.py makemigrations
```

---

## Aplicar migrations

```bash
python manage.py migrate
```

---

## Criar novo superusuário

```bash
python manage.py createsuperuser
```

---

## Executar servidor

```bash
python manage.py runserver
```

---

# 🚀 Deploy Futuro

O projeto pode futuramente ser hospedado em:

* Render
* Railway
* PythonAnywhere
* VPS Linux
* Hostinger VPS

---

# 🎯 Melhorias Futuras

* API REST
* Relatórios PDF
* Controle de usuários
* Níveis de acesso
* Sistema de notificações
* Upload de imagens
* Integração com WhatsApp
* Integração com e-mail
* Controle de fornecedores
* Controle de caixa
* Gráficos avançados
* Deploy em nuvem

---

# 👨‍💻 Desenvolvedor

Projeto desenvolvido para fins acadêmicos e aprendizado de desenvolvimento

---

# 📄 Licença

Projeto de uso acadêmico e educacional.
