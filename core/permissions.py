from rest_framework.permissions import BasePermission

class RoleBasedPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        role = request.user.role
        if role == 'admin':
            return True
        if role == 'manager' and request.method in ['GET', 'POST', 'PATCH']:
            return True
        if role == 'employee' and request.method == 'GET':
            return True
        return False