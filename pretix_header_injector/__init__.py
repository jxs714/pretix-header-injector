from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PluginApp(AppConfig):
    name = 'pretix_header_injector'
    verbose_name = 'Pretix Header Injector'

    class PretixPluginMeta:
        name = _('Header Injector')
        author = 'Your Name'
        description = _('Embed any code into Pretix header event pages')
        visible = True
        version = '1.0.0'
        category = 'CUSTOMIZATION'
        compatibility = "pretix>=3.0.0"

    def ready(self):
        from . import signals  # noqa


# Make PretixPluginMeta available at module level for entry point
PretixPluginMeta = PluginApp.PretixPluginMeta
default_app_config = 'pretix_header_injector.PluginApp'
