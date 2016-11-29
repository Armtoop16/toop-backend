# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Local apps imports
from apps.core.gifts.models import Gift
from apps.api.v1.serializers.gifts import GiftSerializer
from apps.api.v1.utils.paginators import APIPaginator
from apps.api.v1.utils.permissions import IsUserOrReadOnly


class GiftsViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    lookup_field = "pk"
    queryset = Gift.objects.all()
    pagination_class = APIPaginator
    serializer_class = GiftSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsUserOrReadOnly)
    allowed_methods = ['GET']
