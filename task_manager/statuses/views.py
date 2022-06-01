"""View for Statuses app."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from .forms import CreateAndUpdateStatusForm
from .models import Status


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
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully deleted.')
    extra_context = {'title': _('Delete status')}

    def delete(self, request, *args, **kwargs):
        """Delete object except status is currently used by task."""
        status = self.get_object()
        if status.chidlren.count() > 0:
            messages.add_message(
                request,
                messages.ERROR,
                _("Can't be deleted, has assigned task."),
            )
            return redirect(self.get_success_url())

        return super().delete(request, *args, **kwargs)
