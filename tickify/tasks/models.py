from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from slugify import slugify
from django.urls import reverse

from tickify import settings


# Create your models here.
class Priority(models.IntegerChoices):
    DEFAULT = 0, "Звичайний"
    LOW = 1, "Низький"
    MEDIUM = 2, "Середній"
    HIGH = 3, "Високий"
    CRITICAL = 4, "Критичний"


class CompletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(completed=True)


class UncompletedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(completed=False)


class Task(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Опис')
    completed = models.BooleanField(
        choices=[(False, "Active"), (True, "Completed")],
        default=False,
        verbose_name='Статус'
    )
    priority = models.IntegerField(choices=Priority.choices, default=Priority.DEFAULT, verbose_name='Пріоритет')
    deadline = models.DateTimeField(blank=True, null=True, verbose_name='Дедлайн')
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks',
        verbose_name='Категорія',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Користувач'
    )
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None, blank=True, null=True, verbose_name='Фото')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    completed_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата завершення')

    objects = models.Manager()
    completed_obj = CompletedManager()
    uncompleted_obj = UncompletedManager()

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]

    def get_absolute_url(self):
        return reverse('tasks_detail', kwargs={'task_slug': self.slug})

    def clean(self):
        if self.category and hasattr(self, 'user') and self.user and self.category.user != self.user:
            raise ValidationError('Завдання не може бути в категорії другого користувача')


    def save(self, *args, **kwargs):
        if self.completed and not self.completed_at:
            from django.utils import timezone
            self.completed_at = timezone.now()
        elif not self.completed:
            self.completed_at = None

        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1
            while Task.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{num}'
                num += 1
            self.slug = slug


        super().save(*args, **kwargs)

    def is_completed(self):
        return self.completed


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва категорії')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Слаг')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name='Користувач',
    )

    class Meta:
        verbose_name = "Категорії"
        verbose_name_plural = "Категорії"
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{num}'
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)


class UploadFile(models.Model):
    file = models.FileField(upload_to='uploads')