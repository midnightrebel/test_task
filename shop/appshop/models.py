import datetime

from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название города')

    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


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
    class Meta:
        verbose_name = 'Расписание магазина'
        verbose_name_plural = 'Расписание магазинов'




class Shop(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название магазина')
    city = models.ForeignKey(City, on_delete=models.CASCADE,blank=True,null=True,related_name='city')
    street = models.OneToOneField(Street, on_delete=models.CASCADE)
    home_number = models.IntegerField(verbose_name='Номер дома')
    schedule = models.ManyToManyField(Schedule, verbose_name='Расписание магазина')
    isOpened = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
