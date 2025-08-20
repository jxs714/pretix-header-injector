from django.dispatch import receiver
from django.utils.safestring import mark_safe
from pretix.presale.signals import html_head
from pretix.base.settings import settings_hierarkey

settings_hierarkey.add_default('header_injector_code', '', str)

@receiver(html_head, dispatch_uid="header_injector_html_head")
def header_injector_html_head(sender, request, **kwargs):
    code = sender.settings.get('header_injector_code')
    if code:
        return mark_safe(code)
    return ""
