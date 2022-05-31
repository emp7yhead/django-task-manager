from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterAndUpdateUserForm(UserCreationForm):
    """Form for creating and updating user."""

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'password1', 'password2',
        )
