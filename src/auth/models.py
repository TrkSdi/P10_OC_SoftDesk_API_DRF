from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=30, null=True, blank=True, unique=True)
    
    def __str__(self):
        if self.first_name == "":
            return self.username
        return self.first_name