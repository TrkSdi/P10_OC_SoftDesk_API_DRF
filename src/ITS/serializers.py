from rest_framework.serializers import ModelSerializer
from ITS.models import Comments, Contributors, Issues, Project


class CommentsSerializer(ModelSerializer):
    
    class Meta:
        model = Comments
        fields = ['id',
                  'description',
                  'author_user',
                  'issue',
                  'created_time'] 

class ContributorsSerializer(ModelSerializer):
    
    class Meta:
        model = Contributors
        fields = ['id',
                  'user',
                  'project',
                  'permission',
                  'role']

class IssuesSerializer(ModelSerializer):
    
    class Meta:
        model = Issues
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
        
class ProjectSerializer(ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'project_type',
                  'author_user']
