from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions
from .models import Project



class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return True
            
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS :
            return True
        return obj.author_user == request.user 

class IsProjectContributor(BasePermission):
    def has_permission(self, request, view):
        if request.user in Project.contributor:
            return True