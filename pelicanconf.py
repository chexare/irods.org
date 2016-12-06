#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'iRODS Consortium'
SITENAME = 'iRODS'
SITEURL = ''

PATH = 'content'

THEME = './themes/irods_theme'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

STATIC_PATHS = ['extras']

EXTRA_PATH_METADATA = {
    'extras/.htaccess':   {'path': '.htaccess'},
    'extras/robots.txt':  {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
}
