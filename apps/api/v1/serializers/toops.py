# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework import serializers

# Local apps imports
from apps.core.toops.models import Toop


class ToopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toop
