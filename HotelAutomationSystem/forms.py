from django import forms
from django.forms import ModelForm
from HotelAutomationSystem.models import HouseKeeping

from HotelAutomationSystem.models import CheckAvailability
from HotelAutomationSystem.models import Customer1
from HotelAutomationSystem.models import HouseKeeping
class Availabilityform(ModelForm):
    class Meta:
      model=CheckAvailability
      fields=("checkin","checkout","rooms")
      widgets={
        "checkin": forms.TextInput(attrs={'class':'form-control','placeholder':'Checkin(YYYY-MM-DD)'}),
         "checkout": forms.TextInput(attrs={'class':'form-control','placeholder':'Checkout(YYYY-MM-DD)'}),
      }

class Customerform(ModelForm):
    class Meta:
      model=Customer1
      fields=("name","checkin","checkout","no_of_rooms","no_of_members","email","address","city","phone_no")
      widgets={
         "name": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
         "checkin": forms.TextInput(attrs={'class':'form-control','placeholder':'Checkin(YYYY-MM-DD)'}),
         "checkout": forms.TextInput(attrs={'class':'form-control','placeholder':'Checkout(YYYY-MM-DD)'}),
         "email": forms.EmailInput(attrs={'class':'form-control','placeholder':'Email_ID'}),
         "address":forms.Textarea(attrs={'rows':4}),
         "city": forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
      }


class Housekeepingform(ModelForm):
      class Meta:
        model=HouseKeeping
        fields=("Roomno","HouseKeepingRequest")
        widgets={
          "Roomno": forms.TextInput(attrs={'class':'form-control','placeholder':'Your Room No'}),
          "HouseKeepingRequest": forms.Textarea(attrs={'rows':4})
        }