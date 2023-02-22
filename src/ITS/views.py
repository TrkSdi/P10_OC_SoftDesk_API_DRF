from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import ProjectSerializer, IssuesSerializer, ContributorsSerializer, CommentsSerializer
from ITS.models import Project, Issues, Contributors, Comments


class ProjectViewset(ReadOnlyModelViewSet):
    
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        return Project.objects.all()
    
class IssuesViewset(ReadOnlyModelViewSet):
    
    serializer_class = IssuesSerializer
    
    def get_queryset(self):
        return Issues.objects.all()
    
class ContributorsViewset(ReadOnlyModelViewSet):
    
    serializer_class = ContributorsSerializer
    
    def get_queryset(self):
        return Contributors.objects.all()

class CommentsViewset(ReadOnlyModelViewSet):
    
    serializer_class = CommentsSerializer
    
    def get_queryset(self):
        return Comments.objects.all()