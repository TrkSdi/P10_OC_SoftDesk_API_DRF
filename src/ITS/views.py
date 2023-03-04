from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework import status


from .serializers import (ProjectDetailSerializer, ProjectListSerializer,
                          IssuesSerializer, ContributorsSerializer, CommentsSerializer)
from ITS.models import Project, Issue, Contributor, Comment
from .permissions import IsProjectOwner



class ProjectViewset(ModelViewSet):
    
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    permissions_classes = [IsProjectOwner]
    
    def list(self, request, *args, **kwargs):
        queryset = Project.objects.filter()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.filter()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
class ContributorsViewset(ModelViewSet):
    
    queryset = Contributor.objects.all()
    serializer_class = ContributorsSerializer
    
    def list(self, request, project_pk=None):
        queryset = Contributor.objects.filter(project=project_pk)
        serializer = ContributorsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Contributor.objects.filter(pk=pk, project=project_pk)
        maildrop = get_object_or_404(queryset, pk=pk)
        serializer = ContributorsSerializer(maildrop)
        return Response(serializer.data)

class IssuesViewset(ModelViewSet):
    
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer
    
    def list(self, request, project_pk=None):
        queryset = Issue.objects.filter(project=project_pk)
        serializer = IssuesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Issue.objects.filter(pk=pk, project=project_pk)
        maildrop = get_object_or_404(queryset, pk=pk)
        serializer = IssuesSerializer(maildrop)
        return Response(serializer.data)
    
class CommentsViewset(ModelViewSet):   
    
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer

    def list(self, request, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(issue__project=project_pk, issue=issue_pk)
        serializer = CommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(pk=pk, issue__project=project_pk, issue=issue_pk)
        maildrop = get_object_or_404(queryset, pk=pk)
        serializer = CommentsSerializer(maildrop)
        return Response(serializer.data)