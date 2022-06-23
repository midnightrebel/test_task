from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response

from .filters import ShopFilter, StreetFilter
from .models import City, Street, Shop
from .serializers import CitySerializator, ShopSerializator, StreetSerializer, ShopCreate


class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializator
    filterset_fields = ['name']


class StreetAPIView(generics.ListAPIView):
    queryset = Street.objects.select_related('city')
    serializer_class = StreetSerializer
    filterset_class = StreetFilter


class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter
    queryset = Shop.objects.select_related('street', 'city')

    def create(self, request, *args, **kwargs):
        serialzer = ShopCreate(data=request.data)
        serialzer.is_valid(raise_exception=True)
        return Response({"id": serialzer.save().pk}, status=status.HTTP_200_OK)
