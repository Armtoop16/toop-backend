# -*- coding: utf-8 -*-

# Stdlib imports
import os

# Third-party app imports
from rest_framework import serializers
import cloudinary
import cloudinary.uploader

# Local apps imports
from apps.core.images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    file = serializers.ImageField(write_only=True)

    class Meta:
        model = Image
        exclude = ('version', 'width', 'height', 'format', 'bytes', 'secure_url', 'env', 'owner')
        read_only_fields = ('id', 'public_id', 'url', 'created_at', 'updated_at')

    def create(self, validated_data):
        uploaded_image = cloudinary.uploader.upload(validated_data.get('file'))
        owner = self.context['request'].user

        image = Image(
            owner=owner,
            public_id=uploaded_image['public_id'],
            version=uploaded_image['version'],
            width=uploaded_image['width'],
            height=uploaded_image['height'],
            format=uploaded_image['format'],
            bytes=uploaded_image['bytes'],
            url=uploaded_image['url'],
            secure_url=uploaded_image['secure_url'],
            env=os.environ.get("APP_ENVIRONMENT", "local")
        )
        image.save()

        return image
