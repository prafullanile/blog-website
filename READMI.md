# 📝 Django Blog Website

A **role-based Blog Web Application** built using **Python and Django**, following the **MVT (Model–View–Template)** architecture.  
The platform supports **multi-level user roles (User, Editor, Manager)** with **role-based dashboards and permissions**, secure authentication, and blog content management using Django ORM.

---

## 🚀 Features

### 🔐 Authentication & Authorization
- User Registration, Login, Logout
- Django Authentication System
- Secure password handling
- CSRF protection

### 👥 Role-Based Dashboard System
- **User**
  - View published blogs
  - Comment on blogs
  - Access user dashboard
- **Editor**
  - Create and edit blog posts
  - Manage assigned blog content
  - Limited admin permissions
- **Manager**
  - Full access to blog management
  - Manage categories
  - Assign roles and permissions

### 🛠 Blog Management
- Create, Read, Update, Delete (CRUD) blog posts
- Blog categorization
- Draft & publish workflow
- Pagination for blog listing
- Search and category filtering

### 🎨 UI & Performance
- Django Template Engine
- Template inheritance
- Responsive UI with Bootstrap
- Static and media file handling

---

## 🛠️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite  
- **Security:** Django Auth, Permissions, CSRF  
- **Version Control:** Git, GitHub  

---

## 📂 Project Structure


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/blog-website.git
cd blog-website
python -m venv venv
venv\Scripts\activate
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

🧠 Key Concepts Implemented

Role-Based Access Control (RBAC)

Django Groups & Permissions

Custom Dashboards per Role

Django ORM & Database Relations

Secure Authentication & Authorization

MVC / MVT Architecture

Backend Web Development Best Practices

ATS-Optimized Keywords

Python Developer

Django Framework

Role-Based Access Control (RBAC)

Authentication & Authorization

Django ORM

CRUD Operations

SQLite Database

Backend Web Development

User Permissions & Groups

Git & GitHub

**License**

This project is developed for learning, academic, and portfolio purposes.

🙌 Author

Prafull Nile
Python & Django Developer





