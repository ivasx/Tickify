from django.conf.urls.static import static
from django.urls import path, include

from tickify import settings
from . import views
from .views import TaskViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

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

    path('api/v1/', include(router.urls)),
    # path('api/v1/tasklist/', TaskViewSet.as_view({'get': 'list'})),
    # path('api/v1/tasklist/<slug:task_slug>/', TaskViewSet.as_view({'put': 'update'})),
    # path('api/v1/taskdetail/<slug:task_slug>/', TaskViewSet.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)