# -*- coding: utf-8 -*-

from collective.aviary.interfaces import IAviarySettings
from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView
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

        return """
var featherEditor = new Aviary.Feather({{
    apiKey: '{0}',
    apiVersion: {1},
    theme: '{2}',
    tools: '{3}',
    appendTo: 'content',
    onSave: function(imageID, newURL) {{
        $('#' + imageID).attr('src', newURL);
    }},
    onError: function(errorObj) {{
        alert(errorObj.message);
    }}
    }});
    function launchEditor(el) {{
        el = $(el);
        // Image with no id, set a random id
        if(!el.attr('id')) {{
            var id = String(Math.random()).split('.').pop();
            el.attr('id', id);
        }}
        id = el.attr('id');
        src = el.attr('src');
        featherEditor.launch({{
            image: id,
            url: src
        }});
        return false;
    }}
$(function() {{
    launchEditor($('#content-core img'));
}});
""".format(settings.api_key, settings.api_version, settings.theme,
           settings.tools)
