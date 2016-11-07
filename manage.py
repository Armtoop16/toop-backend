#!/usr/bin/env python

# Stdlib imports
import sys
import os

# Local apps imports
from system.utils import read_env

if __name__ == "__main__":
    # Set Django setting module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "system.settings")

    from django.core.management import execute_from_command_line

    # Set environment variables
    read_env()

    # Execute Django
    execute_from_command_line(sys.argv)
