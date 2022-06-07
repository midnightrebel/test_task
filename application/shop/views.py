
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .filters import ShopFilter
from .models import City, Street, Shop
from .serializers import CitySerializator, ShopSerializator, StreetSerializer


class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializator
    filterset_fields = ['name']

class StreetAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Street.objects.filter(city_id=self.kwargs['city_id']).select_related('city')

    queryset = get_queryset
    serializer_class = StreetSerializer
    filterset_fields = ['city']

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter
    queryset = Shop.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            raise ValidationError()

        shop = serializer.save()
        sid = shop.id
        data = serializer.data
        data.clear()
        data.update({'id:': sid})

        return Response(data, status=status.HTTP_201_CREATED)

