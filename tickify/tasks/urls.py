from django.conf.urls.static import static
from django.urls import path

from tickify import settings
from . import views
from .views import TaskAPIView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('tasks/', views.TaskListView.as_view(), name='tasks_list'),
    path('tasks/category/<slug:category_slug>/', views.TaskListView.as_view(),name='category'),
    path('tasks/<slug:task_slug>/', views.TaskDetailView.as_view(), name='tasks_detail'),
    path('contact/', views.ContactsView.as_view(), name='contact'),
    path('add_task/', views.AddTaskView.as_view(), name='add_task'),
    path('edit_task/<slug:task_slug>/', views.EditTaskView.as_view(), name='edit_task'),
    path('delete_task/<slug:task_slug>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('create_category/', views.CreateCategoryView.as_view(), name='create_category'),

    path('api/v1/tasklist/', TaskAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)