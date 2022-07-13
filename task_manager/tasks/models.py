"""Define model for Tasks app."""
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status

MAX_LENGTH = 50

User = get_user_model()


class Task(models.Model):
    """Model representing task."""

    name = models.CharField(
        _('name'),
        max_length=MAX_LENGTH,
    )
    description = models.TextField(_('Description'))
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
        related_name='status',
        verbose_name=_('status'),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        blank=True,
        related_name='executor',
        verbose_name=_('Executor'),
    )
    created_at = models.DateTimeField(
        _('creation date'),
        auto_now_add=True,
    )
    labels = models.ManyToManyField(
        Label,
        verbose_name=_('labels'),
        blank=True,
    )

    class Meta:
        verbose_name = _('task')
        verbose_name_plural = _('tasks')

    def __str__(self):
        """Represent model object."""
        return self.name
