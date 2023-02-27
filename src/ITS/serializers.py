from rest_framework.serializers import ModelSerializer
from ITS.models import Comment, Contributor, Issue, Project


class CommentsSerializer(ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['id',
                  'description',
                  'author_user',
                  'issue',
                  'created_time'] 

class ContributorsSerializer(ModelSerializer):
    
    class Meta:
        model = Contributor
        fields = ['id',
                  'user',
                  'project',
                  'permission',
                  'role']

class IssuesSerializer(ModelSerializer):
    
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
                  'created_time']
        
class ProjectDetailSerializer(ModelSerializer):
    
    issue = IssuesSerializer(many=True)
    contributor = ContributorsSerializer(many=True)
    
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