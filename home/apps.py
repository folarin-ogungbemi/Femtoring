from django.apps import AppConfig
from django.utils.module_loading import import_module


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        import_module('home.signals')
