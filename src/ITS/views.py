from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated

from auth.permissions import IsAdminAuthenticated
from .serializers import ProjectSerializer, IssuesSerializer, ContributorsSerializer, CommentsSerializer
from ITS.models import Project, Issue, Contributor, Comment


class ProjectViewset(ReadOnlyModelViewSet):
    
    serializer_class = ProjectSerializer
    permission_classes = []
    
    def get_queryset(self):
        return Project.objects.all()
    
class IssuesViewset(ReadOnlyModelViewSet):
    
    serializer_class = IssuesSerializer
    permission_classes = []
    
    def get_queryset(self):
        return Issue.objects.all()
    
class ContributorsViewset(ReadOnlyModelViewSet):
    
    serializer_class = ContributorsSerializer
    permission_classes = []
    
    def get_queryset(self):
        return Contributor.objects.all()

class CommentsViewset(ReadOnlyModelViewSet):
    
    serializer_class = CommentsSerializer
    permission_classes = []
    
    def get_queryset(self):
        return Comment.objects.all()
