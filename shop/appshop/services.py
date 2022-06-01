from datetime import datetime

from django_filters import rest_framework as filters
from .models import Shop

class CharFilterInFilter(filters.BaseInFilter,filters.CharFilter):
    pass



class ShopFilter(filters.FilterSet):
    street = CharFilterInFilter(field_name='street__name',lookup_expr='in')
    city = CharFilterInFilter(field_name='city__name',lookup_expr='in')
    isOpened = filters.BooleanFilter(field_name='isOpened')



    class Meta:
        model = Shop
        fields = ['street','city','isOpened']