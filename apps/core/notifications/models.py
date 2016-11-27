# -*- coding: utf-8 -*-

# Core Django imports
from django.db import models


class Notification(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
