from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Define custom User model."""

    def __str__(self):
        """Represent model object."""
        return self.get_full_name()
