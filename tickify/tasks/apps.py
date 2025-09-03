from django.apps import AppConfig


class TasksConfig(AppConfig):
    verbose_name = 'Tickify завдання'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
