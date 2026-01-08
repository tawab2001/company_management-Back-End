from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Company, Department, Employee, Project, PerformanceReview
from .serializers import (
    CompanySerializer, 
    DepartmentSerializer, 
    EmployeeSerializer, 
    ProjectSerializer, 
    PerformanceReviewSerializer
)
from .permissions import RoleBasedPermission


# Custom Token Authentication View (supports email as username)
@api_view(['POST'])
@permission_classes([AllowAny])
def custom_obtain_auth_token(request):
    """
    Custom token authentication that accepts email instead of username
    """
    email = request.data.get('email') or request.data.get('username')
    password = request.data.get('password')
    
    if email and password:
        user = authenticate(username=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)
    else:
        return Response({'error': 'Must include "email" and "password"'}, status=400)


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Company model - ReadOnly (GET only) as per spec
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [RoleBasedPermission]


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet for Department model - ReadOnly (GET only) as per spec
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [RoleBasedPermission]


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Employee model
    Supports: POST, GET, PATCH, DELETE as per spec
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [RoleBasedPermission]
    http_method_names = ['get', 'post', 'patch', 'delete']  # As per spec
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Project model (Bonus)
    Supports: POST, GET, PATCH, DELETE
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [RoleBasedPermission]
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class PerformanceReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for PerformanceReview model
    Supports full CRUD operations + custom transition action
    """
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [RoleBasedPermission]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['patch'])
    def transition(self, request, pk=None):
        """
        Custom action to transition PerformanceReview to a new stage
        Validates allowed transitions according to workflow rules
        """
        review = self.get_object()
        new_stage = request.data.get('stage')
        try:
            review.transition_to(new_stage)
            return Response({'status': 'transition successful', 'new_stage': new_stage})
        except ValueError as e:
            return Response({'error': str(e)}, status=400)

