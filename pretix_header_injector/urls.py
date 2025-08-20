from django.urls import path
from . import views

# This defines the URL patterns for your plugin
# The 'app_name' is important for namespacing
app_name = 'pretix_header_injector'

urlpatterns = [
    # Settings page URL
    # This will be accessible at: /control/event/{organizer}/{event}/settings/plugins/header-injector/
    path('settings/', views.HeaderInjectorSettingsView.as_view(), name='settings'),
]
