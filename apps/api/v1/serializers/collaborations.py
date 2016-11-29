# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework import serializers

# Local apps imports
from apps.core.collaborations.models import Collaboration


class CollaborationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaboration
