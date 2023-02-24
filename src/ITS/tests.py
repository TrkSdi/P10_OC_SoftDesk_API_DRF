from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from .models import Project, Issues, Contributors, Comments

class TestProject(APITestCase):
    
    url = reverse_lazy('project-list')

    def test_list(self):
    
        project = Project.objects.create(title='project_01')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'id': project.id,
                'title': project.title,
                'description': project.description,
                'project_type': project.project_type,
                'author_user': project.author_user
            }
        ]
        self.assertEqual(excepted, response.json())

    def test_create(self):

        self.assertFalse(Project.objects.exists())
        response = self.client.post(self.url, data={'title': 'New Project'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(Project.objects.exists())
        
class TestIssues(APITestCase):
    url = reverse_lazy('issues-list')
    
    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        # Create an issue
        issues = Issues.objects.create(title='issue_01')
        
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'id': issues.pk,
                'title': issues.title,
                'description': issues.description,
                'tag': issues.tag,
                'priority': issues.priority,
                'project': issues.project,
                'status': issues.status,
                'author_user': issues.author_user,
                'assignee_us': issues.assignee_us,
                'created_time': self.format_datetime(issues.created_time)
            }
        ]
        self.assertEqual(excepted, response.json())

    def test_create(self):
        
        self.assertFalse(Issues.objects.exists())
        response = self.client.post(self.url, data={'title': 'New issue'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(Issues.objects.exists())

class TestContributors(APITestCase):
    url = reverse_lazy('contributors-list')

    def test_list(self):
        
        contributors = Contributors.objects.create()
        
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'id': contributors.id,
                'user': contributors.user,
                'project': contributors.project,
                'permission': contributors.permission,
                'role': contributors.role,

            }
        ]
        self.assertEqual(excepted, response.json())

    def test_create(self):
        
        self.assertFalse(Contributors.objects.exists())
        response = self.client.post(self.url, data={'role': 'New role'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(Contributors.objects.exists())
    
class TestComments(APITestCase):
    url = reverse_lazy('comments-list')
    
    def format_datetime(self, value):
        return value.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    def test_list(self):
        
        comments = Comments.objects.create(description='comments_01')
        
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        excepted = [
            {
                'id': comments.id,
                'description': comments.description,
                'author_user': comments.author_user,
                'issue': comments.issue,
                'created_time': self.format_datetime(comments.created_time),

            }
        ]
        self.assertEqual(excepted, response.json())

    def test_create(self):
        
        self.assertFalse(Comments.objects.exists())
        response = self.client.post(self.url, data={'description': 'new comment'})
        self.assertEqual(response.status_code, 405)
        self.assertFalse(Comments.objects.exists())