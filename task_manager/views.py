"""Views for task manager."""
from django.shortcuts import render


def index(request):
    """Render index page.

    Args:
        request: request for page.

    Returns:
        HttpResponse.
    """
    return render(request, 'index.html', context={
        'hello': 'Welcome to Task Manager!',
    })
