from django.apps import AppConfig


class TasksConfig(AppConfig):
    """Config for Statuses app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_manager.tasks'
