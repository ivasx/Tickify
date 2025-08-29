from django import template
import tasks.views as views
from tasks.models import Category

register = template.Library()

@register.simple_tag
def get_task_list():
    return views.tasks_db


@register.inclusion_tag('tasks/tasks_list.html')
def show_tasks():
    tasks = views.tasks_db
    return {'tasks': tasks}

@register.simple_tag
def get_tasks_count(category):
    count_tasks = category.tasks.filter(completed=0).count()
    return count_tasks