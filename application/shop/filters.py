from datetime import datetime

from django.utils.timezone import localtime
from django_filters import rest_framework as filters
from .models import Shop


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ShopFilter(filters.FilterSet):
    street = CharFilterInFilter(field_name='street__name', lookup_expr='in')
    city = CharFilterInFilter(field_name='city__name', lookup_expr='in')
    isOpened = filters.BooleanFilter(label='Filter', method='filter_time')

    class Meta:
        model = Shop
        fields = ['street', 'city']

    def filter_time(self, queryset, value):
        filtered_queryset = queryset.all()

        if value == True:
            return queryset.filter(opening_time__lt=localtime().time(), close_time__gt=localtime().time())

        part1 = queryset.filter(close_time__lte=localtime().time())
        part2 = queryset.filter(opening_time__gte=localtime().time())
        filtered_queryset = part1 | part2
        return filtered_queryset