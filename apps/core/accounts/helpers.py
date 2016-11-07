# -*- coding: utf-8 -*-

# Stdlib imports
import os

# Core Django imports
from django.contrib.auth import get_user_model


def create_or_update_superuser(email=None, password=None):
    user_model = get_user_model()

    email = os.environ.get('APP_SUPERUSER_EMAIL', email)
    password = os.environ.get('APP_SUPERUSER_PASSWORD', password)

    try:
        user = user_model.objects.get(email=email)
    except user_model.DoesNotExist:
        user = user_model(email=email)

    user.email = email
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.first_name = 'Super'
    user.last_name = 'Admin'
    user.set_password(password)

    user.save()

    return user
