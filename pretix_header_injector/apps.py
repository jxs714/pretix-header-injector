from django.utils.translation import gettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

from . import __version__

class PluginApp(PluginConfig):
    name = "pretix_header_injector"
    verbose_name = "Header Code Injector"
    urls = "pretix_header_injector.urls"

    class PretixPluginMeta:
        name = gettext_lazy("Header Code Injector")
        author = "Your Name"
        description = gettext_lazy("Injects custom code into the HTML head of event pages.")
        visible = True
        version = __version__
        category = "CUSTOMIZATION"
        compatibility = "pretix>=2.7.0"

    def ready(self):
        from . import signals  # NOQA
