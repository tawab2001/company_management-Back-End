from django.contrib import admin
from .models import User, Company, Department, Employee, Project, PerformanceReview


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('email', 'username')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'num_departments', 'num_employees', 'num_projects')
    search_fields = ('name',)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'num_employees', 'num_projects')
    list_filter = ('company',)
    search_fields = ('name', 'company__name')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'company', 'department', 'designation', 'hired_on', 'days_employed')
    list_filter = ('company', 'department', 'designation')
    search_fields = ('name', 'email', 'designation')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'department', 'start_date', 'end_date')
    list_filter = ('company', 'department', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    filter_horizontal = ('assigned_employees',)


@admin.register(PerformanceReview)
class PerformanceReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'stage', 'review_date')
    list_filter = ('stage', 'review_date')
    search_fields = ('employee__name', 'employee__email')
