from rest_framework import serializers
from .models import (
    Company,
    Department,
    Employee,
    Project,              # Bonus
    PerformanceReview,
    User,                 # لو عندك Custom User
)

class CompanySerializer(serializers.ModelSerializer):
    num_departments = serializers.ReadOnlyField()
    num_employees = serializers.ReadOnlyField()
    num_projects = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    num_employees = serializers.ReadOnlyField()
    num_projects = serializers.ReadOnlyField()

    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    days_employed = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = '__all__'


# Bonus
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class PerformanceReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceReview
        fields = '__all__'


# لو عندك Custom User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role')
        extra_kwargs = {'password': {'write_only': True}}