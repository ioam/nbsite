# -*- coding: utf-8 -*-
# flake8: noqa (hacky way of sharing config, etc...)

from nbsite.shared_conf import *

###################################################
# edit things below as appropriate for your project

project = u'Project'
authors = u'Authors for html meta author'
copyright = u'2019 ' + authors
description = 'Short description for html meta description.'
version = release = '0.0.1'

html_static_path += ['_static']
html_theme = 'sphinx_pyviz_theme'
# logo file etc should be in html_static_path, e.g. _static
# only change colors in primary, primary_dark, and secondary
html_theme_options = {
#    'custom_css': 'site.css',
#    'logo': 'logo.png',
#    'favicon': 'favicon.ico',
#    'primary_color': 'coral',
#    'primary_color_dark': 'sienna',
#    'secondary_color': 'gold',
}

_NAV =  (
    ('Getting Started', 'getting_started/index'),
    ('User Guide', 'user_guide/index'),
    ('Gallery', 'gallery/index'),
    ('API', 'Reference_Manual/index'),
    ('FAQ', 'FAQ'),
    ('About', 'about')
)

html_context.update({
    'PROJECT': project,
    'DESCRIPTION': description,
    'AUTHOR': authors,
    # will work without this - for canonical (so can ignore when building locally or test deploying)
    'WEBSITE_SERVER': '//{}.pyviz.org'.format(project),
    'VERSION': version,
    'NAV': _NAV,
    # by default, footer links are same as those in header
    'LINKS': _NAV,
    'SOCIAL': (
        ('Gitter', '//gitter.im/pyviz/pyviz'),
        ('Twitter', '//twitter.com/pyviz_org'),
        ('Github', '//github.com/pyviz/{}'.format(project)),
    )
})
