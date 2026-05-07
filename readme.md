# 📦 StockSync ERP

A modern ERP web application built with Django for complete business management, including:

* Clients
* Employees
* Inventory
* Product stock operations
* Purchases and sales
* Financial management
* Smart dashboard analytics

---

# 🚀 Technologies Used

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

## Libraries

* validate-docbr → CPF/CNPJ validation
* email-validator → email validation
* IMask.js → automatic input masks

---

# 🎨 Features

## 📊 Smart Dashboard

Real-time dashboard integrated with the database displaying:

* Total clients
* Total employees
* Total inventory value
* Low stock products
* Overdue payments
* Accounts payable
* Accounts receivable
* Monthly purchases and sales
* Recent stock movements
* Featured products
* Financial charts

---

# 👥 Clients & Employees

## Features

* Create
* Edit
* Delete
* Dynamic search
* Interactive table selection
* Automatic input masks
* CPF/CNPJ validation
* Email validation

## Validations

* Valid CPF
* Valid CNPJ
* Valid email
* Automatic masks for:

  * CPF
  * CNPJ
  * Phone number
  * Mobile number
  * ZIP code
  * State abbreviation

---

# 📦 Inventory

## Features

* Product registration
* Stock control
* Minimum stock alerts
* Cost price
* Selling price
* Automatic categories
* Search by name or code

---

# 🔄 Inventory Operations

## Available operations

### Stock Entry

* Adds units to inventory

### Stock Exit

* Removes units from inventory

### Purchase

* Adds products to stock
* Generates financial records

### Sale

* Removes products from stock
* Generates receivable records

---

# 💰 Financial Management

## Features

* Financial control
* Automatic status updates
* Automatic overdue detection
* Manual financial entries
* Integrated with purchases and sales

## Status Types

| Status     | Color  |
| ---------- | ------ |
| Paid       | Green  |
| Pending    | Orange |
| Receivable | Blue   |
| Overdue    | Red    |
| Cancelled  | Gray   |

---

# 🗄️ Database

The system uses SQLite integrated with Django ORM.

## Main tables

* Clients
* Employees
* Products
* Categories
* Financial records
* Stock operations

---

# 🔐 Authentication & Security

* Django Authentication System
* Protected routes
* Superuser access
* CSRF protection

---

# 📁 Project Structure

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

# ⚙️ Full Installation Guide

# ✅ 1. Install Python

Download Python:

https://www.python.org/downloads/

During installation:

✅ check:

```text
Add Python to PATH
```

---

# ✅ 2. Verify Python Installation

Open terminal:

```bash
python --version
```

or:

```bash
py --version
```

---

# ✅ 3. Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
```

---

# ✅ 4. Open Project Folder

```bash
cd StockSync
```

---

# ✅ 5. Create Virtual Environment

## Windows

```bash
python -m venv venv
```

## Linux / Mac

```bash
python3 -m venv venv
```

---

# ✅ 6. Activate Virtual Environment

## Windows

```bash
venv\Scripts\activate
```

## Linux / Mac

```bash
source venv/bin/activate
```

---

# ✅ 7. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ✅ 8. Run Database Migrations

```bash
python manage.py migrate
```

---

# ✅ 9. Create Superuser

```bash
python manage.py createsuperuser
```

Fill:

* username
* email
* password

---

# ✅ 10. Start Server

```bash
python manage.py runserver
```

---

# 🌐 Access System

Open in browser:

```text
http://127.0.0.1:8000
```

---

# 🔐 Admin Panel

```text
http://127.0.0.1:8000/admin
```

Use the superuser credentials created previously.

---

# 📦 Manual Library Installation

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

# 🧩 Libraries Used

## validate-docbr

Used for:

* CPF validation
* CNPJ validation

---

## email-validator

Used for:

* Email validation
* Domain verification
* MX record verification

---

## IMask.js

Used for automatic masks:

* CPF
* CNPJ
* Phone numbers
* ZIP code
* Currency values

---

# 🔄 Useful Commands

## Create Migrations

```bash
python manage.py makemigrations
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

---

# 🚀 Future Improvements

* REST API
* PDF reports
* User roles & permissions
* Notification system
* Image upload
* WhatsApp integration
* Email integration
* Supplier management
* Cash flow management
* Advanced charts
* Cloud deployment

---

# 👨‍💻 Developer

Project developed for academic purposes and web development learning using Django.

---

# 📄 License

Educational and academic use project.
