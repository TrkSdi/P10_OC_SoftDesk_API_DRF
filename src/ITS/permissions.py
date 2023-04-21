from rest_framework import permissions
from .models import Project, Contributor


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            project_id = view.kwargs['pk']
            project = Project.objects.get(pk=project_id)
            if project.author_user != request.user:
                return False
            else:
                return True
        except:
            return True

    def has_object_permission(self, request, view, obj):
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
        project_id = request.resolver_match.kwargs.get('project_pk')
        project = Project.objects.get(pk=project_id)
        try:
            contributor = Contributor.objects.get(
                project_id=project_id, user_id=request.user.id)
        except Contributor.DoesNotExist:
            contributor = None
        if (contributor is not None) or (project.author_user == request.user):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return self.has_permission(request, view)
        return obj.author_user == request.user
