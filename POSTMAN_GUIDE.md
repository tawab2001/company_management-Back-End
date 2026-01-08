# دليل اختبار API في Postman

## معلومات أساسية
- **Base URL**: `http://127.0.0.1:8000`
- **Authentication**: Token Authentication
- جميع الـ endpoints تتطلب Authentication

---

## 1. الحصول على Token (Authentication)

### Endpoint: POST `/api-token-auth/`

**Headers:**
```
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "email": "your_email@example.com",
    "password": "your_password"
}
```

**ملاحظة:** يمكنك استخدام `email` أو `username` في الـ body (كلاهما يعمل)

**Response:**
```json
{
    "token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

**ملاحظة:** استخدم الـ token في جميع الطلبات التالية في Header:
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

---

## 2. Companies (الشركات)

### GET `/api/companies/` - عرض جميع الشركات
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
- **Response**: قائمة بجميع الشركات

### GET `/api/companies/{id}/` - عرض شركة محددة
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
- **Example**: `GET /api/companies/1/`

---

## 3. Departments (الأقسام)

### GET `/api/departments/` - عرض جميع الأقسام
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

### GET `/api/departments/{id}/` - عرض قسم محدد
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
- **Example**: `GET /api/departments/1/`

---

## 4. Employees (الموظفين)

### GET `/api/employees/` - عرض جميع الموظفين
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

### GET `/api/employees/{id}/` - عرض موظف محدد
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

### POST `/api/employees/` - إضافة موظف جديد
- **Method**: POST
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
  - `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
    "company": 1,
    "department": 1,
    "name": "أحمد محمد",
    "email": "ahmed@example.com",
    "mobile_number": "01234567890",
    "address": "القاهرة، مصر",
    "designation": "مطور برمجيات",
    "hired_on": "2024-01-15"
}
```

### PATCH `/api/employees/{id}/` - تحديث موظف
- **Method**: PATCH
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
  - `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
    "designation": "مطور أول",
    "mobile_number": "01234567891"
}
```

### DELETE `/api/employees/{id}/` - حذف موظف
- **Method**: DELETE
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

---

## 5. Projects (المشاريع)

### GET `/api/projects/` - عرض جميع المشاريع
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

### GET `/api/projects/{id}/` - عرض مشروع محدد
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

### POST `/api/projects/` - إضافة مشروع جديد
- **Method**: POST
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
  - `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
    "company": 1,
    "department": 1,
    "name": "مشروع تطوير النظام",
    "description": "تطوير نظام إدارة الشركات",
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "assigned_employees": [1, 2]
}
```

### PATCH `/api/projects/{id}/` - تحديث مشروع
- **Method**: PATCH
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
  - `Content-Type: application/json`

### DELETE `/api/projects/{id}/` - حذف مشروع
- **Method**: DELETE
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

---

## 6. Performance Reviews (تقييمات الأداء)

### GET `/api/reviews/` - عرض جميع التقييمات
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

### GET `/api/reviews/{id}/` - عرض تقييم محدد
- **Method**: GET
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

### POST `/api/reviews/` - إضافة تقييم جديد
- **Method**: POST
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
  - `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
    "employee": 1,
    "stage": "pending_review",
    "review_date": "2024-01-20",
    "feedback": "أداء ممتاز"
}
```

### PATCH `/api/reviews/{id}/` - تحديث تقييم
- **Method**: PATCH
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
  - `Content-Type: application/json`

### DELETE `/api/reviews/{id}/` - حذف تقييم
- **Method**: DELETE
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`

### PATCH `/api/reviews/{id}/transition/` - تغيير مرحلة التقييم
- **Method**: PATCH
- **Headers**: 
  - `Authorization: Token YOUR_TOKEN`
  - `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
    "stage": "review_scheduled"
}
```
- **المراحل المتاحة:**
  - `pending_review`
  - `review_scheduled`
  - `feedback_provided`
  - `under_approval`
  - `review_approved`
  - `review_rejected`

---

## خطوات الاختبار في Postman

### 1. إنشاء مستخدم جديد (من Django Admin أو Shell)
```bash
python manage.py createsuperuser
```

أو من Django Shell:
```python
from core.models import User
user = User.objects.create_user(
    email='test@example.com',
    username='testuser',
    password='testpass123',
    role='admin'
)
```

### 2. الحصول على Token
1. افتح Postman
2. أنشئ طلب جديد: `POST http://127.0.0.1:8000/api-token-auth/`
3. في تبويب **Body**، اختر **raw** و **JSON**
4. أدخل:
```json
{
    "username": "test@example.com",
    "password": "testpass123"
}
```
5. اضغط **Send**
6. انسخ الـ token من الـ response

### 3. إعداد Authorization لجميع الطلبات
1. في Postman، اضغط على **Collections**
2. أنشئ Collection جديد باسم "Company Management API"
3. اضغط على Collection → **Authorization** tab
4. اختر **Type**: `Token`
5. الصق الـ token في حقل **Token**
6. الآن جميع الطلبات في هذا Collection ستستخدم هذا الـ token تلقائياً

### 4. اختبار الـ Endpoints
1. أضف طلبات جديدة في Collection
2. استخدم الـ URLs المذكورة أعلاه
3. تأكد من تشغيل السيرفر: `python manage.py runserver`

---

## مثال على Collection في Postman

يمكنك إنشاء Collection يحتوي على:

1. **Authentication**
   - Get Token

2. **Companies**
   - Get All Companies
   - Get Company by ID

3. **Departments**
   - Get All Departments
   - Get Department by ID

4. **Employees**
   - Get All Employees
   - Get Employee by ID
   - Create Employee
   - Update Employee
   - Delete Employee

5. **Projects**
   - Get All Projects
   - Get Project by ID
   - Create Project
   - Update Project
   - Delete Project

6. **Reviews**
   - Get All Reviews
   - Get Review by ID
   - Create Review
   - Update Review
   - Delete Review
   - Transition Review Stage

---

## ملاحظات مهمة

1. **تأكد من تشغيل السيرفر:**
   ```bash
   python manage.py runserver
   ```

2. **إنشاء بيانات تجريبية:**
   - استخدم Django Admin: `http://127.0.0.1:8000/admin/`
   - أو أنشئ بيانات من Django Shell

3. **أخطاء شائعة:**
   - **401 Unauthorized**: تأكد من إضافة Token في Headers
   - **400 Bad Request**: تحقق من صحة البيانات المرسلة
   - **404 Not Found**: تأكد من صحة الـ URL والـ ID

4. **CSRF Token**: إذا كنت تستخدم Session Authentication، قد تحتاج CSRF token

---

## مثال كامل لطلب POST

**URL:** `POST http://127.0.0.1:8000/api/employees/`

**Headers:**
```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
Content-Type: application/json
```

**Body (raw JSON):**
```json
{
    "company": 1,
    "department": 1,
    "name": "محمد أحمد",
    "email": "mohamed@example.com",
    "mobile_number": "01012345678",
    "address": "الإسكندرية، مصر",
    "designation": "مهندس برمجيات",
    "hired_on": "2024-01-10"
}
```

**Expected Response (201 Created):**
```json
{
    "id": 1,
    "company": 1,
    "department": 1,
    "name": "محمد أحمد",
    "email": "mohamed@example.com",
    "mobile_number": "01012345678",
    "address": "الإسكندرية، مصر",
    "designation": "مهندس برمجيات",
    "hired_on": "2024-01-10",
    "days_employed": 365
}
```

