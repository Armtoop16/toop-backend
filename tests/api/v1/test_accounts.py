# -*- coding: utf-8 -*-

# Third-party app imports
from rest_framework.test import APITestCase


class AccountsTestCase(APITestCase):
    fixtures = ['users.json', 'images.json']

    def setUp(self):
        self.maxDiff = None
        self.admin_token = 'b3369a8199ffaa4beb7175a8d103092b4ecf2671'
        self.john_token = 'd4569c10a7c996cc18fdc2b8e8ae057c18450e52'
        self.jane_token = 'f579f18ff8a47d08b6924b531fe2048d110702b1'

    def test_me_action_unauthenticated(self):
        response = self.client.get('/api/v1/accounts/me/')
        self.assertEqual(response.status_code, 401)

    def test_me_action_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.get('/api/v1/accounts/me/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('first_name'), 'John')

    def test_retrieve_action(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.get('/api/v1/accounts/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('id', None), 1)
        self.assertEqual(response.data.get('username', None), 'admin')
        self.assertEqual(response.data.get('location', None), None)
        self.assertEqual(response.data.get('birthday', None), None)
        self.assertEqual(response.data.get('age', None), None)
        self.assertEqual(response.data.get('avatar', None), None)
        self.assertEqual(response.data.get('about', None), None)
        self.assertEqual(response.data.get('facebook_id', None), None)
        self.assertEqual(response.data.get('last_login', None), '2016-09-03T12:39:47.842000Z')
        self.assertEqual(response.data.get('last_name', None), 'Admin')
        self.assertEqual(response.data.get('first_name', None), 'Super')
        self.assertEqual(response.data.get('email', None), 'admin@example.com')
        self.assertEqual(response.data.get('is_active', None), True)
        self.assertEqual(response.data.get('gender', None), 'male')
        self.assertEqual(response.data.get('date_joined', None), '2016-08-26T15:06:50.634000Z')
        self.assertEqual(response.data.get('created_at', None), '2016-08-26T15:06:50.634000Z')

    def test_retrieve_action_unauthenticated(self):
        response = self.client.get('/api/v1/accounts/1/')
        self.assertEqual(response.status_code, 401)

    def test_retrieve_action_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.get('/api/v1/accounts/11/')
        self.assertEqual(response.status_code, 404)

    def test_update_action(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.put('/api/v1/accounts/2/', {
            'first_name': 'Updated first name',
            'last_name': 'Updated last name',
            'location': 'POINT (1 2)',
            'birthday': '1988-09-04',
            'avatar': 1,
            'about': 'About text',
            'gender': 'male'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], 2)
        self.assertEqual(response.data['location'], 'SRID=4326;POINT (1 2)')
        self.assertEqual(response.data['age'], 28)
        self.assertEqual(response.data['last_login'], '2016-09-03T12:39:47.842000Z')
        self.assertEqual(response.data['is_active'], True)
        self.assertEqual(response.data['email'], 'john@example.com')
        self.assertEqual(response.data['first_name'], 'Updated first name')
        self.assertEqual(response.data['last_name'], 'Updated last name')
        self.assertEqual(response.data['birthday'], '1988-09-04')
        self.assertEqual(response.data['gender'], 'male')
        self.assertEqual(response.data['avatar'], 1)
        self.assertEqual(response.data['date_joined'], '2016-08-26T15:06:50.634000Z')
        self.assertEqual(response.data['created_at'], '2016-08-26T15:06:50.634000Z')
        self.assertEqual(response.data['about'], 'About text')

    def test_update_action_unauthenticated(self):
        response = self.client.put('/api/v1/accounts/2/')
        self.assertEqual(response.status_code, 401)

    def test_update_action_unauthorized(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.put('/api/v1/accounts/3/')
        self.assertEqual(response.status_code, 403)

    def test_update_patch_method_not_allowed(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.patch('/api/v1/accounts/2/')
        self.assertEqual(response.status_code, 200)

    def test_update_action_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.patch('/api/v1/accounts/11/')
        self.assertEqual(response.status_code, 404)

    def test_deactivate_action(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.delete('/api/v1/accounts/2/deactivate/')
        self.assertEqual(response.status_code, 204)

        response = self.client.get('/api/v1/accounts/2/')
        self.assertEqual(response.status_code, 401)

    def test_deactivate_action_not_authenticated(self):
        response = self.client.delete('/api/v1/accounts/2/deactivate/')
        self.assertEqual(response.status_code, 401)

    def test_deactivate_action_not_authorized(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.delete('/api/v1/accounts/1/deactivate/')
        self.assertEqual(response.status_code, 403)

    def test_deactivate_action_not_found(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.john_token)
        response = self.client.delete('/api/v1/accounts/11/deactivate/')
        self.assertEqual(response.status_code, 404)
