# -*- coding: utf-8 -*-

# Core Django imports
from django.db import models
from django.conf import settings

# Local apps imports
from apps.core.images.models import Image


class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ForeignKey(Image)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Moderator(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    company = models.ForeignKey(Company, related_name='moderators')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    image = models.ForeignKey(Image)
    company = models.ForeignKey(Company, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
