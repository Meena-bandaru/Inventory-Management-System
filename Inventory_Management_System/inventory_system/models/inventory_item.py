from django.contrib.auth import admin
from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

