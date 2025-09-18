from django.conf.urls.static import static
from django.urls import path

from tickify import settings
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tasks/', views.TaskListView.as_view(), name='tasks_list'),
    path('tasks/category/<slug:category_slug>/', views.TaskCategoryView.as_view(),name='category'),
    path('tasks/<slug:task_slug>/', views.tasks_detail, name='tasks_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('add_task/', views.AddTaskView.as_view(), name='add_task'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)