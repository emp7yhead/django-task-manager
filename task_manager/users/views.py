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
    template_name = 'users/users_list.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        """Define the title."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Users list')
        return context


class RegisterUserView(SuccessMessageMixin, generic.CreateView):
    """Define view for registration page."""

    form_class = RegisterAndUpdateUserForm
    template_name = 'form.html'
    success_url = reverse_lazy('login')
    success_message = _('Successfully registered user.')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Register user')
        context['button'] = _('Register')
        return context


class UpdateUserView(SuccessMessageMixin, UserCheckMixin, generic.UpdateView):
    """Define view for update user page."""

    model = User
    form_class = RegisterAndUpdateUserForm
    template_name = 'form.html'
    success_url = reverse_lazy('users:users')
    success_message = _('Successfully updated user.')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Update user')
        context['button'] = _('Update')
        return context


class DeleteUserView(UserCheckMixin, generic.DeleteView):
    """Define view for delete user page."""

    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("users:users")

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

    def get_context_data(self, **kwargs):
        """Define the title."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete user')
        return context
