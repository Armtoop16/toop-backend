# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework import serializers

# Local apps imports
from apps.core.companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
