from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.forms import AddTaskForm, UploadFileForm, CreateCategoryForm
from tasks.models import Task, Category, UploadFile
from tasks.permisions import IsOwner
from tasks.serializers import TaskSerializer
from tasks.utils import DataMixin

from rest_framework import generics, viewsets


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'task_slug'
    permission_classes = (IsOwner,)

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    @action(methods=['get'], detail=False, url_path='category/(?P<user_id>[^/.]+)')
    def categories(self, request, user_id=None):
        categories = Category.objects.filter(user_id=user_id)
        return Response({'categories': [c.name for c in categories]})


class HomeView(DataMixin, TemplateView):
    template_name = "tasks/home.html"
    title_page = 'Home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        return self.get_mixin_context(context,
                                      categories=Category.objects.filter(user=user) if user.is_authenticated else None,)


class TaskListView(LoginRequiredMixin, DataMixin, ListView):
    model = Task
    template_name = "tasks/tasks_list.html"
    title_page = 'Tasks'

    paginate_by = 4

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
        tasks_qs = self.object_list

        return self.get_mixin_context(context,
                                      categories=Category.objects.filter(user=user),
                                      current_category=self.current_category,
                                      completed_tasks=tasks_qs.filter(completed=True),
                                      uncompleted_tasks=tasks_qs.filter(completed=False),
                                      tasks = context['page_obj']
                                      )


class TaskDetailView(DataMixin, DetailView):
    model = Task
    template_name = "tasks/task_detail.html"
    slug_url_kwarg = "task_slug"
    context_object_name = "task"
    title_page = "Завдання"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title= self.object.title.capitalize() if self.object.title else "Завдання")


class PageNotFoundView(TemplateView):
    template_name = "tasks/404.html"


class ContactsView(TemplateView):
    template_name = "tasks/contacts.html"


class AddTaskView(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTaskForm
    template_name = "tasks/add_task.html"
    success_url = reverse_lazy('tasks_list')
    title_page = 'Додавання завдання'
    # permission_required = 'tasks.add_task'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CreateCategoryView(LoginRequiredMixin, DataMixin, CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = "tasks/create_category.html"
    success_url = reverse_lazy('tasks_list')
    title_page = 'Створення категорії'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




class EditTaskView(DataMixin, UpdateView):
    model = Task
    form_class = AddTaskForm
    template_name = "tasks/add_task.html"
    slug_url_kwarg = "task_slug"
    title_page = "Редагування завдання"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class DeleteTaskView(DataMixin, DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy('tasks_list')
    slug_url_kwarg = "task_slug"
    title_page = "Видалення завдання"