# -*- coding: utf-8 -*-

from collective.aviary import _
from collective.aviary.config import DEFAULT_THEME
from collective.aviary.config import DEFAULT_TOOLS
from plone.directives import form
from zope import schema
from zope.interface import Interface


class IAviaryLayer(Interface):
    """Layer especifico para este add-on.
    """


class IAviarySettings(form.Schema):
    """Interface for the control panel form.
    """

    api_key = schema.ASCIILine(
        title=_(u'API key'),
        description=_(u''),
        required=False,
    )

    api_version = schema.Int(
        title=_(u'Editor version'),
        description=_(u''),
        readonly=True,
        required=True,
    )

    theme = schema.Choice(
        title=_(u'Theme'),
        description=_(u''),
        required=True,
        default=DEFAULT_THEME,
        vocabulary=u'collective.aviary.Themes',
    )

    form.widget(tools='z3c.form.browser.checkbox.CheckBoxFieldWidget')
    tools = schema.Choice(
        title=_(u'Tools'),
        description=_(u'Select which editing tools you would like to display in the tools panel.'),
        required=True,
        default=DEFAULT_TOOLS,
        vocabulary=u'collective.aviary.Tools',
    )
