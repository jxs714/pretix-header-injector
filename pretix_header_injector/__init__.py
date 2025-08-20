from django.utils.translation import gettext_lazy as _
from pretix.base.plugins import PluginConfig

class HeaderInjectorApp(PluginConfig):
    name = 'pretix_header_injector'
    verbose_name = 'Header Code Injector'

    # All metadata is now directly part of this class
    version = '6.0.0'
    author = 'Your Name'
    description = _('Injects custom code into the HTML head of event pages.')
    category = 'CUSTOMIZATION'
    visible = True
    featured = False

    def ready(self):
        from . import signals

default_app_config = 'pretix_header_injector.HeaderInjectorApp'
