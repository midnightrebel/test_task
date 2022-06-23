import datetime

from django.db import models
from rest_framework import request
from rest_framework.reverse import reverse


class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название города')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название улицы', unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Название города')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название магазина')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cities')
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house_number = models.PositiveIntegerField(verbose_name='Номер дома')
    opening_time = models.TimeField(default=datetime.time(9, 00))
    close_time = models.TimeField(default=datetime.time(18, 00))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
