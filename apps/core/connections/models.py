# -*- coding: utf-8 -*-

# Core Django imports
from django.db import models
from django.conf import settings

# Third-party apps imports
from allauth.socialaccount.models import SocialAccount


class Connection(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='connections', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
