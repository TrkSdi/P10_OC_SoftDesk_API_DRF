from rest_framework.serializers import ModelSerializer
from ITS.models import Comment, Contributor, Issue, Project


class CommentsSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'issue_pk': 'issue__pk',
        'project_pk': 'issue__project__pk',
    }

    class Meta:
        model = Comment
        fields = ['id',
                  'description',
                  'author_user',
                  'created_time']
        read_only_fields = ['author_user']


class ContributorsSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'project_pk': 'project__pk',
    }

    class Meta:
        model = Contributor
        fields = ['id',
                  'user',
                  'permission',
                  'role']


class IssuesSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'project_pk': 'project__pk',
    }
 
    class Meta:
        model = Issue
        fields = ['id',
                  'title',
                  'description',
                  'tag',
                  'priority',
                  'status',
                  'assignee_user',
                  'created_time', ]
        
        read_only_fields = [
                  'author_user',]


class ProjectDetailSerializer(ModelSerializer):

    issue = IssuesSerializer(many=True, read_only=True)
    contributor = ContributorsSerializer(many=True, read_only=True)


    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'project_type',
                  'author_user',
                  'issue',
                  'contributor'
                  ]


class ProjectListSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'project_type',
                  'author_user']
        read_only_fields = ['author_user']
