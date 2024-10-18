from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views.inventory_item import (
    InventoryItemCreateView,
    InventoryItemRetrieveView,
    InventoryItemUpdateView,
    InventoryItemDeleteView,
)
from .views.user import UserRegistrationView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('items/', InventoryItemCreateView.as_view(), name='create-item'),
    path('items/<int:pk>/', InventoryItemRetrieveView.as_view(), name='retrieve-item'),
    path('items/<int:pk>/update/', InventoryItemUpdateView.as_view(), name='update-item'),
    path('items/<int:pk>/delete/', InventoryItemDeleteView.as_view(), name='delete-item'),
]
