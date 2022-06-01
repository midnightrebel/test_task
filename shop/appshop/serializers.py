import datetime
import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.settings import api_settings
from django.db import models
from .models import City, Street, Shop



class CitySerializator(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    class Meta:
        model = City
        fields = ['pk','name']

    def create(self, validated_data):
        return City(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance

class ShopSerializator(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['pk','name','city','cityname','streetname','street','open','isOpened','house_number','opening_time','close_time']
        extra_kwargs = {
            'city': {'write_only': True},
            'street': {'write_only': True},
            'isOpened':{'read_only':True}
        }

    def validate(self, data):
        if re.match(r'\d', data['name']):
            raise ValidationError("Название не должно начинаться с цифры.")
        if data['house_number'] <= 0 or data['house_number'] > 200:
            raise ValidationError("Введите корректный номер дома")
        return data
class StreetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    city = serializers.StringRelatedField(read_only=True)

    def create(self, validated_data):
        return Street(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        return instance

    class Meta:
        model = Street
        fields = ['pk','name','city']



