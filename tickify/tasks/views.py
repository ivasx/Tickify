from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
tasks_db = [
    {'id': 1, 'title': 'Завдання 1', 'description': 'Опис завдання 1', 'is_done': False},
    {'id': 2, 'title': 'Завдання 2', 'description': 'Опис завдання 2', 'is_done': True},
    {'id': 3, 'title': 'Завдання 3', 'description': 'Опис завдання 3', 'is_done': False},
    {'id': 4, 'title': 'Завдання 4', 'description': 'Опис завдання 4', 'is_done': True},
]

def home(request):
    data = {
        'title': 'Tickify',
        'menu': ['Home', 'Tasks', 'Add Task']
    }

    return render(request, "tasks/home.html", context=data)

def tasks_list(request):
    data = {
        'title': 'Tasks',
        'tasks': tasks_db,
    }
    return render(request, "tasks/tasks_list.html", context=data)

def tasks_detail(request, task_id):
    return HttpResponse(f"Детальна сторінка задачи з id = {task_id}.")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена.</h1>")



