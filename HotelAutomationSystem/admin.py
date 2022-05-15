from django.contrib import admin 

from HotelAutomationSystem.models import *


admin.site.register(Hotel)
admin.site.register(CheckAvailability)
admin.site.register(Customer1)
admin.site.register(HouseKeeping)
admin.site.register(FoodOrder)
admin.site.register(FoodItemBreakfast)
admin.site.register(FoodItemLunch)
admin.site.register(FoodItemDinner)

