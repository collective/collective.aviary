*****************
collective.aviary
*****************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

``collective.aviary`` integrates the `Aviary photo editor`_ into Plone.

.. _`Aviary photo editor`: http://developers.aviary.com/

Mostly Harmless
===============

.. image:: https://secure.travis-ci.org/collective/collective.aviary.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/collective/collective.aviary

.. image:: https://coveralls.io/repos/collective/collective.aviary/badge.png?branch=master
    :alt: coveralls badge
    :target: https://coveralls.io/r/collective/collective.aviary

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/collective.aviary/issues

Don't Panic
===========

Installation
------------

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        collective.aviary

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.aviary`` and click the 'Activate' button.

.. Note::
    You may have to empty your browser cache and save your resource registries
    in order to see the effects of the product installation.

Usage
-----

The Aviary photo editor is a proprietary web widget that can be embedded in
any website with just a few lines of Javascript, adding simple yet powerful
image editing to an existing workflow. It is optimized for the latest versions
of Chrome, Firefox, Safari, and Internet Explorer (IE9). The editor also works
in mobile browsers, so it will function on handheld touch-screen devices, but
it works best on tablets.

``collective.aviary`` replaces the standard **Transform** tab in native Image
content type with a new one that invokes the Aviary photo editor.

.. image:: https://raw.github.com/collective/collective.aviary/master/aviary.png
    :align: center
    :alt: The Aviary photo editor in action.
    :height: 680px
    :width: 768px

.. Note::
    Aviary Basic SDK maximum output resolution is 1 megapixel on its web
    version.

To-do list
----------

- `Enable CORS`_
- `Define available tools`_
- `Add suport for plone.app.contenttypes`_

.. _`Enable CORS`: https://github.com/collective/collective.aviary/issues/1
.. _`Define available tools`: https://github.com/collective/collective.aviary/issues/4
.. _`Add suport for plone.app.contenttypes`: https://github.com/collective/collective.aviary/issues/5

Not entirely unlike
===================

`Products.ImageEditor`_
    Adds an ``Image Editor`` link near the image widget allowing the user to
    rotate, flip, blur, compress, change contrast & brightness, sharpen, add
    drop shadows, crop, resize an image, save as, and apply sepia.

`collective.externalimageeditor`_
    Integrates `Aviary photo editor`_, `FotoFlexer`_ and `Pixlr`_ into Plone.

`plone.app.imagecropping`_
    Allows images to be manually cropped using `Jcrop`_, a jQuery image
    cropping plugin.

.. _`collective.externalimageeditor`: https://pypi.python.org/pypi/collective.externalimageeditor
.. _`FotoFlexer`: http://fotoflexer.com/
.. _`Jcrop`: http://deepliquid.com/content/Jcrop.html
.. _`Pixlr`: https://www.pixlr.com/
.. _`plone.app.imagecropping`: https://pypi.python.org/pypi/plone.app.imagecropping
.. _`Products.ImageEditor`: https://pypi.python.org/pypi/Products.ImageEditor
