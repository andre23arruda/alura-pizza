from django.urls import path, include
from rest_framework import routers
from .api.viewsets import (
    DishesViewSet,
)

app_name = 'restaurant'

# router
router = routers.DefaultRouter()
router.register('dishes', DishesViewSet, basename='Dishes')

urlpatterns = [
    path('restaurant/', include(router.urls)),
]
