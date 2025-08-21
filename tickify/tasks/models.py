from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from tickify import settings


# Create your models here.

class Priority(models.IntegerChoices):
    DEFAULT = 0, "Default"
    LOW = 1, "Low"
    MEDIUM = 2, "Medium"
    HIGH = 3, "High"
    CRITICAL = 4, "Critical"

class CompletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(completed=Task.Status.COMPLETED)

class UncompletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(completed=Task.Status.ACTIVE)

class Task(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 0, "Active"
        COMPLETED = 1, "Completed"

    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(choices=Status.choices, default=Status.ACTIVE)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.DEFAULT)
    deadline = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    completed_obj= CompletedManager()
    uncompleted_obj = UncompletedManager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]

    def get_absolute_url(self):
        return reverse('tasks_detail', kwargs={'task_slug': self.slug})


class User(AbstractUser):
    pass