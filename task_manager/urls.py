"""task_manager URL Configuration."""

from django.contrib import admin
from django.urls import path

from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('users/create/', views.RegisterUserView.as_view(), name='sign_up'),
    # path('/users/<int:pk>/update/', views, name='update'),
    # path('/users/<int:pk>/delete/', views, name='delete'),
    # path('login/', views, name='login')
]
