from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from tasks.models import Task, Category

# Create your views here.
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
    categories = Category.objects.filter(user=request.user)
    data = {
        'title': 'Tickify',
        'menu': menu,
        'categories': categories
    }

    return render(request, "tasks/home.html", context=data)

def tasks_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        completed_tasks = Task.completed_obj.filter(user=request.user)
        uncompleted_tasks = Task.uncompleted_obj.filter(user=request.user)
        categories = Category.objects.filter(user=request.user)
        data = {
            'title': 'Tasks',
            'completed_tasks': completed_tasks,
            'uncompleted_tasks': uncompleted_tasks,
            'categories': categories,
        }
        return render(request, "tasks/tasks_list.html", context=data)

def tasks_detail(request, task_slug):
    task = get_object_or_404(Task,slug=task_slug)

    data = {
        'title': task.title,
        'task': task,
    }

    return render(request, "tasks/task_detail.html", context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена.</h1>")

def contact(request):
    return render(request, "tasks/contacts.html")

def add_task(request):
    return render(request, "tasks/add_task.html", context={'title': 'Add Task'})


def show_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    completed_tasks = Task.completed_obj.filter(category=category)
    uncompleted_tasks = Task.uncompleted_obj.filter(category=category)
    categories = Category.objects.all()
    data = {
        'title': category.name,
        'completed_tasks': completed_tasks,
        'uncompleted_tasks': uncompleted_tasks,
        'categories': categories,
        'current_category': category,
    }
    return render(request, "tasks/tasks_list.html", context=data)
