# -*- coding: utf-8 -*-

from five import grok

grok.templatedir('templates')


class HelloWorld (grok.view):
    """Browserview de exemplo Hello World
    """
