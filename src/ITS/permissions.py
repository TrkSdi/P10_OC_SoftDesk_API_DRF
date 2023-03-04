from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions


class IsAdminAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and 
                    request.user.is_authenticated and 
                    request.user.is_superuser)

class IsProjectOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS :
            return True
        return obj.author_user == request.user and request.user.is_authenticated()

class IsIssueOwner(BasePermission):
    pass

class IsCommentOwber(BasePermission):
    pass