"""Views for task manager users."""
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from task_manager.users.forms import RegisterAndUpdateUserForm
from task_manager.users.mixins import UserCheckMixin

User = get_user_model()


class UserListView(generic.ListView):
    """Define view for users list page."""

    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"
    extra_context = {"title": _("Users list")}


class RegisterUserView(SuccessMessageMixin, generic.CreateView):
    """Define view for registration page."""

    form_class = RegisterAndUpdateUserForm
    template_name = "users/create_and_update.html"
    success_url = reverse_lazy("login")
    extra_context = {"title": _("Register user")}
    success_message = _("Successfully registered user.")


class UpdateUserView(SuccessMessageMixin, UserCheckMixin, generic.UpdateView):
    """Define view for update user page."""

    model = User
    form_class = RegisterAndUpdateUserForm
    template_name = "users/create_and_update.html"
    success_url = reverse_lazy("users:users")
    extra_context = {"title": _("Update user")}
    success_message = _("Successfully updated user.")


class DeleteUserView(UserCheckMixin, generic.DeleteView):
    """Define view for delete user page."""

    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("users:users")
    extra_context = {"title": _("Delete user")}

    def form_valid(self, form):
        """Check if user has assigned task."""
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                self.request,
                _('User has assigned task'),
            )
        else:
            messages.success(
                self.request,
                _("Successfully deleted user."),
            )
        return HttpResponseRedirect(self.success_url)
