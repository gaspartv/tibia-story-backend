from rest_framework import permissions
from rest_framework.views import View
from .models import User


class IsUserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return request.user.is_authenticated and obj == request.user


class SalesmanPermission(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_staff == True
        )
