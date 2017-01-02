============
Installation
============

Requirements
============

* Python and Pip
* Sphinx 1.5+

Setup
=====

* You will need to install the `cakephp_theme` package:

.. code-block:: shell

    # from pypi
    pip install cakephp_theme

    # from github
    pip install -e git+https://github.com/cakephp/doc-theme/#egg=cakephp_theme

Usage
=====

Add the following to your ``conf.py`` so the theme location is loaded:

.. code-block:: python

    import cakephp_theme

    html_theme_path = [cakephp_theme.get_path()]
    html_theme = 'cakephp_theme'
    extensions = ['cakephp_theme']


Add an explicit ``html_context`` setting so the theme's
customized attributes are properly initialized:
   
.. code-block:: python
    
    html_context = {
        'maintainer': 'Your Name',
        'project_pretty_name': 'Your Project Name',
        'projects': {
            'CakePHP Book': 'https://book.cakephp.org/',
            'Some other project': 'https://example.com/',
        }
    }

That's it! You now have the CakePHP documentation theme set up.
