"""Views for task manager."""
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from task_manager.forms import RegisterAndUpdateUserForm


class IndexView(TemplateView):
    """Define view for index page."""

    template_name = 'index.html'
    extra_context = {'title': _('Task Manager')}


class UserListView(ListView):
    """Define view for users list page."""

    model = User
    template_name = 'users.html'
    context_object_name = 'users'
    extra_context = {'title': _('Users list')}


class RegisterUserView(CreateView):
    """Define view for registration page."""

    form_class = RegisterAndUpdateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    extra_context = {'title': _('Register user')}


class UpdateUserView(UpdateView):
    """Define view for update user page."""

    model = User
    form_class = RegisterAndUpdateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
    extra_context = {'title': _('Update user')}


class DeleteUserView(DeleteView):
    """Define view for delete user page."""

    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('index')
    extra_context = {'title': _('Delete user')}


class LoginUserView(SuccessMessageMixin, LoginView):
    """Define view for login page."""

    template_name = 'registration/login.html'
    next_page = 'index'
    extra_context = {'title': _('Login')}


class LogoutUserView(LogoutView):
    """Define view for logout."""

    next_page = 'index'
