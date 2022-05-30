from rest_framework import serializers
from rest_framework.settings import api_settings
from django.db import models
from .models import City, Street, Shop



class CitySerializator(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    class Meta:
        model = City
        fields = ['name']

    def create(self, validated_data):
        return City(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance

class ShopSerializator(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    city = serializers.StringRelatedField(read_only=True)
    street = serializers.StringRelatedField(read_only=True)
    isOpened = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Shop(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.street = validated_data.get('street', instance.street)
        instance.isOpened = validated_data.get('isOpened', instance.isOpened)
        return instance

    class Meta:
        model = Shop
        fields = ['name','city','street','isOpened']

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
        fields = ['name','city']



