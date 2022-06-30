"""View for Labels app."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from task_manager.labels.forms import CreateAndUpdateLabelForm
from task_manager.labels.models import Label


class LabelsListView(LoginRequiredMixin, generic.ListView):
    """Define view for labels list page."""

    model = Label
    template_name = 'labels/labels_list.html'
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        """Define the title text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Labels list')
        return context


class CreateLabelView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    """Define view for create label page."""

    model = Label
    form_class = CreateAndUpdateLabelForm
    template_name = 'form.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully created.')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create label')
        context['button'] = _('Create')
        return context


class UpdateLabelView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.UpdateView,
):
    """Define view for update label page."""

    model = Label
    form_class = CreateAndUpdateLabelForm
    template_name = 'form.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully updated.')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Update label')
        context['button'] = _('Update')
        return context


class DeleteLabelView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.DeleteView,
):
    """Define view for delete label page."""

    model = Label
    template_name = 'delete.html'
    success_url = reverse_lazy('labels:labels')
    success_message = _('Label successfully deleted.')

    def get_context_data(self, **kwargs):
        """Define the title text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete label')
        return context
