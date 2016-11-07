# -*- coding: utf-8 -*-

# Core Django imports
from django.contrib import admin

# Local apps imports
from apps.core.images.models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('public_id', 'owner', 'created_at', 'updated_at')


admin.site.register(Image, ImageAdmin)
