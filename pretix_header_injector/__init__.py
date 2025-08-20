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
        compatibility = "pretix>=4.0.0"

    def ready(self):
        from . import signals  # noqa

    @property
    def control_urls(self):
        from django.urls import include, path
        return [
            path('plugins/header-injector/', include('pretix_header_injector.urls')),
        ]


# This is crucial - make PretixPluginMeta available at module level
PretixPluginMeta = PluginApp.PretixPluginMeta
default_app_config = 'pretix_header_injector.PluginApp'
