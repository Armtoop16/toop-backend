# -*- coding: utf-8 -*-

# Stdlib imports
import os

# Core Django imports
from django.conf import settings

# Third-party app imports
from rest_framework.test import APITestCase


class ImagesTestCase(APITestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.admin_token = 'b3369a8199ffaa4beb7175a8d103092b4ecf2671'
        self.john_token = 'd4569c10a7c996cc18fdc2b8e8ae057c18450e52'
        self.jane_token = 'f579f18ff8a47d08b6924b531fe2048d110702b1'

    def test_upload_and_get_and_remove(self):
        # Test upload
        with open(os.path.join(settings.BASE_DIR, 'tests/files/file.png'), 'rb') as fp:
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
            response = self.client.post('/api/v1/images/', data={'file': fp}, format='multipart')

            self.assertEqual(response.status_code, 201)
            self.assertIsNotNone(response.data.get('id', None))
            self.assertIsNotNone(response.data.get('public_id', None))
            self.assertIsNotNone(response.data.get('url', None))
            self.assertIsNotNone(response.data.get('created_at', None))
            self.assertIsNotNone(response.data.get('updated_at', None))

        image_id = response.data.get('id', None)

        # Test upload not authorized
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.post('/api/v1/images/')
        self.assertEqual(response.status_code, 401)

        # Test upload invalid
        with open(os.path.join(settings.BASE_DIR, 'tests/files/file.txt'), 'rb') as fp:
            self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
            response = self.client.post('/api/v1/images/', data={'file': fp}, format='multipart')
            self.assertEqual(response.status_code, 400)

        # Test retrieve
        self.client.credentials()
        response = self.client.get('/api/v1/images/' + str(image_id) + '/')
        self.assertEqual(response.status_code, 200)

        # Test remove unauthenticated
        self.client.credentials(HTTP_AUTHORIZATION="")
        response = self.client.delete('/api/v1/images/' + str(image_id) + '/')
        self.assertEqual(response.status_code, 401)

        # Test remove unauthorized
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.jane_token)
        response = self.client.delete('/api/v1/images/' + str(image_id) + '/')
        self.assertEqual(response.status_code, 403)

        # Test remove
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.delete('/api/v1/images/' + str(image_id) + '/')
        self.assertEqual(response.status_code, 204)
