from django.urls import path, include
from rest_framework import routers

from .views import CityAPIView, StreetAPIView, ShopViewSet
router = routers.DefaultRouter()
router.register('shop', ShopViewSet)
urlpatterns = [
    path('city/',CityAPIView.as_view(),name ='cities'),
    path('street/',StreetAPIView.as_view(),name = 'streets'),
    path('', include(router.urls)),
]
