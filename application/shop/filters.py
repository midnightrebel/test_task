from django.db.models import Q
from django.utils.timezone import localtime
from django_filters import rest_framework as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class StreetFilter(filters.FilterSet):
    city = CharFilterInFilter(field_name='city__name', lookup_expr='in')


class ShopFilter(filters.FilterSet):
    street = CharFilterInFilter(field_name='street__name', lookup_expr='in')
    city = CharFilterInFilter(field_name='city__name', lookup_expr='in')
    isOpened = filters.BooleanFilter(label='Filter', method='filter_time')

    def filter_time(self, queryset, name, value):
        if value == True:
            return queryset.filter(opening_time__lt=localtime().time(), close_time__gt=localtime().time())
        return queryset.filter(Q(close_time__lte=localtime().time()) |
                               Q(opening_time__gte=localtime().time()))
