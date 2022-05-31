from django.contrib import admin
from .models import *
# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'city', 'street', 'house_number')
admin.site.register(City)
admin.site.register(Schedule)
admin.site.register(Shop,ShopAdmin)
admin.site.register(Street)


