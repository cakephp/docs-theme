import os

__version__ = '1.0.0'


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return cur_dir


def update_context(app, pagename, templatename, context, doctree):
    context['cakephp_theme_version'] = __version__
    context['branch'] = app.config.branch


def setup(app):
    app.connect('html-page-context', update_context)
    app.add_config_value('branch', '', True)
    return {'version': __version__,
            'parallel_read_safe': True}
