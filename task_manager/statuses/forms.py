from django.forms import ModelForm

from .models import Status


class CreateAndUpdateStatusForm(ModelForm):
    """Form for creating and updating status."""

    class Meta:
        model = Status
        fields = ('name',)
