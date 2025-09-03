from django.contrib import admin

from tasks.models import Task, Category

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'category', 'user', 'updated_at')
    list_display_links = ('id', 'title')
    list_editable = ('completed', 'category')
    list_per_page = 5

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')
    list_display_links = ('id', 'name')