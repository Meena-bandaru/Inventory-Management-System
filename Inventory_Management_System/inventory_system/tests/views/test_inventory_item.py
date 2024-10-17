from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from inventory_system.models import InventoryItem


class TestInventoryItemView(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

        # Obtain JWT token
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'password'
        })
        self.token = response.data['access']

        # Include the token in the header for authenticated requests
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.item_data = {
            "name": "Test Item",
            "description": "Test description",
            "quantity": 10,
        }
        self.item = InventoryItem.objects.create(**self.item_data)

    def test_create_inventory_item(self):
        # Using reverse to resolve the correct path for the create item endpoint
        url = reverse('create-item')
        item_data = {
            "name": "Test Item 1",
            "description": "Test description 1",
            "quantity": 11,
        }
        response = self.client.post(url, item_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InventoryItem.objects.count(), 2)  # Since setUp creates one item already

    def test_retrieve_inventory_item(self):
        # Using reverse to resolve the correct path for the retrieve item endpoint
        url = reverse('retrieve-item', args=[self.item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_inventory_item(self):
        updated_data = {"name": "Updated Item"}
        # Using reverse to resolve the correct path for the update item endpoint
        url = reverse('update-item', args=[self.item.id])
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Updated Item")

    def test_delete_inventory_item(self):
        # Using reverse to resolve the correct path for the delete item endpoint
        url = reverse('delete-item', args=[self.item.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(InventoryItem.objects.count(), 0)

    def test_get_non_existent_inventory_item(self):
        # Using reverse for non-existent item lookup
        url = reverse('retrieve-item', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
