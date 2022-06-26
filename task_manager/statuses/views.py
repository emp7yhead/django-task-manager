"""View for Statuses app."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
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

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Statuses list')
        return context  


class CreateStatusView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    """Define view for create status page."""

    model = Status
    form_class = CreateAndUpdateStatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully created.')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create status')
        context['button'] = _('Create')
        return context


class UpdateStatusView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.UpdateView,
):
    """Define view for update status page."""

    model = Status
    form_class = CreateAndUpdateStatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('statuses:statuses')
    success_message = _('Status successfully updated.')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Update status')
        context['button'] = _('Update')
        return context


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

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete status')
        return context
