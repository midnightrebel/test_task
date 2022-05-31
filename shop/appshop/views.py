from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import City, Street, Shop
from .serializers import CitySerializator,ShopSerializator,StreetSerializer
from rest_framework.response import Response
class CityAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializator

class StreetAPIView(generics.ListAPIView):
    def get_queryset(self):
        return Street.objects.filter(city_id=self.kwargs['city_id']).select_related('city')
    queryset = get_queryset
    serializer_class = StreetSerializer


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializator

    def create(self, request):
        serializer = ShopSerializator(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            pid = product.id
            data = serializer.data
            data.clear()
            data.update({'id:':pid})
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




