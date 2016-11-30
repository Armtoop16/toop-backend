# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework import serializers

# Local apps imports
from apps.core.connections.models import Connection


class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = '__all__'
