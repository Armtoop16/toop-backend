# -*- coding: utf-8 -*-

# Stdlib imports
import os

# Core Django imports
from django.contrib.sites.models import Site

# Third-party apps imports
from allauth.socialaccount.models import SocialApp


def create_facebook_app():
    app = SocialApp.objects.create(
        provider="facebook",
        name="Facebook",
        client_id=os.environ.get("APP_FB_APP_ID", None),
        secret=os.environ.get("APP_FB_APP_SECRET", None)
    )

    app.sites.add(Site.objects.filter().first())
    app.save()
