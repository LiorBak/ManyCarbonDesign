from os import environ
import dj_database_url
import os
from pathlib import Path

SESSION_CONFIGS = [
     dict(
         name='Oil_Game',
         num_demo_participants=3,
         is_control=True,
         use_browser_bots=False,
         app_sequence=['ManyDesignsCarbon', 'Survey']),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.001, participation_fee=2.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

ROOMS = [
    dict(
        name='room1',
        display_name='Room 1 control',
    ),
    dict(
        name='room2',
        display_name='Room 2 treatment',
    ),
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = ''

SECRET_KEY = '9727914704108'

DEBUG = environ.get('DEBUG', 'False').lower() == 'true'

AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL', None)

DATABASES = {
    'default': dj_database_url.config(default=environ.get('DATABASE_URL'))
}

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
