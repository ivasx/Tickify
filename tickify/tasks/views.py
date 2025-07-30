from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Головна сторінка.")

def tasks_list(request):
    return HttpResponse("Список задач.")

def tasks_detail(request, task_id):
    return HttpResponse(f"Детальна сторінка задачи з id = {task_id}.")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сторінка не знайдена.</h1>")



