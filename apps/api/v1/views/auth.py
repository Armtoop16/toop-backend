# Third-party apps imports
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from push_notifications.models import APNSDevice


@api_view(['post'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout(request):
    """ Logout user. """
    try:
        Token.objects.filter(user=request.user).delete()
    except Token.DoesNotExist:
        pass

    try:
        APNSDevice.objects.filter(user=request.user).delete()
    except APNSDevice.DoesNotExist:
        pass

    return Response(status=status.HTTP_204_NO_CONTENT)
