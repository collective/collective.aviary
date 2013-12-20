# -*- coding: utf-8 -*-

from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implements

PROJECTNAME = 'collective.aviary'

AVIARY_THEMES = [
    'dark',
    'light',
    'minimum',
]

AVIARY_TOOLS = [
    'all',
]

DEFAULT_THEME = 'minimum'
DEFAULT_TOOLS = 'all'
DEFAULT_VERSION = 3


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [
            u'collective.aviary:uninstall',
        ]
