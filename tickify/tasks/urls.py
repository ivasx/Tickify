from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks_list, name='tasks_list'),
    path('tasks/category/<slug:category_slug>/', views.tasks_list, name='category'),
    path('tasks/<slug:task_slug>/', views.tasks_detail, name='tasks_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('add_task/', views.add_task, name='add_task'),

]