from django.dispatch import receiver
from django.utils.safestring import mark_safe
from pretix.presale.signals import html_head

@receiver(html_head, dispatch_uid="header_injector")
def inject_header(sender, request, **kwargs):
    return mark_safe('<!-- Header Injector Active -->')
