from django.utils.translation import gettext_lazy as _

class PretixPluginMeta:
    name = _('Header Injector')
    author = 'Your Name'
    description = _('Embed any code into Pretix header event pages')
    visible = True
    version = '1.0.0'

default_app_config = 'pretix_header_injector.PluginApp'
