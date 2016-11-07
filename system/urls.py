# -*- coding: utf-8 -*-

# Core Django imports
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Admin Panel
    url(r'^admin/', include(admin.site.urls)),

    # Api
    url(r'^api/v1/', include('apps.api.v1.urls')),

    # Website
    url(r'', include('apps.web.urls')),
]
