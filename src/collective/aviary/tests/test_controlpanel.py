# -*- coding: utf-8 -*-

from collective.aviary.config import DEFAULT_THEME
from collective.aviary.config import DEFAULT_TOOLS
from collective.aviary.config import DEFAULT_VERSION
from collective.aviary.config import PROJECTNAME
from collective.aviary.interfaces import IAviarySettings
from collective.aviary.testing import INTEGRATION_TESTING
from plone import api
from plone.app.testing import logout
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import unittest


class ControlPanelTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.controlpanel = self.portal['portal_controlpanel']

    def test_controlpanel_has_view(self):
        request = self.layer['request']
        view = api.content.get_view(u'aviary-settings', self.portal, request)
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_controlpanel_view_is_protected(self):
        from AccessControl import Unauthorized
        logout()
        with self.assertRaises(Unauthorized):
            self.portal.restrictedTraverse('@@aviary-settings')

    def test_controlpanel_installed(self):
        actions = [a.getAction(self)['id']
                   for a in self.controlpanel.listActions()]
        self.assertIn('aviary', actions)

    def test_controlpanel_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']
        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECTNAME])
        actions = [a.getAction(self)['id']
                   for a in self.controlpanel.listActions()]
        self.assertNotIn('aviary', actions)


class RegistryTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.registry = getUtility(IRegistry)
        self.settings = self.registry.forInterface(IAviarySettings)

    def test_api_key_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'api_key'))
        self.assertEqual(self.settings.api_key, None)

    def test_api_version_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'api_version'))
        self.assertEqual(self.settings.api_version, DEFAULT_VERSION)

    def test_theme_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'theme'))
        self.assertEqual(self.settings.theme, DEFAULT_THEME)

    def test_tools_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'tools'))
        self.assertEqual(self.settings.tools, DEFAULT_TOOLS)

    def test_records_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']
        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECTNAME])

        BASE_REGISTRY = 'collective.aviary.interfaces.IAviarySettings.'
        records = [
            BASE_REGISTRY + 'api_key',
            BASE_REGISTRY + 'api_version',
            BASE_REGISTRY + 'theme',
            BASE_REGISTRY + 'tools',
        ]

        for r in records:
            self.assertNotIn(r, self.registry)
