from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('tasks/<int:task_id>/', views.tasks_detail, name='tasks_detail'),

]