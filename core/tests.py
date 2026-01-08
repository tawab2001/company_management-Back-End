from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Company

class ModelTestCase(TestCase):
    def test_company_creation(self):
        company = Company.objects.create(name='Test Co')
        self.assertEqual(company.name, 'Test Co')

class CompanyAPITestCase(APITestCase):
    def test_get_companies(self):
        response = self.client.get('/api/companies/')
        self.assertEqual(response.status_code, 200)  # Add auth if needed

