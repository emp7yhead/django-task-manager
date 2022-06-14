from django import template

register = template.Library()


@register.filter
def get_verbose_name(model):
    """Return model verbose name."""
    return model._meta.verbose_name
