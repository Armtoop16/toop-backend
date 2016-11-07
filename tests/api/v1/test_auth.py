# -*- coding: utf-8 -*-

# Stdlib imports
import os

# Third-party app imports
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from push_notifications.models import APNSDevice

# Local apps imports
from tests.utils.helpers import create_facebook_app


class AuthTestCase(APITestCase):
    fixtures = ['users.json', 'devices.json']

    def setUp(self):
        self.maxDiff = None
        self.admin_token = 'b3369a8199ffaa4beb7175a8d103092b4ecf2671'
        self.john_token = 'd4569c10a7c996cc18fdc2b8e8ae057c18450e52'
        self.jane_token = 'f579f18ff8a47d08b6924b531fe2048d110702b1'

        create_facebook_app()

    def test_facebook_login_with_valid_token(self):
        response = self.client.post('/api/v1/auth/facebook/', {
            'access_token': os.environ.get('APP_FB_APP_TEST_TOKEN')
        })

        self.assertEqual(response.status_code, 200)
        self.assertTrue('key' in response.data)

        # Test if django user crated
        key = response.data.get('key', None)
        self.assertIsNotNone(key)

        token = Token.objects.get(key=key)
        self.assertIsNotNone(token)
        self.assertIsNotNone(token.user)

    def test_facebook_login_with_invalid_token(self):
        response = self.client.post('/api/v1/auth/facebook/', {
            'access_token': 'invalid' + os.environ.get('APP_FB_APP_TEST_TOKEN')
        })

        self.assertEqual(response.status_code, 400)

    def test_logout(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.post('/api/v1/auth/logout/')
        self.assertEqual(response.status_code, 204)

        tokens = Token.objects.filter(user=2)
        self.assertEqual(len(tokens), 0)

        apns_devices = APNSDevice.objects.filter(user=2)
        self.assertEqual(len(apns_devices), 0)

    def test_logout_unauthenticated(self):
        response = self.client.get('/api/v1/auth/logout/')
        self.assertEqual(response.status_code, 401)
