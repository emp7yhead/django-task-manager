"""View for Tasks app."""
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import generic

from task_manager.tasks.forms import CreateAndUpdateTaskForm
from task_manager.tasks.models import Task


class TasksListView(LoginRequiredMixin, generic.ListView):
    """Define view for tasks list page."""

    model = Task
    template_name = 'tasks/tasks_list.html'
    context_object_name = 'tasks'
    extra_context = {'title': _('Tasks list')}

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Tasks list')
        return context


class CreateTaskView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    """Define view for create task page."""

    model = Task
    form_class = CreateAndUpdateTaskForm
    template_name = 'form.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task successfully created.')

    def form_valid(self, form):
        """Save the associated model adding current user as author."""
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Create task')
        context['button'] = _('Create')
        return context


class UpdateTaskView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.UpdateView,
):
    """Define view for update task page."""

    model = Task
    form_class = CreateAndUpdateTaskForm
    template_name = 'form.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task successfully updated.')

    def get_context_data(self, **kwargs):
        """Define the title and button text."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Update task')
        context['button'] = _('Update')
        return context


class DetailedTaskView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.DetailView,
):
    """Define view for detail task page."""

    model = Task
    template_name = 'tasks/task_detail.html'


class DeleteTaskView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.DeleteView,
):
    """Define view for delete task page."""

    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks:tasks')
    success_message = _('Task successfully deleted.')

    def form_valid(self, form):
        """Check if the current user is a task creator."""
        task_author = self.get_object().author
        if task_author == self.request.user:
            super().form_valid(form)
        else:
            messages.error(
                self.request,
                _('Task can be deleted only by author.'),
            )
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        """Define the title."""
        context = super().get_context_data(**kwargs)
        context['title'] = _('Delete task')
        return context
