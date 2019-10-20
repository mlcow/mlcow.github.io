#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'mlcow'
SITENAME = u'mlcow'
SITESUBTITLE = u'mlcow'
SITEURL = ''
THEME = 'my_themes/SoMA2/'
CSS_FILE = 'main.css?2'
#THEME = 'pelican-blueidea'
DISQUS_SITENAME = "mlcow-github-io"
GOOGLE_ANALYTICS = "UA-150419350-1"
PLUGIN_PATHS = ['pelican-plugins', 'plugins']
PLUGINS = ['pelican-cite', 'render_math']
#PLUGINS = ['pelican-cite', 'pandoc_reader', 'render_math']

PANDOC_EXTENSIONS = [
  '+hard_line_breaks',
  '+citations'
]

#PANDOC_ARGS =[ '--filter=pandoc-citeproc']


PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# pelican-cite
#PUBLICATIONS_SRC = 'content/bibliography.bib'

