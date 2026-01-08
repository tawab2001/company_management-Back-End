# Company Management System - Backend API

## 📋 Overview

This is a Django REST Framework-based backend API for managing companies, departments, employees, projects, and employee performance reviews. The system implements role-based access control and a workflow system for performance reviews.

## ✨ Features

- **Company Management**: Manage companies with auto-calculated statistics
- **Department Management**: Organize departments within companies
- **Employee Management**: Full CRUD operations for employees
- **Project Management** (Bonus): Manage projects with assigned employees
- **Performance Review Workflow**: Structured workflow for employee performance reviews
- **Role-Based Access Control**: Admin, Manager, and Employee roles with different permissions
- **Token Authentication**: Secure API access using token-based authentication

## 🛠️ Technology Stack

- **Framework**: Django 6.0.1
- **API**: Django REST Framework
- **Database**: SQLite (default, can be changed to PostgreSQL/MySQL)
- **Authentication**: Token Authentication + Session Authentication

## 📦 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd company_management
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** If `requirements.txt` doesn't exist, install manually:
```bash
pip install django==6.0.1 djangorestframework django-cors-headers
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

Or use the provided script:
```bash
python create_user.py
```

This will create a test user:
- **Email**: test@example.com
- **Password**: testpass123
- **Role**: admin

### 6. Run Development Server

```bash
python manage.py runserver
```

The API will be available at: `http://127.0.0.1:8000/`

## 📚 API Documentation

### Base URL
```
http://127.0.0.1:8000/api/
```

### Authentication

All API endpoints require authentication except the token endpoint.

#### Get Authentication Token

**Endpoint:** `POST /api-token-auth/`

**Request:**
```json
{
    "email": "test@example.com",
    "password": "testpass123"
}
```

**Response:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

**Usage:**
Include the token in request headers:
```
Authorization: Token YOUR_TOKEN_HERE
```

---

### API Endpoints

#### Companies

- **GET** `/api/companies/` - List all companies
- **GET** `/api/companies/{id}/` - Get single company

**Note:** Companies are read-only (GET only) as per specification.

---

#### Departments

- **GET** `/api/departments/` - List all departments
- **GET** `/api/departments/{id}/` - Get single department

**Note:** Departments are read-only (GET only) as per specification.

---

#### Employees

- **GET** `/api/employees/` - List all employees
- **GET** `/api/employees/{id}/` - Get single employee
- **POST** `/api/employees/` - Create new employee
- **PATCH** `/api/employees/{id}/` - Update employee
- **DELETE** `/api/employees/{id}/` - Delete employee

**Create Employee Example:**
```json
{
    "company": 1,
    "department": 1,
    "name": "Ahmed Mohamed",
    "email": "ahmed@example.com",
    "mobile_number": "01234567890",
    "address": "Cairo, Egypt",
    "designation": "Software Developer",
    "hired_on": "2024-01-15"
}
```

---

#### Projects (Bonus)

- **GET** `/api/projects/` - List all projects
- **GET** `/api/projects/{id}/` - Get single project
- **POST** `/api/projects/` - Create new project
- **PATCH** `/api/projects/{id}/` - Update project
- **DELETE** `/api/projects/{id}/` - Delete project

**Create Project Example:**
```json
{
    "company": 1,
    "department": 1,
    "name": "New System Development",
    "description": "Developing a new management system",
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "assigned_employees": [1, 2, 3]
}
```

---

#### Performance Reviews

- **GET** `/api/reviews/` - List all reviews
- **GET** `/api/reviews/{id}/` - Get single review
- **POST** `/api/reviews/` - Create new review
- **PATCH** `/api/reviews/{id}/` - Update review
- **DELETE** `/api/reviews/{id}/` - Delete review
- **PATCH** `/api/reviews/{id}/transition/` - Transition review stage

**Create Review Example:**
```json
{
    "employee": 1,
    "stage": "pending_review",
    "review_date": "2024-01-20",
    "feedback": "Excellent performance"
}
```

**Transition Review Example:**
```json
{
    "stage": "review_scheduled"
}
```

**Allowed Stages:**
- `pending_review`
- `review_scheduled`
- `feedback_provided`
- `under_approval`
- `review_approved`
- `review_rejected`

**Allowed Transitions:**
- `pending_review` → `review_scheduled`
- `review_scheduled` → `feedback_provided`
- `feedback_provided` → `under_approval`
- `under_approval` → `review_approved` or `review_rejected`
- `review_rejected` → `feedback_provided`

---

## 🔐 Security & Permissions

### Role-Based Access Control

The system implements three roles with different permissions:

1. **Admin**
   - Full access to all operations (GET, POST, PATCH, DELETE)

2. **Manager**
   - GET: View all resources
   - POST: Create new resources
   - PATCH: Update existing resources
   - DELETE: Not allowed

3. **Employee**
   - GET: View resources only
   - POST, PATCH, DELETE: Not allowed

### Authentication Methods

- **Token Authentication**: Primary method for API access
- **Session Authentication**: For Django admin interface

---

## 📊 Data Models

### User
- Email (Login ID)
- Username
- Role (admin/manager/employee)
- Password

### Company
- Name
- Number of Departments (auto-calculated)
- Number of Employees (auto-calculated)
- Number of Projects (auto-calculated)

### Department
- Company (ForeignKey)
- Name
- Number of Employees (auto-calculated)
- Number of Projects (auto-calculated)

### Employee
- Company (ForeignKey)
- Department (ForeignKey)
- Name
- Email
- Mobile Number
- Address
- Designation
- Hired On (optional)
- Days Employed (auto-calculated)

### Project (Bonus)
- Company (ForeignKey)
- Department (ForeignKey)
- Name
- Description
- Start Date
- End Date
- Assigned Employees (ManyToMany)

### Performance Review
- Employee (ForeignKey)
- Stage (with workflow transitions)
- Review Date
- Feedback

---

## ✅ Task Completion Checklist

### Mandatory Requirements

- [x] **Data Models**: All models implemented with required fields
- [x] **User Accounts**: Custom User model with email login and roles
- [x] **Company Model**: With auto-calculated properties
- [x] **Department Model**: With auto-calculated properties
- [x] **Employee Model**: With all required fields and auto-calculated days_employed
- [x] **Performance Review Workflow**: All stages and transitions implemented
- [x] **Role-Based Access Control**: Admin, Manager, Employee permissions
- [x] **Authentication**: Token-based authentication
- [x] **Company API**: GET endpoints (ReadOnly)
- [x] **Department API**: GET endpoints (ReadOnly)
- [x] **Employee API**: Full CRUD operations
- [x] **RESTful API**: Proper HTTP methods and conventions
- [x] **Security**: Secure data handling and authentication

### Bonus Requirements

- [x] **Project Model**: Implemented with all required fields
- [x] **Project API**: Full CRUD operations
- [x] **Logging Configuration**: Basic logging setup in settings
- [ ] **Comprehensive Logging**: Detailed logging in views/models (partially implemented)
- [ ] **Comprehensive Testing**: Unit and integration tests (basic tests exist)

### Documentation

- [x] **README.md**: This file
- [ ] **API Documentation**: Detailed endpoint documentation (can be generated from code)
- [ ] **Setup Instructions**: Included in this README

---

## 🧪 Testing

### Run Tests

```bash
python manage.py test
```

### Test Coverage

Basic tests are included for:
- Model creation
- API endpoints

**Note:** More comprehensive tests are recommended for production use.

---

## 📝 Assumptions & Considerations

1. **Companies and Departments**: Read-only (GET only) as per specification. They should be created via Django Admin.

2. **Email as Username**: Custom User model uses email as the login identifier.

3. **Auto-calculated Fields**: Properties like `num_departments`, `num_employees`, `days_employed` are calculated dynamically and not stored in the database.

4. **Workflow Transitions**: Performance Review transitions are validated to ensure only allowed transitions are permitted.

5. **Token Authentication**: Primary authentication method. Tokens are created automatically on first login.

---

## 🔧 Configuration

### Database

Default: SQLite (`db.sqlite3`)

To use PostgreSQL or MySQL, update `DATABASES` in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Custom User Model

The project uses a custom User model (`core.User`). This is configured in `settings.py`:

```python
AUTH_USER_MODEL = 'core.User'
```

---

## 🐛 Troubleshooting

### Common Issues

1. **Import Error for Views**
   - Ensure `core/views.py` exists and contains all ViewSets

2. **Authentication Errors**
   - Verify token is included in request headers
   - Check token format: `Authorization: Token YOUR_TOKEN`

3. **Permission Denied**
   - Verify user role has required permissions
   - Check `RoleBasedPermission` implementation

4. **Migration Errors**
   - Run: `python manage.py makemigrations`
   - Then: `python manage.py migrate`

---

## 📞 Support

For issues or questions, please refer to:
- Django Documentation: https://docs.djangoproject.com/
- DRF Documentation: https://www.django-rest-framework.org/

---

## 📄 License

This project is part of an evaluation task.

---

## 👤 Author

Developed as part of Company Management System evaluation task.

---

**Last Updated:** January 2026

