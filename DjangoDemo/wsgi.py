"""
WSGI config for DjangoDemo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoDemo.settings")

application = get_wsgi_application()
#PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#import sys
#sys.path.insert(0,PROJECT_DIR)
