"""Define model for Labels app."""

from django.db import models
from django.utils.translation import gettext as _

MAX_LENGTH = 50


class Label(models.Model):
    """Model representing label."""

    name = models.CharField(
        max_length=MAX_LENGTH,
        blank=False,
    )
    created_at = models.DateTimeField(
        _('creation date'),
        auto_now_add=True,
    )

    class Meta:
        verbose_name = _('label')
        verbose_name_plural = _('labels')

    def __str__(self):
        """Represent model object."""
        return self.name
