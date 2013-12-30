# -*- coding:utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '1.0b1'
description = 'Integrates the Aviary photo editor into Plone.'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='collective.aviary',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: JavaScript',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone aviary javascript sdk',
    author='Simples Consultoria',
    author_email='products@simplesconsultoria.com.br',
    url='https://github.com/collective/collective.aviary',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'plone.app.registry',
        'plone.directives.form',
        'plone.i18n',
        'plone.registry',
        'Products.CMFPlone',
        'Products.GenericSetup',
        'setuptools',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
    ],
    extras_require={
        'test': [
            'plone.app.robotframework',
            'plone.app.testing [robot] >=4.2.2',
            'plone.browserlayer',
            'plone.registry',
            'plone.testing',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
