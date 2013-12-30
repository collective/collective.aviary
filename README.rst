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
    drop shadows, crop, resize an image, save as, and apply sepia. Was the
    first attemp to enhance Plone image editing options but, let's face it,
    who wants to use a user interface à la `GIMP`_ these days?

`collective.externalimageeditor`_
    Integrates Aviary, `FotoFlexer`_ and `Pixlr`_ into Plone. Unfortunately,
    `Aviary support was broken`_ when we test it and it was the only service
    we wanted to use. On the other side, creating a new package with support
    only for Aviary allow us better control of its features.

`plone.app.imagecropping`_
    Allows images to be manually cropped using `Jcrop`_, a jQuery image
    cropping plugin. This package aims to be `THE cropping solution for Plone
    that just works` ™. Unfortunately, the package only use case is cropping
    on the scales given by `plone.app.imaging`_ and not on the original image.

.. _`Aviary support was broken`: https://github.com/collective/collective.externalimageeditor/issues/2
.. _`collective.externalimageeditor`: https://pypi.python.org/pypi/collective.externalimageeditor
.. _`FotoFlexer`: http://fotoflexer.com/
.. _`GIMP`: http://www.gimp.org/
.. _`Jcrop`: http://deepliquid.com/content/Jcrop.html
.. _`Pixlr`: https://www.pixlr.com/
.. _`plone.app.imagecropping`: https://pypi.python.org/pypi/plone.app.imagecropping
.. _`plone.app.imaging`: https://pypi.python.org/pypi/plone.app.imaging
.. _`Products.ImageEditor`: https://pypi.python.org/pypi/Products.ImageEditor
