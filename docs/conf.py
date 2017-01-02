# -*- coding: utf-8 -*-
import datetime
import sys
import os
import cakephp_theme
from sphinx.highlighting import lexers
from pygments.lexers.php import PhpLexer

########################
# Begin Customizations #
########################

maintainer = u'cakephp'
project = u'doc-theme'
project_pretty_name = u'CakePHP Doc Theme'
copyright = u'%d, CakePHP' % datetime.datetime.now().year
version = '0.0.0'
release = '0.0.0'
html_title = 'CakePHP Doc Theme'
html_context = {
    'maintainer': maintainer,
    'project_pretty_name': project_pretty_name,
    'projects': {
        'CakePHP Book': 'https://book.cakephp.org/',
        'Doc Theme': 'https://cakephp-theme.readthedocs.io/',
    }
}

htmlhelp_basename = 'cakephp-theme'
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'cakephp-theme.tex', u'cakephp-theme',
     u'CakePHP', 'manual'),
]
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'cakephp-theme', u'CakePHP Doc Theme Documentation',
     [u'CakePHP'], 1)
]

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'cakephp-theme', u'CakePHP Doc Theme Documentation',
     u'CakePHP', 'cakephp-theme', 'A Sphinx theme for CakePHP doc sites',
     'Miscellaneous'),
]

branch = 'master'

########################
#  End Customizations  #
########################

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.todo',
    'sphinxcontrib.phpdomain',
    'cakephp_theme',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'contents'
exclude_patterns = [
    '_build',
    '_themes',
    '_partials',
]

pygments_style = 'sphinx'
highlight_language = 'php'

# -- Options for HTML output ----------------------------------------------

html_theme = 'cakephp_theme'
html_theme_path = [cakephp_theme.get_html_theme_path()]
html_static_path = []
html_last_updated_fmt = '%b %d, %Y'
html_sidebars = {
    '**': ['globaltoc.html', 'localtoc.html']
}

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

lexers['php'] = PhpLexer(startinline=True)
lexers['phpinline'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
primary_domain = "php"
