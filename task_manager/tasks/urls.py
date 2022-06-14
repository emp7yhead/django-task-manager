"""task_manager.tasks URL routes."""
from django.urls import path

from task_manager.tasks import views

app_name = 'tasks'
urlpatterns = [
    path(
        '',
        views.TasksListView.as_view(),
        name='tasks',
    ),
    path(
        'create/',
        views.CreateTaskView.as_view(),
        name='create',
    ),
    path(
        '<int:pk>/update',
        views.UpdateTaskView.as_view(),
        name='update',
    ),
    path(
        '<int:pk>/delete/',
        views.DeleteTaskView.as_view(),
        name='delete',
    ),
    path(
        '<int:pk>/',
        views.DetailedTaskView.as_view(),
        name='detail',
    ),
]
