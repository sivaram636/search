from django.db import models

# Create your models here.
class index(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField()
    
    
