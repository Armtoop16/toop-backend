# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework import serializers

# Local apps imports
from apps.core.lists.models import Lists


class ListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lists
        fields = '__all__'
