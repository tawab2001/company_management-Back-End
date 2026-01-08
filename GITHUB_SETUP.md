# خطوات رفع المشروع على GitHub

## المتطلبات الأساسية

1. **تثبيت Git** (إذا لم يكن مثبتاً):
   - تحميل من: https://git-scm.com/download/win
   - تثبيت Git على Windows
   - إعادة تشغيل Terminal بعد التثبيت

2. **إنشاء حساب على GitHub** (إذا لم يكن لديك):
   - الذهاب إلى: https://github.com
   - إنشاء حساب جديد

---

## خطوات الرفع على GitHub

### 1. تثبيت Git (إذا لم يكن مثبتاً)

- تحميل Git من: https://git-scm.com/download/win
- تثبيت Git
- إعادة تشغيل Terminal/PowerShell

### 2. فتح Terminal في مجلد المشروع

```bash
cd "d:\New folder\company_management"
```

### 3. تهيئة Git Repository

```bash
git init
```

### 4. إضافة جميع الملفات

```bash
git add .
```

### 5. عمل Commit أولي

```bash
git commit -m "Initial commit: Company Management System"
```

### 6. إنشاء Repository على GitHub

1. اذهب إلى: https://github.com/new
2. أدخل اسم المستودع (مثلاً: `company-management-system`)
3. اختر **Public** (مطلوب للتسليم)
4. **لا** تضع علامة على "Initialize with README" (لأننا لدينا README بالفعل)
5. اضغط **Create repository**

### 7. ربط المشروع المحلي بـ GitHub

بعد إنشاء المستودع، GitHub سيعطيك أوامر. استخدم هذه الأوامر:

```bash
git remote add origin https://github.com/YOUR_USERNAME/company-management-system.git
git branch -M main
git push -u origin main
```

**ملاحظة:** استبدل `YOUR_USERNAME` باسم المستخدم الخاص بك على GitHub

---

## إذا واجهت مشاكل

### مشكلة: Git غير مثبت
**الحل:** قم بتثبيت Git من https://git-scm.com/download/win

### مشكلة: طلب اسم المستخدم وكلمة المرور
**الحل:** 
- استخدم **Personal Access Token** بدلاً من كلمة المرور
- إنشاء Token: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
- أو استخدم GitHub Desktop (أسهل)

### مشكلة: الملفات كبيرة جداً
**الحل:** تأكد من أن `.gitignore` يتجاهل:
- `db.sqlite3`
- `__pycache__/`
- `env/`
- `*.log`

---

## استخدام GitHub Desktop (أسهل طريقة)

إذا كنت تفضل واجهة رسومية:

1. تحميل GitHub Desktop: https://desktop.github.com/
2. تثبيت GitHub Desktop
3. فتح GitHub Desktop
4. File → Add Local Repository
5. اختيار مجلد المشروع
6. Commit & Push

---

## التحقق من الرفع

بعد الرفع، تأكد من:
- ✅ جميع الملفات موجودة على GitHub
- ✅ README.md يظهر بشكل صحيح
- ✅ .gitignore موجود
- ✅ requirements.txt موجود
- ✅ لا توجد ملفات حساسة (مثل db.sqlite3)

---

## رابط المستودع

بعد الرفع، رابط المستودع سيكون:
```
https://github.com/YOUR_USERNAME/company-management-system
```

استخدم هذا الرابط في نموذج التسليم.

