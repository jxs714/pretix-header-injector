from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PretixPluginMeta:
    name = _('Header Code Injector')
    author = _('Your Name')
    version = '1.0.1'
    description = _('This plugin allows you to inject custom code (e.g., Google Analytics, Meta Pixel) into the HTML head of your event pages.')
    category = 'CUSTOMIZATION'
    visible = True
    featured = False

class HeaderInjectorApp(AppConfig):
    name = 'pretix_header_injector'
    verbose_name = 'Header Code Injector'

    def ready(self):
        from . import signals  # NOQA

default_app_config = 'pretix_header_injector.HeaderInjectorApp'