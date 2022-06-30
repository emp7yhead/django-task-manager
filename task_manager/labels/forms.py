from django.forms import ModelForm

from task_manager.labels.models import Label


class CreateAndUpdateLabelForm(ModelForm):
    """Form for creating and updating label."""

    class Meta:
        model = Label
        fields = ('name',)
