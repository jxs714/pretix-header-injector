from django.utils.translation import gettext_lazy as _
from pretix.base.plugins import PluginConfig

class HeaderInjectorApp(PluginConfig):
    name = 'pretix_header_injector'
    verbose_name = 'Header Code Injector'

    class PretixPluginMeta:
        name = _('Header Code Injector')
        author = _('Your Name')
        version = '2.0.0' # Bumping version to guarantee a fresh install
        description = _('Injects custom code (e.g., Google Analytics, Meta Pixel) into the HTML head of event pages.')
        visible = True
        category = 'CUSTOMIZATION'
        featured = False

    def ready(self):
        from . import signals  # NOQA

default_app_config = 'pretix_header_injector.HeaderInjectorApp'
