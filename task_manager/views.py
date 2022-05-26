"""Views for task manager."""
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.models import User

from task_manager.forms import RegisterUserForm


class IndexView(TemplateView):
    """Define view for index page."""

    template_name = 'index.html'


class UserListView(ListView):
    """Define view for users list page."""

    model = User
    template_name = 'users.html'
    context_object_name = 'users'


class RegisterUserView(CreateView):
    """Define view for registration page."""

    form_class = RegisterUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
