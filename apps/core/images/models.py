# -*- coding: utf-8 -*-

# Core Django imports
from django.conf import settings
from django.db import models

# Third-party app imports
import cloudinary.uploader
from django.dispatch import receiver

# Local apps imports
from apps.core.images.manager import ImageManager


class Image(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    public_id = models.CharField(max_length=64)
    version = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    format = models.CharField(max_length=8)
    bytes = models.IntegerField()
    url = models.URLField()
    secure_url = models.URLField()
    env = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ImageManager()

    def __str__(self):
        return self.public_id


@receiver(models.signals.post_delete, sender=Image)
def remove_from_storage(sender, instance, *args, **kwargs):
    """ Remove from Cloudinary on instance delete. """
    cloudinary.uploader.destroy(instance.public_id)
