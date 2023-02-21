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
    project_type = models.CharField(choices=TYPE)
    author_user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

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
    tag = models.CharField(choices=TAG)
    priority = models.CharField(choices=PRIORITY)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')
    status = models.CharField(choices=STATUS)
    author_user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    assignee_us_id = models.ForeignKey('User', on_delete=models.CASCADE, default='User')
    created_time = models.DateTimeField(auto_now_add=True)
    
class Contributors(models.Model):
    
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
