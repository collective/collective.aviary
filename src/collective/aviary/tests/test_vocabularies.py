# -*- coding: utf-8 -*-

from collective.aviary.testing import INTEGRATION_TESTING
from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory

import unittest


class VocabulariesTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_themes_vocabulary(self):
        name = u'collective.aviary.Themes'
        vocabulary = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(vocabulary)
        themes = vocabulary(self.portal)
        self.assertEqual(len(themes), 3)
        self.assertIn(u'dark', themes)
        self.assertIn(u'light', themes)
        self.assertIn(u'minimum', themes)

    def test_tools_vocabulary(self):
        name = u'collective.aviary.Tools'
        vocabulary = queryUtility(IVocabularyFactory, name)
        self.assertIsNotNone(vocabulary)
        themes = vocabulary(self.portal)
        self.assertEqual(len(themes), 1)
        self.assertIn(u'all', themes)
