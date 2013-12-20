*****************
collective.aviary
*****************

.. contents:: Table of Contents

Life, the Universe, and Everything
==================================

``collective.aviary`` integrates the `Aviary`_ photo editor into Plone.

Mostly Harmless
---------------

.. image:: https://secure.travis-ci.org/collective/collective.aviary.png?branch=master
    :alt: Travis CI badge
    :target: http://travis-ci.org/collective/collective.aviary

.. image:: https://coveralls.io/repos/collective/collective.aviary/badge.png?branch=master
    :alt: coveralls badge
    :target: https://coveralls.io/r/collective/collective.aviary

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

.. _`opening a support ticket`: https://github.com/collective/collective.aviary/issues

Don't Panic
-----------

Installation
^^^^^^^^^^^^

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

Not entirely unlike
-------------------

`Products.ImageEditor`_
    Adds an ``Image Editor`` link near the image widget allowing the user to
    rotate, flip, blur, compress, change contrast & brightness, sharpen, add
    drop shadows, crop, resize an image, save as, and apply sepia. Was the
    first attemp to enhance Plone image editing options but, let's face it,
    who wants to use an user interface à la `GIMP`_ these days?

`collective.externalimageeditor`_
    Integrates `Aviary`_, `FotoFlexer`_ and `Pixlr`_ into Plone. Creating a
    new package with support only for `Aviary`_ allow us better control on its
    features following the `KISS principle`_.

`plone.app.imagecropping`_
    Allows images to be manually cropped using `Jcrop`_, a jQuery image
    cropping plugin. This package aims to be `THE cropping solution for Plone
    that just works` ™. Unfortunately, the package only use case is cropping
    on the scales given by `plone.app.imaging`_ and not on the original image.

.. _`Aviary`: http://developers.aviary.com/
.. _`collective.externalimageeditor`: https://pypi.python.org/pypi/collective.externalimageeditor
.. _`FotoFlexer`: http://fotoflexer.com/
.. _`GIMP`: http://www.gimp.org/
.. _`Jcrop`: http://deepliquid.com/content/Jcrop.html
.. _`KISS principle`: https://en.wikipedia.org/wiki/KISS_principle
.. _`Pixlr`: https://www.pixlr.com/
.. _`plone.app.imagecropping`: https://pypi.python.org/pypi/plone.app.imagecropping
.. _`plone.app.imaging`: https://pypi.python.org/pypi/plone.app.imaging
.. _`Products.ImageEditor`: https://pypi.python.org/pypi/Products.ImageEditor