from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
tasks_db = [
    {'id': 1, 'title': 'Завдання 1', 'description': 'Опис завдання 1', 'is_done': False},
    {'id': 2, 'title': 'Завдання 2', 'description': 'Опис завдання 2', 'is_done': True},
    {'id': 3, 'title': 'Завдання 3', 'description': 'Опис завдання 3', 'is_done': False},
    {'id': 4, 'title': 'Завдання 4', 'description': 'Опис завдання 4', 'is_done': True},
]

menu = [{'title': 'Home', 'url': 'home'},
        {'title': 'Tasks', 'url': 'tasks_list'},
        {'title': 'Add Task', 'url': 'add_task'},
        {'title': 'Contact', 'url': 'contact'},
        {'title': 'Login', 'url': 'login'},
        {'title': 'Register', 'url': 'register'}
]

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return redirect('home')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')

def home(request):
    data = {
        'title': 'Tickify',
        'menu': menu,
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

def contact(request):
    return HttpResponse("Контактові дані.")

def add_task(request):
    return render(request, "tasks/add_task.html")



