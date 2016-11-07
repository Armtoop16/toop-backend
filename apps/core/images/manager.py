# -*- coding: utf-8 -*-

# Core Django imports
from django.db import models
from django.db.models.query import QuerySet


class ImageQuerySet(QuerySet):
    pass


class ImageManager(models.Manager):
    def get_query_set(self):
        return ImageQuerySet(self.model)
