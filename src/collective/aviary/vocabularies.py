# -*- coding: utf-8 -*-

from collective.aviary import _
from collective.aviary.config import AVIARY_THEMES
from collective.aviary.config import AVIARY_TOOLS
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


def AvailableThemesVocabulary(context):
    items = []
    for theme in AVIARY_THEMES:
        items.append(SimpleTerm(value=theme, title=_(theme)))
    return SimpleVocabulary(items)


def AvailableToolsVocabulary(context):
    items = []
    for tool in AVIARY_TOOLS:
        items.append(SimpleTerm(value=tool, title=_(tool)))
    return SimpleVocabulary(items)
