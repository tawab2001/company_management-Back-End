# حل مشاكل API - Troubleshooting Guide

## خطأ 400 Bad Request

### 1. مشكلة في البيانات المرسلة (Request Body)

**الأسباب الشائعة:**
- البيانات ناقصة (مثلاً: `company` أو `department` مش موجودين)
- نوع البيانات غلط (مثلاً: أرسلت string بدل number)
- الـ JSON مش صحيح (syntax error)

**الحل:**
- تأكد إن كل الحقول المطلوبة موجودة
- تأكد إن الـ JSON صحيح (استخدم JSON validator)
- شوف الـ response بالتفصيل - هيكون فيه رسالة توضح إيه المشكلة

**مثال على خطأ شائع:**
```json
// ❌ غلط - company مش موجود
{
    "name": "أحمد",
    "email": "ahmed@example.com"
}

// ✅ صح - company و department موجودين
{
    "company": 1,
    "department": 1,
    "name": "أحمد",
    "email": "ahmed@example.com",
    "mobile_number": "01234567890",
    "address": "القاهرة",
    "designation": "مطور"
}
```

---

### 2. مشكلة في Authentication (Token)

**الأعراض:**
- خطأ 401 Unauthorized
- خطأ 403 Forbidden

**الحل:**
1. تأكد إنك جبت الـ token صح:
   ```
   POST http://127.0.0.1:8000/api-token-auth/
   Body: {"email": "your_email", "password": "your_password"}
   ```

2. تأكد إنك حاطط الـ token في Headers:
   ```
   Authorization: Token YOUR_TOKEN_HERE
   ```
   **مهم:** كلمة "Token" لازم تكون موجودة قبل الـ token نفسه

3. تأكد إن الـ token مش منتهي (لو عملت logout أو غيرت الـ password)

---

### 3. مشكلة في Foreign Key (company أو department مش موجودين)

**الخطأ:**
```json
{
    "company": ["Invalid pk \"1\" - object does not exist."]
}
```

**الحل:**
1. أولاً، أنشئ Company:
   ```
   POST /api/companies/
   Body: {"name": "شركة التطوير"}
   ```
   خد الـ ID اللي هيجيلك في الـ response

2. بعدين أنشئ Department:
   ```
   POST /api/departments/
   Body: {"company": 1, "name": "قسم البرمجيات"}
   ```
   خد الـ ID

3. استخدم الـ IDs دي في Employee:
   ```
   POST /api/employees/
   Body: {
       "company": 1,
       "department": 1,
       ...
   }
   ```

**أو استخدم Django Admin:**
- افتح `http://127.0.0.1:8000/admin/`
- أنشئ Company و Department من هناك
- خد الـ IDs واستخدمها في Postman

---

### 4. مشكلة في Permissions (الصلاحيات)

**الأعراض:**
- خطأ 403 Forbidden
- "You do not have permission to perform this action"

**الأسباب:**
- المستخدم مش admin أو manager
- الـ role مش صحيح

**الحل:**
1. تأكد إن المستخدم عنده role صحيح:
   - `admin`: يقدر يعمل كل حاجة
   - `manager`: يقدر يعمل GET, POST, PATCH بس
   - `employee`: يقدر يعمل GET بس

2. غير الـ role من Django Admin أو Shell:
   ```python
   from core.models import User
   user = User.objects.get(email='your_email@example.com')
   user.role = 'admin'
   user.save()
   ```

---

### 5. مشكلة في Date Format

**الخطأ:**
```json
{
    "hired_on": ["Date has wrong format. Use one of these formats instead: YYYY-MM-DD."]
}
```

**الحل:**
استخدم الصيغة الصحيحة:
```json
{
    "hired_on": "2024-01-15"  // ✅ صح
}
```

**مش:**
```json
{
    "hired_on": "15/01/2024"  // ❌ غلط
}
```

---

### 6. مشكلة في ManyToMany Field (assigned_employees)

**مثال على Project:**
```json
{
    "company": 1,
    "department": 1,
    "name": "مشروع جديد",
    "description": "وصف المشروع",
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "assigned_employees": [1, 2, 3]  // ✅ array of IDs
}
```

**مهم:** 
- `assigned_employees` لازم يكون array
- الـ Employee IDs لازم تكون موجودة فعلاً

---

## خطوات Debugging (كيف تكتشف المشكلة)

### 1. شوف الـ Response بالتفصيل

في Postman، شوف الـ **Body** في الـ response - هيكون فيه تفاصيل الخطأ:

```json
{
    "company": ["This field is required."],
    "email": ["Enter a valid email address."]
}
```

### 2. تأكد من الـ Headers

```
Content-Type: application/json
Authorization: Token YOUR_TOKEN
```

### 3. تأكد من الـ URL

```
✅ http://127.0.0.1:8000/api/employees/
❌ http://127.0.0.1:8000/api/employee/  (مفرد)
❌ http://127.0.0.1:8000/employees/     (ناقص /api/)
```

### 4. تأكد إن السيرفر شغال

```bash
python manage.py runserver
```

---

## أمثلة على طلبات صحيحة

### 1. إنشاء Company (من Django Admin فقط)
لأن CompanyViewSet هو ReadOnly (GET بس)

### 2. إنشاء Department (من Django Admin فقط)
لأن DepartmentViewSet هو ReadOnly (GET بس)

### 3. إنشاء Employee

**Request:**
```
POST http://127.0.0.1:8000/api/employees/
```

**Headers:**
```
Authorization: Token YOUR_TOKEN
Content-Type: application/json
```

**Body:**
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

**Response (201 Created):**
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

---

## نصائح مهمة

1. **ابدأ بسيط:** جرب GET requests أولاً (مش محتاجة body)
2. **استخدم Django Admin:** لإنشاء Companies و Departments
3. **شوف الـ Response:** دائماً اقرأ رسالة الخطأ بالتفصيل
4. **تأكد من الـ Token:** لو جالك 401، جدد الـ token
5. **تأكد من الـ IDs:** استخدم IDs موجودة فعلاً في الـ database

---

## إذا لسه في مشكلة

1. شوف الـ response بالتفصيل في Postman
2. افتح Django terminal وشوف الـ error logs
3. تأكد إن كل الـ migrations اتعملت:
   ```bash
   python manage.py migrate
   ```
4. تأكد إن في بيانات في الـ database (Companies, Departments)

