from django.dispatch import receiver
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from pretix.presale.signals import html_head


@receiver(html_head, dispatch_uid="header_injector_html_head")
def add_header_code(sender, request, **kwargs):
    """
    Add custom header code to event pages
    This function runs every time a page loads and adds custom HTML to the <head> section
    """
    try:
        # Get the event from the sender
        event = sender
        
        # Check if our plugin is enabled for this event
        if not hasattr(event, 'settings'):
            return ""
            
        # Get custom header code from event settings (if you implement settings later)
        custom_code = event.settings.get('header_injector_code', '')
        
        # For now, let's add a simple comment to prove the plugin works
        default_code = """
<!-- Header Injector Plugin Active -->
<meta name="header-injector" content="active">
"""
        
        # If there's custom code, use it, otherwise use default
        if custom_code:
            return mark_safe(custom_code)
        else:
            return mark_safe(default_code)
            
    except Exception as e:
        # If anything goes wrong, fail silently
        return ""
