# -*- coding: utf-8 -*-

# Core Django imports
from django.db import models
from django.conf import settings


class Lists(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='lists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
