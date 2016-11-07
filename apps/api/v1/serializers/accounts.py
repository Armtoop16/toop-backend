# -*- coding: utf-8 -*-

# Core Django imports
from django.contrib.auth import get_user_model

# Third-party app imports
from rest_framework import serializers
from rest_framework_gis.fields import GeometryField

# Local apps imports
from apps.contrib.helpers.date import birthday_to_age


class UserSerializer(serializers.ModelSerializer):
    location = GeometryField(required=False, help_text="Location format: POINT (lat lon)", )
    age = serializers.SerializerMethodField()
    score = serializers.FloatField(required=False)

    class Meta:
        model = get_user_model()
        exclude = ('password', 'user_permissions', 'groups', 'is_staff', 'is_superuser')
        read_only_fields = ('last_login', 'username', 'email', 'is_active', 'date_joined', 'score')

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)

        representation['location'] = None if instance.location is None else str(instance.location)

        return representation

    @staticmethod
    def get_age(obj):
        return birthday_to_age(obj.birthday)

    @staticmethod
    def get_score(obj):
        if obj.gendre == "male" and len(obj.owned_relations) == 0:
            return 10
