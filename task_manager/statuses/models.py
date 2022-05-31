from django.db import models
from django.utils.translation import gettext as _

MAX_LENGTH = 40


class Status(models.Model):
    """Model representing statuses."""

    name = models.CharField(_('name'), max_length=MAX_LENGTH)
    created_at = models.DateTimeField(_('creation date'), auto_now_add=True)

    class Meta:
        verbose_name = _('status')
        verbose_name_plural = _('statuses')

    def __str__(self):
        """Represent model object."""
        return self.name
