from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from inventory_system.serializers.user import UserSerializer


class TestUserSerializer(APITestCase):

    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        self.serializer = UserSerializer(data=self.user_data)

    def test_valid_user_serializer(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data['username'], self.user_data['username'])

    def test_create_user(self):
        self.assertTrue(self.serializer.is_valid())
        user = self.serializer.save()
        self.assertEqual(user.username, self.user_data['username'])
        self.assertTrue(user.check_password(self.user_data['password']))

    def test_invalid_user_serializer(self):
        invalid_data = {'username': '', 'password': ''}
        serializer = UserSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('username', serializer.errors)
        self.assertIn('password', serializer.errors)
