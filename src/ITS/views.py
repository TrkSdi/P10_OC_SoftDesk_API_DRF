from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import (ProjectDetailSerializer, ProjectListSerializer,
                          IssuesSerializer, ContributorsSerializer,
                          CommentsSerializer)
from .models import Project, Issue, Contributor, Comment
from .permissions import IsOwnerOrReadOnly, IsContributor, IsProjectOwner


class ProjectViewset(ModelViewSet):
    queryset = Project.objects.filter()
    serializer_class = ProjectListSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = Project.objects.filter(Q(author_user=request.user) |
                                          Q(contributors__user=request.user)).distinct()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Project.objects.filter()
        project = get_object_or_404(queryset, pk=pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)


class ContributorsViewset(ModelViewSet):
    serializer_class = ContributorsSerializer
    queryset = Contributor.objects.filter()
    permission_classes = [IsAuthenticated & IsProjectOwner]

    def list(self, request, project_pk=None):
        queryset = Contributor.objects.filter(project=project_pk)
        serializer = ContributorsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Contributor.objects.filter(pk=pk, project=project_pk)
        contributor = get_object_or_404(queryset, pk=pk)
        serializer = ContributorsSerializer(contributor)
        return Response(serializer.data)

    def create(self, request, project_pk=None, *args, **kwargs):
        data = request.data
        contributor = Contributor.objects.create(user_id=data['user'],
                                                 project_id=project_pk,
                                                 permission=data['permission'],
                                                 role=data['role'])
        contributor.save()
        serializer = ContributorsSerializer(contributor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class IssuesViewset(ModelViewSet):

    serializer_class = IssuesSerializer
    queryset = Issue.objects.filter()
    permission_classes = [IsAuthenticated & IsContributor]

    def list(self, request, project_pk=None):
        queryset = Issue.objects.filter(project=project_pk)
        serializer = IssuesSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None):
        queryset = Issue.objects.filter(pk=pk, project=project_pk)
        issue = get_object_or_404(queryset, pk=pk)
        serializer = IssuesSerializer(issue)
        return Response(serializer.data)

    def create(self, request, project_pk=None, *args, **kwargs):
        data = request.data
        issue = Issue.objects.create(title=data['title'],
                                     description=data['description'],
                                     tag=data['tag'],
                                     priority=data['priority'],
                                     project_id=project_pk,
                                     status=data['status'],
                                     author_user_id=data['author_user'],
                                     assignee_user_id=data['assignee_user'])
        issue.save()
        serializer = IssuesSerializer(issue)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        try:
            serializer.save(author_user=self.request.user)
        except:
            serializer.save(user=self.request.user)


class CommentsViewset(ModelViewSet):

    queryset = Comment.objects.filter()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated & IsContributor]

    def list(self, request, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(issue__project=project_pk, issue=issue_pk)
        serializer = CommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, project_pk=None, issue_pk=None):
        queryset = Comment.objects.filter(pk=pk, issue__project=project_pk, issue=issue_pk)
        maildrop = get_object_or_404(queryset, pk=pk)
        serializer = CommentsSerializer(maildrop)
        return Response(serializer.data)

    def create(self, request, issue_pk=None, *args, **kwargs):
        data = request.data
        comment = Comment.objects.create(description=data['description'],
                                         author_user_id=data['author_user'],
                                         issue_id=issue_pk,)
        comment.save()
        serializer = CommentsSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        try:
            serializer.save(author_user=self.request.user)
        except:
            serializer.save(user=self.request.user)
