from django.forms import ModelForm

from task_manager.tasks.models import Task


class CreateAndUpdateTaskForm(ModelForm):
    """Form for creating and updating task."""

    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'label',
            'executor',
        )
