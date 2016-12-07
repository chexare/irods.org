#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'iRODS Consortium'
SITENAME = 'iRODS'
SITEURL = ''
SITEURL = '/newirodsorg'

THEME = './themes/irods_theme'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

PATH = 'content'
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_PATHS = ['posts']
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

# don't produce these pages
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

DEFAULT_PAGINATION = False

STATIC_PATHS = ['extras','images','uploads']

EXTRA_PATH_METADATA = {
    'extras/.htaccess':   {'path': '.htaccess'},
    'extras/robots.txt':  {'path': 'robots.txt'},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
