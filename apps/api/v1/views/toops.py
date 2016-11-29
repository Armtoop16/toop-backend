# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Local apps imports
from apps.core.toops.models import Toop
from apps.api.v1.serializers.toops import ToopSerializer
from apps.api.v1.utils.paginators import APIPaginator
from apps.api.v1.utils.permissions import IsUserOrReadOnly


class ToopsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    lookup_field = "pk"
    queryset = Toop.objects.all()
    pagination_class = APIPaginator
    serializer_class = ToopSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsUserOrReadOnly)
    allowed_methods = ['GET']
