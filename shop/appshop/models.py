import datetime

from django.db import models


# Create your models here.
from rest_framework import request
from rest_framework.reverse import reverse


class City(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название города')

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def get_absolute_url(self):  # название по соглашению
        return reverse('city', kwargs={"city_id": self.pk},request=request)


class Street(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название улицы')
    city = models.ForeignKey(City, on_delete=models.CASCADE,verbose_name='Название города')

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


WORKDAYS = [
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
]



class Schedule(models.Model):

    weekday = models.IntegerField(
        choices=WORKDAYS,
        unique=True)
    from_hour = models.TimeField(default=datetime.time(9, 00))
    to_hour = models.TimeField(default=datetime.time(18, 00))
    def __str__(self):
        return "%(weekday)s (%(from_hour)s - %(to_hour)s)" % {
            'weekday': self.weekday,
            'from_hour': self.from_hour,
            'to_hour': self.to_hour
        }
    class Meta:
        verbose_name = 'Расписание магазина'
        verbose_name_plural = 'Расписание магазинов'
        ordering = ['weekday']




class Shop(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название магазина')
    city = models.ForeignKey(City, on_delete=models.CASCADE,related_name='cities')
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house_number = models.PositiveIntegerField(verbose_name='Номер дома')
    schedule = models.ManyToManyField(Schedule, verbose_name='Расписание магазина',related_name='schedule')
    isOpened = models.BooleanField(default=False)

    @property
    def cityname(self):
        return self.city.name
    def streetname(self):
        return self.street.name

    def get_absolute_url(self):  # название по соглашению
        return reverse('shop', kwargs={"shop_id": self.pk},request=request)
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
