# -*- coding: utf-8 -*-

from collective.aviary.interfaces import IAviarySettings
from plone import api
from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView
from urllib2 import HTTPError
from urllib2 import urlopen
from zope.component import getUtility


class AviaryTransform(BrowserView):
    """ Aviary Transform tab
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def javascript(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IAviarySettings)
        ltool = api.portal.get_tool('portal_languages')

        return """
var featherEditor = new Aviary.Feather({{
    apiKey: '{0}',
    apiVersion: {1},
    onLoad: function() {{
        launchEditor();
    }},
    theme: '{2}',
    tools: '{3}',
    language: '{4}'
    }});
""".format(settings.api_key, settings.api_version, settings.theme,
           settings.tools, ltool.getDefaultLanguage())


class Save(BrowserView):
    """ Save after Aviary returns the transformed image
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, imageUrl):
        response = self.request.response

        try:
            image = urlopen(imageUrl)
            field = self.context.getField('image')
            field.getMutator(self.context)(image.read())
            return response.redirect(self.context.absolute_url() + '/view')
        except HTTPError, error:
            api.portal.show_message(error.reason, self.request, type='error')
            return response.redirect(self.context.absolute_url() + '/atct_image_transform')
