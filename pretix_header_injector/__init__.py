from django.utils.translation import gettext_lazy as _

class PretixPluginMeta:
    name = _('Header Injector')
    author = 'Your Name'
    description = _('Inject custom code into headers')
    visible = True
    version = '1.0.0'

default_app_config = 'pretix_header_injector.PluginApp'

from django.apps import AppConfig

class PluginApp(AppConfig):
    name = 'pretix_header_injector'
    verbose_name = 'Header Injector'

    def ready(self):
        from . import signals
