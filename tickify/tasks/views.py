from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "tasks/home.html",)

def tasks_list(request):
    return render(request, "tasks/tasks_list.html",)

def tasks_detail(request, task_id):
    return HttpResponse(f"Детальна сторінка задачи з id = {task_id}.")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена.</h1>")



