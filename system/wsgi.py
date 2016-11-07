# -*- coding: utf-8 -*-

# Stdlib imports
import os
import sys

# Get base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add app paths
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, 'system'))

from system.utils import read_env

# Read environment variables
read_env()

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system.settings")

# Core Django imports
from django.core.wsgi import get_wsgi_application

# Start Django application
application = get_wsgi_application()
