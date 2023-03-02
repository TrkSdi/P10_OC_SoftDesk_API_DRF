from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework import status


from .serializers import (ProjectDetailSerializer, ProjectListSerializer,
                          IssuesSerializer, ContributorsSerializer, CommentsSerializer)
from ITS.models import Project, Issue, Contributor, Comment


class ProjectListViewset(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
    

class ProjectDetailViewset(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer

class ContributorsViewset(ListCreateAPIView):
    
    queryset = Contributor.objects.all()
    serializer_class = ContributorsSerializer
    
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        return serializer.save(project_id=project_id)
    
    def list(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        queryset = self.queryset.filter(project_id=project_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
class DeleteContributorViewSet(RetrieveDestroyAPIView):
    
    queryset = Contributor.objects.all()
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        queryset = self.queryset.filter(project_id=project_id)
        contributor = self.kwargs.get('user_id')
        queryset = self.queryset.filter(user_id=contributor)
        return queryset

class IssuesViewset(ListCreateAPIView):
    
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer
    
    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_id')
        return serializer.save(project_id=project_id)
    
    def list(self, request, *args, **kwargs):
        project_id = self.kwargs.get('project_id')
        queryset = self.queryset.filter(project_id=project_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
"""
class ProjectViewset(ModelViewSet):
    
    serializer_class = ProjectListSerializer
    detail_serializer_class = ProjectDetailSerializer
    
    
    def get_queryset(self):
        return Project.objects.all()
    
    def get_serializer_class(self):
    
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
    
    @action(detail=True, methods=['GET','POST', 'DELETE'], serializer_class=ContributorsSerializer)
    def users(self, request, pk):
        if request.method == 'GET':
            project = Project.objects.get(pk=pk)
            contributors = project.contributor.all()
            serializer = ContributorsSerializer(contributors, many=True)
            return Response(serializer.data)
        
        if request.method == 'POST':
            project = Project.objects.get(pk=pk)
            serializer = ContributorsSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if request.method == 'DELETE':
            contributor = project.contributor.filter(id__in=pk)
            contributor.delete()
            return Response(status=status.HTTP_200_OK)
 """

    
class CommentsViewset(ReadOnlyModelViewSet):
    
    serializer_class = CommentsSerializer
    permission_classes = []
    
    def get_queryset(self):
        return Comment.objects.all()
