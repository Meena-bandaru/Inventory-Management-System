from django.contrib import admin

# Register your models here.

from .models.inventory_item import InventoryItem

admin.site.register(InventoryItem)