from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from tasks.forms import AddTaskForm, UploadFileForm
from tasks.models import Task, Category, UploadFile

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


class HomeView(TemplateView):
    template_name = "tasks/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['title'] = 'Tickify'
        context['menu'] = menu
        context['categories'] = Category.objects.filter(user=user)
        return context

class TaskListView(ListView):
    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = 'tasks'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        user = self.request.user

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug, user=user)
            self.current_category = category
            return Task.objects.filter(user=user, category=category)
        else:
            self.current_category = None
            return Task.objects.filter(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context["title"] = "Tasks"
        context["categories"] = Category.objects.filter(user=user)
        context["current_category"] = self.current_category
        context["completed_tasks"] = self.get_queryset().filter(completed=True)
        context["uncompleted_tasks"] = self.get_queryset().filter(completed=False)
        return context



class TaskCategoryView(ListView):
    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = 'tasks'

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        user = self.request.user

        self.current_category = get_object_or_404(Category, slug=category_slug, user=user)

        return Task.objects.filter(user=user, category=self.current_category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        context['title'] = self.current_category.name
        context['categories'] = Category.objects.filter(user=user)
        context['current_category'] = self.current_category
        context['completed_tasks'] = self.get_queryset().filter(completed=True)
        context['uncompleted_tasks'] = self.get_queryset().filter(completed=False)
        return context

def tasks_detail(request, task_slug):
    task = get_object_or_404(Task, slug=task_slug)

    data = {
        'title': task.title,
        'task': task,
    }

    return render(request, "tasks/task_detail.html", context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена.</h1>")

def contact(request):

    return render(request, "tasks/contacts.html",)


class AddTaskView(View):
    def get(self, request):
        form = AddTaskForm(user=request.user)
        data = {
            'title': 'Add Task',
            'form': form,
        }
        return render(request, "tasks/add_task.html", context=data)

    def post(self, request):
        form = AddTaskForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks_list')

        data = {
            'title': 'Add Task',
            'form': form,
        }
        return render(request, "tasks/add_task.html", context=data)
