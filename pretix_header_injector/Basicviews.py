from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from pretix.base.models import Event
from pretix.control.views.event import EventSettingsViewMixin

class HeaderInjectorSettingsView(EventSettingsViewMixin):
    """Settings view for header injector"""
    pass
