# tests/test_inventory_item.py

from django.test import TestCase

from inventory_system.models import InventoryItem

class TestInventoryItemModel(TestCase):

    def setUp(self):
        self.item = InventoryItem.objects.create(
            name="Test Item",
            description="Test description",
            quantity=10,
        )

    def test_inventory_item_creation(self):
        self.assertEqual(self.item.name, "Test Item")
        self.assertEqual(self.item.quantity, 10)


    def test_inventory_item_update(self):
        self.item.quantity = 20
        self.item.save()
        self.assertEqual(self.item.quantity, 20)

    def test_inventory_item_deletion(self):
        item_id = self.item.id
        self.item.delete()
        with self.assertRaises(InventoryItem.DoesNotExist):
            InventoryItem.objects.get(id=item_id)
