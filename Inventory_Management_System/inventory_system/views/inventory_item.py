
import logging
from django.core.cache import cache
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from ..models import InventoryItem
from ..serializers.inventory_item import InventoryItemSerializer

logger = logging.getLogger(__name__)


class InventoryItemCreateView(generics.CreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            item = serializer.save()
            cache.set(f'inventory_item_{item.id}', item, timeout=60 * 5)  # Cache for 5 minutes
            logger.info(f"Created inventory item: {item.name}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        logger.error(f"Failed to create inventory item: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryItemRetrieveView(generics.RetrieveAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def retrieve(self, request, *args, **kwargs):
        item_id = kwargs['pk']
        cached_item = cache.get(f'inventory_item_{item_id}')
        if cached_item:
            logger.info(f"Retrieved inventory item from cache: {cached_item.name}")
            return Response(InventoryItemSerializer(cached_item).data)

        try:
            item = self.get_object()  # Raises 404 if not found
            cache.set(f'inventory_item_{item.id}', item, timeout=60 * 5)  # Cache the retrieved item
            logger.info(f"Retrieved inventory item: {item.name}")
            return Response(self.get_serializer(item).data)
        except InventoryItem.DoesNotExist:
            logger.error(f"Inventory item with id {item_id} not found in the database.")
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)


class InventoryItemUpdateView(generics.UpdateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def update(self, request, *args, **kwargs):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data, partial=True)

        if serializer.is_valid():
            updated_item = serializer.save()
            cache.set(f'inventory_item_{updated_item.id}', updated_item, timeout=60 * 5)  # Update cache
            logger.info(f"Updated inventory item: {updated_item.name}")
            return Response(serializer.data, status=status.HTTP_200_OK)

        logger.error(f"Failed to update inventory item: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryItemDeleteView(generics.DestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    def destroy(self, request, *args, **kwargs):
        item = self.get_object()
        item_name = item.name
        item.delete()
        cache.delete(f'inventory_item_{item.id}')  # Clear cache after deletion
        logger.info(f"Deleted inventory item: {item_name}")

        return Response(status=status.HTTP_204_NO_CONTENT)
