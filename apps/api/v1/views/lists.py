# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Local apps imports
from apps.core.lists.models import Lists
from apps.api.v1.serializers.lists import ListsSerializer
from apps.api.v1.utils.paginators import APIPaginator
from apps.api.v1.utils.permissions import IsUserOrReadOnly


class ListsViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    lookup_field = "pk"
    queryset = Lists.objects.all()
    pagination_class = APIPaginator
    serializer_class = ListsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsUserOrReadOnly)
    allowed_methods = ['GET']
