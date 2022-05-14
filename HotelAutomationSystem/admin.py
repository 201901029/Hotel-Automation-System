from django.contrib import admin 

from HotelAutomationSystem.models import Hotel
from HotelAutomationSystem.models import CheckAvailability
from HotelAutomationSystem.models import Customer1
from HotelAutomationSystem.models import HouseKeeping

admin.site.register(Hotel)
admin.site.register(CheckAvailability)
admin.site.register(Customer1)
admin.site.register(HouseKeeping)
