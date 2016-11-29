# -*- coding: utf-8 -*-

# Core Django imports
from django.db import models

# Local apps imports
from apps.core.lists.models import Lists


class Gift(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    list = models.ForeignKey(Lists, related_name='gifts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
