# -*- coding: utf-8 -*-

from collective.aviary import _
from collective.aviary.interfaces import IAviarySettings
from plone.app.registry.browser import controlpanel


class AviarySettingsEditForm(controlpanel.RegistryEditForm):
    schema = IAviarySettings
    label = _(u'Aviary')
    description = _(u'Settings for the Aviary photo editor.')


class AviarySettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = AviarySettingsEditForm
