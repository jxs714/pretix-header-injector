from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class HeaderInjectorApp(AppConfig):
    name = 'pretix_header_injector'
    verbose_name = 'Header Code Injector'

    class PretixPluginMeta:
        name = _('Header Code Injector')
        author = 'Your Name'
        version = '1.0.0'
        description = _('Injects custom code into the HTML head of event pages.')
        visible = True
        category = 'CUSTOMIZATION'
        featured = False

    def ready(self):
        from . import signals  # NOQA

default_app_config = 'pretix_header_injector.HeaderInjectorApp'