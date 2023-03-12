from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions
from .models import Project, Contributor



class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return True
            
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author_user == request.user 

class IsContributor(BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk')
        contributor = Contributor.objects.filter(project__id=project_id, user = request.user).count()
        return contributor > 0
    
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
    
class IsProjectOwner(BasePermission):
    #GET POST
    def has_permission(self, request, view):
        project_id = view.kwargs.get('project_pk')
        project = Project.objects.filter(pk=project_id).first()
        if project and project.author_user != request.user:
            return False
        return True
    
    # PUT PATCH DELETE    
    def has_object_permission(self, request, view, obj):
        return obj.author_user == request.user

        