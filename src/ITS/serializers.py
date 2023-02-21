from rest_framework.serializers import ModelSerializer
from models import Comments, Contributors, Issues, Project


class CommentsSerializer(ModelSerializer):
    
    class Meta:
        model = Comments
        fields = ['id',
                  'description',
                  'author_user_id',
                  'issue_id',
                  'created_time'] 

class ContributorsSerializer(ModelSerializer):
    
    class Meta:
        model = Contributors
        fields = ['user_id',
                  'project_id',
                  'permission',
                  'role']

class IssuesSerializer(ModelSerializer):
    
    class Meta:
        model = Issues
        fields = ['id',
                  'description',
                  'tag',
                  'priority',
                  'project_id',
                  'status',
                  'author_user_id',
                  'assignee_us_id',
                  'created_time']
        
class ProjectSerializer(ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['id',
                  'title',
                  'description',
                  'project_type',
                  'author_user_id']
