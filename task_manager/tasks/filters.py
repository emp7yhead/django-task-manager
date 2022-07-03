"""Filters for task app."""
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django_filters import BooleanFilter, ChoiceFilter, FilterSet

from task_manager.labels.models import Label
from task_manager.tasks.models import Task

User = get_user_model()


class TaskFilter(FilterSet):
    """Define filers for tasks list."""

    labels_query = Label.objects.values_list('id', 'name')
    labels = ChoiceFilter(label=_('Label'), choices=labels_query)

    self_tasks = BooleanFilter(
        label=_('Current user tasks'),
        widget=forms.CheckboxInput(),
        method='get_self_tasks',
    )

    def get_self_tasks(self, queryset, name, value):
        """Filter current user tasks."""
        if value:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    class Meta:
        model = Task
        fields = [
            'status',
            'executor',
            'labels',
        ]
