# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Local apps imports
from apps.core.connections.models import Connection
from apps.api.v1.serializers.connections import ConnectionSerializer
from apps.api.v1.utils.paginators import APIPaginator
from apps.api.v1.utils.permissions import IsUserOrReadOnly


class ConnectionsViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    lookup_field = "pk"
    queryset = Connection.objects.all()
    pagination_class = APIPaginator
    serializer_class = ConnectionSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsUserOrReadOnly)
    allowed_methods = ['GET']
