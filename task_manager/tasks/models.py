"""Define model for Tasks app."""
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from task_manager.statuses.models import Status

MAX_LENGTH = 50

User = get_user_model()


class Task(models.Model):
    """Model representing task."""

    name = models.CharField(max_length=MAX_LENGTH)
    description = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        auto_created=True,
        blank=False,
        db_column='author',
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        blank=False,
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=False,
        related_name='executor',
    )
    created_at = models.DateTimeField(
        _('creation date'),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    def __str__(self):
        """Represent model object."""
        return self.name
