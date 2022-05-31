"""Views for task manager users."""
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from task_manager.users.forms import RegisterAndUpdateUserForm
from task_manager.users.mixins import UserCheckMixin


class UserListView(generic.ListView):
    """Define view for users list page."""

    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"
    extra_context = {"title": _("Users list")}


class RegisterUserView(SuccessMessageMixin, generic.CreateView):
    """Define view for registration page."""

    form_class = RegisterAndUpdateUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")
    extra_context = {"title": _("Register user")}
    success_message = _("Successfully registered user.")


class UpdateUserView(SuccessMessageMixin, UserCheckMixin, generic.UpdateView):
    """Define view for update user page."""

    model = User
    form_class = RegisterAndUpdateUserForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users")
    extra_context = {"title": _("Update user")}
    success_message = _("Successfully updated user.")


class DeleteUserView(UserCheckMixin, generic.DeleteView):
    """Define view for delete user page."""

    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users")
    extra_context = {"title": _("Delete user")}
    success_message = _("Successfully deleted user.")
