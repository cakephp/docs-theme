#!/usr/bin/env python

import codecs
from setuptools import setup
from cakephp_theme import __version__

# README into long description
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()


setup(
    name='cakephp_theme',
    version=__version__,
    url='https://github.com/cakephp/doc-theme',
    author='Cake Software Foundation, Inc.',
    author_email='hi@cakephp.com',
    description='A Sphinx theme for CakePHP doc sites',
    long_description=readme,
    zip_safe=False,
    packages=['cakephp_theme'],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
