from django import forms
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView
from pretix.base.models import Event
from pretix.control.permissions import EventPermissionRequiredMixin
from pretix.control.views.event import EventSettingsViewMixin, EventSettingsFormView


class HeaderInjectorForm(forms.Form):
    """
    Form for header injector settings
    """
    header_code = forms.CharField(
        label=_('Custom Header Code'),
        help_text=_('Enter HTML, CSS, or JavaScript code to inject into the page header. This will be added to every page.'),
        widget=forms.Textarea(attrs={
            'rows': 10,
            'placeholder': '<!-- Example -->\n<script>\n  console.log("Hello from header injector!");\n</script>'
        }),
        required=False
    )


class HeaderInjectorSettingsView(EventPermissionRequiredMixin, EventSettingsFormView):
    """
    Settings view for the Header Injector plugin
    """
    model = Event
    form_class = HeaderInjectorForm
    template_name = 'pretix_header_injector/settings.html'
    permission = 'can_change_settings'
    
    def get_success_url(self):
        return reverse('plugins:pretix_header_injector:settings', kwargs={
            'event': self.request.event.slug,
            'organizer': self.request.event.organizer.slug
        })
    
    def form_valid(self, form):
        """
        Save the form data to event settings
        """
        self.request.event.settings.header_injector_code = form.cleaned_data['header_code']
        messages.success(self.request, _('Your header injection settings have been saved.'))
        return super().form_valid(form)
    
    def get_initial(self):
        """
        Load current settings into the form
        """
        return {
            'header_code': self.request.event.settings.get('header_injector_code', '')
        }
