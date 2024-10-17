# tests/test_inventory_item.py

from rest_framework.exceptions import ValidationError
from django.test import TestCase

from inventory_system.serializers.inventory_item import InventoryItemSerializer


class TestInventoryItemSerializer(TestCase):

    def setUp(self):
        self.item_data = {
            "name": "Test Item",
            "description": "Test description",
            "quantity": 10,
        }
        self.serializer = InventoryItemSerializer(data=self.item_data)

    def test_serializer_validates_correct_data(self):
        self.assertTrue(self.serializer.is_valid())
        self.assertEqual(self.serializer.validated_data['name'], "Test Item")

    def test_serializer_invalid_data(self):
        self.serializer = InventoryItemSerializer(data={"name": "", "quantity": 0})  # Invalid data
        with self.assertRaises(ValidationError):
            self.serializer.is_valid(raise_exception=True)
