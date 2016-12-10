# -*- coding: utf-8 -*-

# Stdlib imports
import os
import six
import dateutil.parser

# Core Django imports
from django.contrib.auth.validators import UnicodeUsernameValidator, ASCIIUsernameValidator
from django.db.models import Q
from django.utils import timezone
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver

# Third-party apps imports
from allauth.account.signals import user_signed_up
import cloudinary
import cloudinary.uploader
import cloudinary.api
from allauth.socialaccount.models import SocialAccount, SocialToken
import facebook

# Local apps imports
from apps.core.connections.models import Connection
from apps.core.images.models import Image
from apps.core.lists.models import Lists
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    username_validator = UnicodeUsernameValidator() if six.PY3 else ASCIIUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    email = models.EmailField(_('email address'), blank=True, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    birthday = models.DateField(null=True, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    gender = models.CharField(max_length=8, null=True, blank=True, choices=GENDER_CHOICES)
    avatar = models.ForeignKey(Image, null=True, blank=True, related_name="avatar")
    about = models.TextField(null=True, blank=True)
    facebook_id = models.BigIntegerField(null=True, blank=True)
    location = models.PointField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        """ The user is identified by their email address """
        return self.email

    def get_short_name(self):
        """ The user is identified by their email address """
        return self.email

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = "auth_user"


# ----------------------------------------------------------------------------------------------------------------------
# Signals
# ----------------------------------------------------------------------------------------------------------------------

@receiver(user_signed_up)
def add_social_fields(sender, **kwargs):
    """ Add social fields to User """
    user = kwargs.get('user', None)
    if user is not None:
        social_account = SocialAccount.objects.get(user=user)
        social_token = SocialToken.objects.get(account=social_account)

        social_login = kwargs.get('sociallogin', None)
        if social_login is not None:
            """ Assign FB ID to profile. """
            user.facebook_id = social_login.account.extra_data.get('id')
            user.save()

            """ Assign FB profile picture to user. """
            try:
                image_url = 'http://graph.facebook.com/{}/picture?height=1000&width=1000'.format(
                    social_login.account.extra_data.get('id'))
                uploaded_image = cloudinary.uploader.upload(image_url)

                image = Image(owner=user, public_id=uploaded_image['public_id'], version=uploaded_image['version'],
                              width=uploaded_image['width'], height=uploaded_image['height'], url=uploaded_image['url'],
                              format=uploaded_image['format'], bytes=uploaded_image['bytes'],
                              secure_url=uploaded_image['secure_url'], env=os.environ.get("APP_ENVIRONMENT", "local"))

                image.save()
                user.avatar = image
                user.save()
            except cloudinary.uploader.Error:
                pass

            """ Assign birthday, gender. """
            user.birthday = dateutil.parser.parse(social_login.account.extra_data.get('birthday'))
            user.gender = social_login.account.extra_data.get('gender')
            user.save()

            """ Add connections. """
            graph = facebook.GraphAPI(access_token=social_token.token, version='2.7')
            friends = graph.get_connections(id=social_account.uid, connection_name='friends', fields='id')

            friends_ids = [friend['id'] for friend in friends['data']]

            for friend_id in friends_ids:
                try:
                    connection_account = SocialAccount.objects.filter(Q(uid=friend_id) & Q(provider='facebook'))
                    Connection.objects.get_or_create(owner=user, user=connection_account.user)
                except SocialAccount.DoesNotExist:
                    pass

            """ Add default lists. """
            wish_lists = ['Birthday', 'New year', 'Thanksgiving']

            for wish_list in wish_lists:
                Lists.objects.get_or_create(owner=user, name=wish_list)
