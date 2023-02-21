from django.db import models

# Create your models here.

class Project(models.Model):
    TYPE = [
        ('back-end', 'back-end'),
        ('front-end', 'front-end'),
        ('iOS', 'iOS'),
        ('Android', 'Android')
    ]
    
    project_id = models.IntegerField()
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=800)
    project_type = models.CharField(max_length=50, choices=TYPE)
    author_user_id = models.ForeignKey('User', on_delete=models.CASCADE)
