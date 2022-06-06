# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.response import Response

from .filters import ShopFilter
from .models import City, Street, Shop
from .serializers import CitySerializator, ShopSerializator, StreetSerializer


class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializator
    filterset_class = ShopFilter

class StreetAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Street.objects.filter(city_id=self.kwargs['city_id']).select_related('city')

    queryset = get_queryset
    serializer_class = StreetSerializer
    filterset_class = ShopFilter

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter
    queryset = Shop.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            shop = serializer.save()
            sid = shop.id
            data = serializer.data
            data.clear()
            data.update({'id:': sid})
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
