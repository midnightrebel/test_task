from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render
import datetime
# Create your views here.
from django.utils import timezone
from django.utils.timezone import localtime
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import City, Street, Shop
from .serializers import CitySerializator,ShopSerializator,StreetSerializer
from rest_framework.response import Response
from .services import ShopFilter

class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializator

class StreetAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Street.objects.filter(city_id=self.kwargs['city_id']).select_related('city')
    queryset = get_queryset
    serializer_class = StreetSerializer


class ShopViewSet(viewsets.ModelViewSet):

    serializer_class = ShopSerializator
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter
    queryset = Shop.objects.all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            shop_name = serializer.validated_data['name']
            city_location = serializer.validated_data['city']
            street_location = serializer.validated_data['street']
            now = localtime().time()
            open_time = serializer.validated_data['opening_time']
            close_time = serializer.validated_data['close_time']
            if open_time < now < close_time:
                serializer.validated_data['isOpened'] = True
            else:
                serializer.validated_data['isOpened'] = False
            if shop_name != '':
                product_list = Shop.objects.filter(name=shop_name, city=city_location,street= street_location)
            if not product_list:
                shop = serializer.save()
                sid = shop.id

                data = serializer.data
                data.clear()
                data.update({'id:': sid})
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                raise ValidationError('Магазин уже существует')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







