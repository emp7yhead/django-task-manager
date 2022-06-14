"""View for Statuses app."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from task_manager.statuses.forms import CreateAndUpdateStatusForm
from task_manager.statuses.models import Status


class StatusesListView(LoginRequiredMixin, generic.ListView):
    """Define view for statuses list page."""

    model = Status
    template_name = 'statuses/statuses_list.html'
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses list')}


class CreateStatusView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    """Define view for create status page."""

    model = Status
    form_class = CreateAndUpdateStatusForm
    template_name = 'statuses/create_and_update.html'
    success_url = reverse_lazy('statuses:statuses')
    extra_context = {'title': _('Create status')}
    success_message = _('Status successfully created.')


class UpdateStatusView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.UpdateView,
):
    """Define view for update status page."""

    model = Status
    form_class = CreateAndUpdateStatusForm
    template_name = 'statuses/create_and_update.html'
    success_url = reverse_lazy('statuses:statuses')
    extra_context = {'title': _('Update status')}
    success_message = _('Status successfully updated.')


class DeleteStatusView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.DeleteView,
):
    """Define view for delete status page."""

    model = Status
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully deleted.')
    extra_context = {'title': _('Delete status')}

    def form_valid(self, form):
        """Check if status is used by task."""
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(
                self.request,
                _('Status is used by task'),
            )
        else:
            messages.success(
                self.request,
                _("Successfully deleted status."),
            )
        return HttpResponseRedirect(self.success_url)
