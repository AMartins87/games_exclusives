from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    Creates home app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'


class ContactConfig(AppConfig):
    """
    Creates contact app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
