from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated

from auth.permissions import IsAdminAuthenticated
from .serializers import ProjectSerializer, IssuesSerializer, ContributorsSerializer, CommentsSerializer
from ITS.models import Project, Issues, Contributors, Comments


class ProjectViewset(ReadOnlyModelViewSet):
    
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Project.objects.all()
    
class IssuesViewset(ReadOnlyModelViewSet):
    
    serializer_class = IssuesSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Issues.objects.all()
    
class ContributorsViewset(ReadOnlyModelViewSet):
    
    serializer_class = ContributorsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Contributors.objects.all()

class CommentsViewset(ReadOnlyModelViewSet):
    
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Comments.objects.all()

class AdminProjectViewset(ModelViewSet):
    
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminAuthenticated]
    
    def get_queryset(self):
        return Project.objects.all()

class AdminContribViewset(ModelViewSet):
    
    serializer_class = ContributorsSerializer
    permission_classes = [IsAdminAuthenticated]
    
    def get_queryset(self):
        return Contributors.objects.all()

class AdminIssuesViewset(ModelViewSet):
    
    serializer_class = IssuesSerializer
    permission_classes = [IsAdminAuthenticated]
    
    def get_queryset(self):
        return Issues.objects.all()

class AdminCommentsViewset(ModelViewSet):
    
    serializer_class = CommentsSerializer
    permission_classes = [IsAdminAuthenticated]
    
    def get_queryset(self):
        return Comments.objects.all()