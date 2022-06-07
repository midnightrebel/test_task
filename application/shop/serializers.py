import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import City, Street, Shop


class CitySerializator(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)

    class Meta:
        model = City
        fields = ['pk', 'name']

    def create(self, validated_data):
        return City(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance


class ShopSerializator(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['pk', 'name', 'city', 'cityname', 'streetname', 'street', 'open', 'house_number', 'opening_time',
                  'close_time']
        extra_kwargs = {
            'city': {'write_only': True},
            'street': {'write_only': True},
        }

    def validate(self, data):
        if re.match(r'\d', data['name']):
            raise ValidationError("Название не должно начинаться с цифры.")

        if data['house_number'] <= 0 or data['house_number'] > 200:
            raise ValidationError("Введите корректный номер дома")

        if data['opening_time'] >= data['close_time']:
            raise ValidationError("Введено некорректное значения времени открытия.")

        shop_name = data['name']
        city_location = data['city']
        street_location = data['street']

        if shop_name != '':
            product_list = Shop.objects.filter(name=shop_name, city=city_location, street=street_location)

        if product_list:
            raise ValidationError("Магазин уже существует")
        return data

    def create(self, validated_data):
        id = validated_data.get('pk', None)
        return Shop.objects.create(id=id, **validated_data)


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
        fields = ['pk', 'name', 'city']
