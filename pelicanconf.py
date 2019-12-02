#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Eric Lake'
SITENAME = 'Ramblings'
SITETITLE = 'Ramblings'
SITESUBTITLE = 'Ramblings of someone who should be more closely supervised!'
SITEDESCRIPTION = 'Ramblings of someone who should be more closely supervised!'
SITEURL = 'http://localhost:8000'
SITESRC = 'https://github.com/ericlake/ericlake.github.io'
SITELOGO = SITEURL + '/static/avatar.png'
FAVICON = SITEURL + '/static/favicon.ico'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Biography
BIO = "Site Reliability Engineer @LogDNA"
PROFILE_IMAGE = 'avatar.png'

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/ericlake/'),
          ('twitter', 'https://twitter.com/etank'),
          ('github', 'https://github.com/ericlake'))

DEFAULT_PAGINATION = 10

#DEFAULT_METADATA = {
#    'status': 'draft',
#}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# URL settings
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Theme
THEME = 'themes/flex'

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['neighbors', 'post_stats']

# static files
STATIC_PATHS = [
    'static'
]

JINJA_ENVIRONMENT = {
    'extensions': [
        'jinja2.ext.do'
    ]
}

COPYRIGHT_YEAR = 2019
COPYRIGHT_NAME = 'Eric Lake'

MAIN_MENU = True

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

LINKS = (('Archives', '/archives.html'),)
