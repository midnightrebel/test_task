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
    city = serializers.StringRelatedField()
    street = serializers.StringRelatedField()

    class Meta:
        model = Shop
        fields = ['pk', 'name', 'city', 'street', 'house_number', 'opening_time',
                  'close_time']


class ShopCreate(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'city', 'street', 'house_number', 'opening_time', 'close_time']

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
        house_number = data['house_number']
        if shop_name != '':
            product_list = Shop.objects.filter(name=shop_name, city=city_location, street=street_location)

        if product_list.exists():
            raise ValidationError("Магазин уже существует")

        if street_location != '':
            street_list = Street.objects.filter(city=city_location)

        if not street_list.exists():
            raise ValidationError('Такой улицы нет в городе.')
        if house_number != '':
            number_list = Shop.objects.filter(street=street_location, house_number=house_number)

        if number_list.exists():
            raise ValidationError('Данный дом занят.Для создания введите другой номер')
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
        fields = ['name', 'city']
