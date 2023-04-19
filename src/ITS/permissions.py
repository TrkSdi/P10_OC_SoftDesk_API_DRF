from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import permissions
from .models import Project, Contributor




class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author_user == request.user


class IsProjectOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs['project_pk']
        project = Project.objects.get(pk=project_id)
        if project.author_user == request.user:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs['project_pk']
        project = Project.objects.get(pk=project_id)
        contributor = Contributor.objects.get(
                project_id=project_id, user_id=request.user.id)
        if contributor is not None or project.author_user == request.user:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return self.has_permission(request, view)
        return obj.author_user == request.user

