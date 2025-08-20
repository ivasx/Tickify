from django import template
import tasks.views as views

register = template.Library()

@register.simple_tag
def get_task_list():
    return views.tasks_db


@register.inclusion_tag('tasks/tasks_list.html')
def show_tasks():
    tasks = views.tasks_db
    return {'tasks': tasks}