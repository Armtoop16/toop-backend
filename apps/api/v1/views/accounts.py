# -*- coding: utf-8 -*-

# Core Django imports
from django.contrib.auth import get_user_model

# Third-party app imports
from rest_framework import mixins, viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import list_route, detail_route
from rest_framework.permissions import IsAuthenticated

# Local apps imports
from rest_framework.response import Response

from apps.api.v1.serializers.accounts import UserSerializer
from apps.api.v1.utils.paginators import APIPaginator
from apps.api.v1.utils.permissions import IsUserOrReadOnly


class UserViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    lookup_field = "pk"
    queryset = get_user_model().objects.all()
    pagination_class = APIPaginator
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsUserOrReadOnly)
    allowed_methods = ['POST', 'PUT', 'GET', 'DELETE']

    @list_route(methods=['GET'])
    def me(self, request):
        """ Get requesting user """
        user = request.user
        serializer = UserSerializer(instance=user)

        return Response(data=serializer.data)

    @detail_route(methods=['DELETE'])
    def deactivate(self, request, pk=None):
        """ Deactivate account """
        user = self.get_object()
        self.check_object_permissions(request=request, obj=user)

        user.is_active = False
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
