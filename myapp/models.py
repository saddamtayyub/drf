from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    
