"""Views for task manager."""
from django.shortcuts import render
from django.views import View


class IndexView(View):
    """Define view for index page."""

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        """Render index page.

        Args:
            request: request for page.

        Returns:
            HttpResponse.
        """
        return render(self.request, self.template_name)
