from django.urls import reverse
from django.views.generic import FormView
from pretix.control.forms.event import event_settings_form_factory

class SettingsView(FormView):
    template_name = 'pretix_header_injector/settings.html'
    form_class = event_settings_form_factory(
        [
            'header_injector_code',
        ]
    )

    def get_success_url(self):
        return reverse('plugins:pretix_header_injector:settings', kwargs={
            'organizer': self.request.event.organizer.slug,
            'event': self.request.event.slug,
        })

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['obj'] = self.request.event
        return kwargs

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            self.request.event.log_action('pretix.plugins.header_injector.settings', user=self.request.user)
        return super().post(request, *args, **kwargs)
