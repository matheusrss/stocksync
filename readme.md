# 📦 StockSync ERP

A modern ERP web application built with Django for inventory, financial, employee and business management.

---

# 🚀 Features

* Client management
* Employee management
* Inventory control
* Product stock operations
* Purchases and sales
* Financial management
* Smart dashboard
* CPF/CNPJ validation
* Email validation
* Interactive tables
* Responsive modern UI

---

# 🛠️ Technologies

## Backend

* Python 3
* Django
* SQLite3

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5

## Libraries

* validate-docbr
* email-validator
* IMask.js

---

# 📁 Project Structure

```text id="m85y7q"
StockSync/
│
├── config/
├── core/
├── estoque/
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation Guide

# ✅ 1. Clone Repository

```bash id="3xk8uq"
git clone https://github.com/matheusrss/StockSync.git
```

---

# ✅ 2. Open Project Folder

```bash id="fgjwhx"
cd StockSync
```

---

# ✅ 3. Create Virtual Environment

## Windows

```bash id="gjlwmw"
python -m venv venv
```

## Linux / Mac

```bash id="mij1rk"
python3 -m venv venv
```

---

# ✅ 4. Activate Virtual Environment

## Windows

```bash id="o1v2i7"
venv\Scripts\activate
```

## Linux / Mac

```bash id="jq40d6"
source venv/bin/activate
```

---

# ✅ 5. Install Dependencies

```bash id="3y7p2x"
pip install -r requirements.txt
```

---

# ⚠️ IMPORTANT

This repository does NOT include the SQLite database file.

Because of that, you MUST create the database locally before running the project.

---

# ✅ 6. Create Database

Run migrations:

```bash id="qrj1y7"
python manage.py migrate
```

This command creates all database tables automatically.

---

# ✅ 7. Create Superuser

Create an admin account:

```bash id="4hv2b0"
python manage.py createsuperuser
```

Fill:

* username
* email
* password

---

# ✅ 8. Run Development Server

```bash id="jlwm1h"
python manage.py runserver
```

---

# 🌐 Access System

Open in browser:

```text id="r0m0h7"
http://127.0.0.1:8000
```

---

# 🔐 Admin Panel

```text id="p1nrfc"
http://127.0.0.1:8000/admin
```

Use the superuser credentials created previously.

---

# 📦 Manual Library Installation

## Django

```bash id="st9x6z"
pip install django
```

## validate-docbr

```bash id="iw5s1t"
pip install validate-docbr
```

## email-validator

```bash id="5k1r2w"
pip install email-validator
```

---

# 🔄 Useful Commands

## Create migrations

```bash id="1ck9l3"
python manage.py makemigrations
```

---

## Apply migrations

```bash id="8c4qwe"
python manage.py migrate
```

---

## Create superuser

```bash id="ibk4rt"
python manage.py createsuperuser
```

---

## Run server

```bash id="yyc4kh"
python manage.py runserver
```

---

# 🚀 Future Improvements

* REST API
* PDF reports
* User roles & permissions
* Notification system
* WhatsApp integration
* Email integration
* Cloud deployment

---

# 👨‍💻 Developer

Project developed for academic and educational purposes using Django.

---

# 📄 License

Educational and academic use project.
