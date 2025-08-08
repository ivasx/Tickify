from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    