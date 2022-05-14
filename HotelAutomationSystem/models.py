from django.db import models
from datetime import date
import uuid
class Hotel(models.Model):
      name=models.CharField(max_length=30)
      total_rooms=models.IntegerField()
      image=models.ImageField(upload_to="images",default="")
      price=models.IntegerField(default="0")

class CheckAvailability(models.Model):
      checkin=models.DateField()
      checkout=models.DateField()
      rooms=models.IntegerField()

class Customer1(models.Model):
      name=models.CharField(max_length=30)
      checkin=models.DateField()
      checkout=models.DateField()
      no_of_rooms=models.IntegerField()
      no_of_members=models.IntegerField()
      email=models.EmailField()
      address=models.TextField(default="")
      city=models.CharField(max_length=30)
      phone_no=models.IntegerField()
      Room_type=models.CharField(max_length=30)

class HouseKeeping(models.Model):
      Roomno=models.CharField(max_length=10)
      HouseKeepingRequest=models.TextField()
      
