"""
Script to create a test user for API testing
Run: python create_user.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company_management.settings')
django.setup()

from core.models import User

# Create or get user
email = 'test@example.com'
password = 'testpass123'

try:
    user = User.objects.get(email=email)
    print(f"User already exists: {email}")
    print("Updating password...")
    user.set_password(password)
    user.role = 'admin'  # Set as admin for full access
    user.save()
    print(f"Password updated successfully!")
except User.DoesNotExist:
    user = User.objects.create_user(
        email=email,
        username='testuser',
        password=password,
        role='admin'
    )
    print(f"User created successfully!")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Role: {user.role}")

print("\nYou can now use these credentials in Postman:")
print(f"Email: {email}")
print(f"Password: {password}")

