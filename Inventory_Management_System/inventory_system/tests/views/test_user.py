from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class TestUserRegistrationView(APITestCase):

    def setUp(self):
        self.valid_user_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        self.invalid_user_data = {
            'username': '',
            'password': ''
        }

    def test_user_registration_success(self):
        url = reverse('user-registration')
        response = self.client.post(url, self.valid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_user_registration_failure(self):
        url = reverse('user-registration')
        response = self.client.post(url, self.invalid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_user_duplicate_registration(self):
        url = reverse('user-registration')
        self.client.post(url, self.valid_user_data, format='json')
        response = self.client.post(url, self.valid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
