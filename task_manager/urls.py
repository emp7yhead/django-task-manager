"""task_manager URL routes."""

from django.contrib import admin
from django.urls import path

from task_manager import views

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        '',
        views.IndexView.as_view(),
        name='index',
    ),
    path(
        'users/',
        views.UserListView.as_view(),
        name='users',
    ),
    path(
        'users/create/',
        views.RegisterUserView.as_view(),
        name='registration',
    ),
    path(
        'users/<int:pk>/update',
        views.UpdateUserView.as_view(),
        name='update',
    ),
    path(
        'users/<int:pk>/delete/',
        views.DeleteUserView.as_view(),
        name='delete',
    ),
    path(
        'login/',
        views.LoginUserView.as_view(),
        name='login',
    ),
    path(
        'logout',
        views.LogoutUserView.as_view(),
        name='logout',
    ),
]
