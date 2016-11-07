# -*- coding: utf-8 -*-

# Core Django imports
from django.http import HttpResponse

# Third-party app imports
import requests
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Local apps imports
from apps.api.v1.serializers.images import ImageSerializer
from apps.api.v1.utils.permissions import IsOwnerOrReadOnly
from apps.core.images.models import Image


class ImageViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    lookup_field = "pk"
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    allowed_methods = ['POST', 'DELETE']

    def create(self, request, *args, **kwargs):
        """
        Upload image
        ---
        parameters:
            - name: file
              required: true
              type: file
              paramType: form
        """
        return super(ImageViewSet, self).create(request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve image
        ---
        parameters:
            - name: width
              type: string
              paramType: query
            - name: height
              type: string
              paramType: query
            - name: blur_faces
              type: boolean
              paramType: query
            - name: add_red_overlay
              type: boolean
              paramType: query
        """
        segments = ["c_fill", "g_face"]

        """ Add blur effect """
        if request.GET.get("blur_faces", False) == 'true':
            segments.append("e_blur_faces")

        """ Add red overlay effect """
        if request.GET.get("add_red_overlay", False) == 'true':
            segments.append("e_multiply,l_red_pixel,o_30,w_1.0,h_1.0,fl_relative")

        """ Add width and height """
        dimensions = []
        width = request.GET.get('width', None)
        height = request.GET.get('height', None)

        if width is not None:
            dimensions.append("w_{}".format(width))

        if height is not None:
            dimensions.append("h_{}".format(height))

        if len(dimensions) > 0:
            segments.append("c_scale,{}".format(",".join(dimensions)))

        url = 'http://res.cloudinary.com/www-evetheapp-com/image/upload/{}/{}'.format(
            "/".join(segments),
            self.get_object().public_id
        )

        image = requests.get(url=url)
        return HttpResponse(image, content_type="image/jpeg")
