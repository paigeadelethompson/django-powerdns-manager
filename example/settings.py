"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

#
# Python PATH
#
# Append directories to the PYTHON PATH
#

import os
import sys
# The current directory
#sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)) )
# The ``src`` directory.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')) )

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Django settings for example project.

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zz2g4+3mfe&amp;6rfin76pj8c$y_vd!qlcug6x(22*+e@gbr9=fsh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# IMPORTANT: If not set, the application will return 'Bad request 400' error if
# DEBUG is set to False.
# Enter the hostnames that should be allowed.
ALLOWED_HOSTS = []

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # PowerDNS Manager
    'powerdns_manager',

    # Debug toolbar (Comment to disable. Also comment reference in MIDDLEWARE_CLASSES)
    ##'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Debug Toolbar (Comment to disable. Also comment reference in INSTALLED_APPS)
    ##'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {    # Used by all apps of the Django project except django-powerdns-manager
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'main.db',               # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
    'powerdns': {    # Used by django-powerdns-manager and PowerDNS server
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'powerdns.db',           # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DATABASE_ROUTERS = ['powerdns_manager.routers.PowerdnsManagerDbRouter']

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery. (Default: True)
USE_I18N = False

USE_L10N = True

USE_TZ = True


# Media files

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Websites generally need to serve additional files such as images, JavaScript,
# or CSS. In Django, we refer to these files as "static files".
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = os.path.join(MEDIA_ROOT, 'site')

# URL prefix for static files.
STATIC_URL = MEDIA_URL + 'site/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


# Templates

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    
    # Directory for template overrides
    os.path.abspath(os.path.join(BASE_DIR, 'templates')),
)


# Performance
# https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/#performance-optimizations

# Default
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Using the cached templates
# https://docs.djangoproject.com/en/1.6/ref/templates/api/#django.template.loaders.cached.Loader
#TEMPLATE_LOADERS = (
#    ('django.template.loaders.cached.Loader', (
#        'django.template.loaders.filesystem.Loader',
#        'django.template.loaders.app_directories.Loader',
#    )),
#)


# Logging
# https://docs.djangoproject.com/en/dev/topics/logging/
#
# Default logging configuration:
#   * https://docs.djangoproject.com/en/dev/topics/logging/#django-s-default-logging-configuration
# Example:
#   * https://docs.djangoproject.com/en/dev/topics/logging/#configuring-logging
#


#
# App Settings
#

#
# django-debug-toolbar specific settings
# http://github.com/robhudson/django-debug-toolbar

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)


# PowerDNS Manager Settings

PDNS_DEFAULT_ZONE_TYPE = 'NATIVE'

PDNS_DEFAULT_RR_TTL = 86400

PDNS_ENABLED_RR_TYPES = [
    'SOA',
    'NS',
    'MX',
    'A',
    'AAAA',
    'CNAME',
    'PTR',
    'TXT',
    'SPF',
    'SRV',
#    'CERT',
#    'DNSKEY',
#    'DS',
#    'KEY',
#    'NSEC',
#    'RRSIG',
#    'HINFO',
#    'LOC',
#    'NAPTR',
#    'RP',
#    'AFSDB',
#    'SSHFP',
]
