from django.conf import settings
from django.db import models


# Create your models here.

class Project(models.Model):
    TYPE = [
        ('back-end', 'back-end'),
        ('front-end', 'front-end'),
        ('iOS', 'iOS'),
        ('Android', 'Android')
    ]
    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    project_type = models.CharField(max_length=50, choices=TYPE)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.title

class Contributors(models.Model):
    # Revoir permission, role
    PERMISSION = [
        ('USER', 'USER'),
        ('SUPERUSER', 'SUPERUSER')
    ]
    
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE, null=True, blank=True)
    permission = models.CharField(max_length=20, choices=PERMISSION, default='USER')
    role = models.CharField(max_length=20)

class Issues(models.Model):
    TAG = [
        ('BUG', 'BUG'),
        ('AMELIORATION', 'AMELIORATION'),
        ('TACHE', 'TACHE')
    ]
    
    PRIORITY = [
        ('FAIBLE', 'FAIBLE'),
        ('MOYENNE', 'MOYENNE'),
        ('ELEVEE', 'ELEVEE'),
    ]
    
    STATUS = [
        ('A faire', 'A faire'),
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé'),
    ] 
    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    tag = models.CharField(max_length=50, choices=TAG)
    priority = models.CharField(max_length=50, choices=PRIORITY)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, default=None)
    status = models.CharField(max_length=50, choices=STATUS)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author', null=True, blank=True, default=None)
    assignee_us_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignee', null=True, blank=True, default=None)
    created_time = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    
    description = models.CharField(max_length=800)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE, null=True, blank=True, default=None)
    created_time = models.DateTimeField(auto_now_add=True)
    