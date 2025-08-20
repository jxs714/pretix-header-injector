from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "pretix_header_injector"
    verbose_name = "Pretix Header Injector"

    class PretixPluginMeta:
        name = gettext_lazy("Pretix Header Injector")
        author = "Fueled By X"
        description = gettext_lazy("Inject any script into pretix header for analytics etc")
        visible = True
        version = __version__
        category = "CUSTOMIZATION"
        compatibility = "pretix>=2.7.0"
        settings_links = []
        navigation_links = []

    def ready(self):
        from . import signals  # NOQA
