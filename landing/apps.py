from django.apps import AppConfig


class LandingConfig(AppConfig):
    """
    Provides primary key type for landing app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landing'
