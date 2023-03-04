from rest_framework.serializers import ModelSerializer
from ITS.models import Comment, Contributor, Issue, Project


class CommentsSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'project_pk': 'project_pk',
        'issue_pk': 'issue__project_pk',
    }
    
    class Meta:
        model = Comment
        fields = ['id',
                  'description',
                  'author_user',
                  'issue',
                  'created_time'] 

class ContributorsSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'project_pk': 'project_pk',
    }
    
    class Meta:
        model = Contributor
        fields = ['id',
                  'user',
                  'permission',
                  'role']

class IssuesSerializer(ModelSerializer):
    parent_lookup_kwargs = {
        'project_pk': 'project_pk',
    }
    
    class Meta:
        model = Issue
        fields = ['id',
                  'title',
                  'description',
                  'tag',
                  'priority',
                  'project',
                  'status',
                  'author_user',
                  'assignee_us',
                  'created_time',
                  'comment']
        
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