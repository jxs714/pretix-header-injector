from django.apps import AppConfig

class PluginApp(AppConfig):
    name = 'pretix_header_injector'
    verbose_name = 'Pretix Header Injector'

    def ready(self):
        # Import signals if you have any
        try:
            from . import signals
        except ImportError:
            pass
