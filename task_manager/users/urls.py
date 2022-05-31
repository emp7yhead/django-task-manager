"""task_manager URL routes."""
from django.urls import path

from task_manager.users import views

urlpatterns = [
    path(
        '',
        views.UserListView.as_view(),
        name='users',
    ),
    path(
        'create/',
        views.RegisterUserView.as_view(),
        name='registration',
    ),
    path(
        '<int:pk>/update',
        views.UpdateUserView.as_view(),
        name='update',
    ),
    path(
        '<int:pk>/delete/',
        views.DeleteUserView.as_view(),
        name='delete',
    ),
]
