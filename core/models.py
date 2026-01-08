from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)  # Login ID
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('manager', 'Manager'), ('employee', 'Employee')])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Company(models.Model):
    name = models.CharField(max_length=255)

    @property
    def num_departments(self):
        return self.department_set.count()

    @property
    def num_employees(self):
        return self.employee_set.count()

    @property
    def num_projects(self):
        return self.project_set.count()

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    @property
    def num_employees(self):
        return self.employee_set.count()

    @property
    def num_projects(self):
        return self.project_set.count()

class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    address = models.TextField()
    designation = models.CharField(max_length=255)
    hired_on = models.DateField(null=True, blank=True)

    @property
    def days_employed(self):
        if self.hired_on:
            return (timezone.now().date() - self.hired_on).days
        return 0

# Bonus: Project Model
class Project(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_employees = models.ManyToManyField(Employee)


class PerformanceReview(models.Model):
    STAGES = [
        ('pending_review', 'Pending Review'),
        ('review_scheduled', 'Review Scheduled'),
        ('feedback_provided', 'Feedback Provided'),
        ('under_approval', 'Under Approval'),
        ('review_approved', 'Review Approved'),
        ('review_rejected', 'Review Rejected'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    stage = models.CharField(max_length=50, choices=STAGES, default='pending_review')
    review_date = models.DateField(null=True, blank=True)
    feedback = models.TextField(blank=True)
    # Add fields like manager_approver if needed

    def transition_to(self, new_stage):
        allowed_transitions = {
            'pending_review': ['review_scheduled'],
            'review_scheduled': ['feedback_provided'],
            'feedback_provided': ['under_approval'],
            'under_approval': ['review_approved', 'review_rejected'],
            'review_rejected': ['feedback_provided'],
        }
        if new_stage in allowed_transitions.get(self.stage, []):
            self.stage = new_stage
            self.save()
        else:
            raise ValueError("Invalid transition")