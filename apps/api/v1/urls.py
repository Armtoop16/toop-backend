# -*- coding: utf-8 -*-

# Core Django imports
from django.conf.urls import include, url

# Third-party app imports
from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet, GCMDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter

# Local apps imports
from apps.web.accounts.views import FacebookLogin
from apps.api.v1.views import accounts, auth, images, collaborations, companies, connections, gifts, lists, toops

router = DefaultRouter()

# Devices
router.register(r'device/apns', APNSDeviceAuthorizedViewSet)
router.register(r'device/gcm', GCMDeviceAuthorizedViewSet)

# Accounts
router.register(r'^accounts', accounts.UserViewSet, 'accounts')

# Collaborations
router.register(r'^collaborations', collaborations.CollaborationsViewSet, 'collaborations')

# Companies
router.register(r'^companies', companies.CompaniesViewSet, 'companies')

# Connections
router.register(r'^connections', connections.ConnectionsViewSet, 'connections')

# Gifts
router.register(r'^gifts', gifts.GiftsViewSet, 'gifts')

# Lists
router.register(r'^lists', lists.ListsViewSet, 'lists')

# Toops
router.register(r'^toops', toops.ToopsViewSet, 'toops')

""" Images """
router.register(r'^images', images.ImageViewSet, 'images')

urlpatterns = [
    # Django Rest Auth
    url(r'^auth/facebook/$', FacebookLogin.as_view(), name='api.facebook_login'),
    url(r'^auth/logout/$', auth.logout, name='auth.logout'),

    # Django Push Notifications
    url(r'^', include(router.urls)),

    # Django Rest Swagger
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
