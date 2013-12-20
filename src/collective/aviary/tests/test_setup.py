# -*- coding: utf-8 -*-

from collective.aviary.config import PROJECTNAME
from collective.aviary.testing import INTEGRATION_TESTING
from plone.browserlayer.utils import registered_layers
from plone.testing.z2 import Browser

import unittest


EXPECTED_JS = (
    u'//dme0ih8comzn4.cloudfront.net/js/feather.js',
)


class TestInstall(unittest.TestCase):
    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME),
                        '%s not installed' % PROJECTNAME)

    def test_addon_layer_is_registered(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertIn('IAviaryLayer', layers)

    def test_js_are_registered(self):
        actual_js = self.portal.portal_javascripts.getResourceIds()
        for id in EXPECTED_JS:
            self.assertIn(id, actual_js)

    def test_static_resource_directory(self):
        app = self.layer['app']

        browser = Browser(app)
        portal_url = self.portal.absolute_url()

        browser.open('%s/++resource++collective.aviary' % portal_url)
        self.assertEqual(browser.headers['status'], '200 Ok')


class TestUninstall(unittest.TestCase):
    """Ensure product is properly uninstalled."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))

    def test_addon_layer_is_unregistered(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertNotIn('IAviaryLayer', layers)

    def test_js_are_unregistered(self):
        actual_js = self.portal.portal_javascripts.getResourceIds()
        for id in EXPECTED_JS:
            self.assertNotIn(id, actual_js)
