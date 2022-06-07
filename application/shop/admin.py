from django.contrib import admin
from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'street', 'house_number')


admin.site.register(City)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Street)
