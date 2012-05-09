import os, sys
sys.path.append('/home/www/csesoc-website')
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings_production'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()