from django.forms import ModelForm

from task_manager.statuses.models import Status


class CreateAndUpdateStatusForm(ModelForm):
    """Form for creating and updating status."""

    class Meta:
        model = Status
        fields = ('name',)
