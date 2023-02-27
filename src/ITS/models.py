from django.conf import settings
from django.db import models



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
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.title

class Contributor(models.Model):
    # Revoir permission, role
    PERMISSION = [
        ('USER', 'USER'),
        ('SUPERUSER', 'SUPERUSER')
    ]
    
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, null=True, blank=True, related_name='contributor')
    permission = models.CharField(max_length=20, choices=PERMISSION, default='USER')
    role = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Contributor: {self.user}"

class Issue(models.Model):
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
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='issue')
    status = models.CharField(max_length=50, choices=STATUS)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author', null=True, blank=True, default=None)
    assignee_us = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignee', null=True, blank=True, default=None)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    
    description = models.CharField(max_length=800)
    author_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True, default=None)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, null=True, blank=True, default=None)
    created_time = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Author: {self.author_user}"