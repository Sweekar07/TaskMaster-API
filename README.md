# TaskMaster API

A comprehensive Django REST API for task management featuring JWT authentication, role-based access control, and security patterns.

## 🎯 Project Overview
TaskMaster API is a full-featured backend system designed for task management applications. Built with Django REST Framework, it provides secure user authentication, role-based permissions, and complete CRUD operations for tasks and comments.

## 🔥 Core Features
- **JWT Authentication System** with automatic token rotation
- **Role-Based Access Control** (Admin & User roles)
- **Task Management** with customizable status workflows
- **Comment System** with permission-based visibility
- **Soft Delete Implementation** maintaining data relationships
- **Email-Based Authentication** using custom user model
- **RESTful API Design** following OpenAPI standards

## 💻 Technology Stack
- **Backend Framework:** Django 4.2, Django REST Framework 3.14+
- **Authentication:** JWT (djangorestframework-simplejwt)
- **Database:** PostgreSQL with Django ORM
- **Security:** Advanced permission classes, password validation
- **API Documentation:** Self-documenting REST endpoints
- **Development:** Python 3.8+, pip package management

## 🏆 Features
- Pagination support for large datasets
- Comprehensive input validation and error handling
- Database migrations for deployment consistency
- Role-based endpoint access control
- Token blacklisting for secure logout


## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+
- PostgreSQL
-  Git

### Installation & Setup

# 1. Clone the repository
```
git clone https://github.com/Sweekar07/TaskMaster-API.git
cd taskmaster-api
```

# 2. Create virtual environment
```
python -m venv venv
```

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Configure environment variables
### Create .env file in project root:
####  Edit .env with your database credentials:
```
DB_NAME=task_management_db
DB_USER=your_username  
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

# 6. Create a PostgreSQL database
```
createdb task_management_db
```

# 7. Run migrations
```
python manage.py makemigrations
python manage.py migrate
```

# 8. Create superuser (admin)
```
python manage.py createsuperuser
```

# 9. Start the development server
```
python manage.py runserver
```

# 10. For testing APIs using Postman, etc.
- Either create a new environment.
- Or use the global environment with the below key and value

```
variable: base_url; key value: http://localhost:8000/api
variable: access_token; value: {leave it empty, it will auto populate after login}
variable: refresh_token; value: {leave it empty, it will auto populate after login}
```

