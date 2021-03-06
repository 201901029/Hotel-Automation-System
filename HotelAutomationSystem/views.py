import re
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from HotelAutomationSystem.models import *
from HotelAutomationSystem.forms import Availabilityform
from HotelAutomationSystem.forms import Customerform
from HotelAutomationSystem.forms import Housekeepingform
from HotelAutomationSystem.models import FoodOrder

from django.core.mail import send_mail
from datetime import *

username_for_use=[]

def index(request):
    context = {'name':'Vedant'}
    return render(request,'index.html',context)

def food(request):
    breakfast_food_details=FoodItemBreakfast.objects.all()
    lunch_food_details=FoodItemLunch.objects.all()
    dinner_food_details=FoodItemDinner.objects.all()
    flag=0
    email=request.user.email
    if request.method=="POST":
        for item in Customer1.objects.all():
            if str(item.email)==email:
                flag=1
                break
        if flag==0:
            messages.error(request,"Please book the room first")
            return redirect('RoomBooking')
        post=FoodOrder()
        post.username=request.user
        price=0
        name="123"
        for breakfast_food_detail in breakfast_food_details:
            if breakfast_food_detail.name in request.POST:
                name=breakfast_food_detail.name
                price=breakfast_food_detail.price
                break
        for lunch_food_detail in lunch_food_details:
            if lunch_food_detail.name in request.POST:
                name=lunch_food_detail.name
                price=lunch_food_detail.price
                break
        for dinner_food_detail in dinner_food_details:
            if dinner_food_detail.name in request.POST:
                name=dinner_food_detail.name
                price=dinner_food_detail.price
                break
        post.name=name
        post.price=price

        post.quantity=request.POST.get('quantity')
        post.total=int(price)*int(post.quantity)
        post.save()
        messages.success(request,"Your order has been placed successfully")

    context={
             "breakfast_food_details" : breakfast_food_details, 
             "lunch_food_details" : lunch_food_details,
             "dinner_food_details" : dinner_food_details
             }
    return render(request,'food.html',context)

def SignUp(request):
    list=User.objects.all()
    if request.method=="POST":
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            confirmpassword=request.POST['confirmpassword']
            for item in list:
                if item.username==username:
                    messages.error(request,"This username already exists")
                    return HttpResponseRedirect('/SignUp')
            if(password != confirmpassword):
                    messages.error(request,"Passwords do not match")
                    return HttpResponseRedirect('/SignUp')
            newUser=User.objects.create_user(username,email,password)
            newUser.save()
            messages.success(request,"Your account has been successfully created")
            return redirect('p2')
    context = {'name':'Vedant'}
    return render(request,'SignUp.html',context)

def dologin(request):
    if request.method=="POST":
        username1=request.POST['username']
        password1=request.POST['password']
        user = authenticate(username=username1,password=password1)
        if user is not None:
            username_for_use=username1
            login(request,user)
            messages.success(request,'You are successfully logged in')
            return redirect('p1')
        else: 
            messages.error(request,'Invalid details. Please try again')
    
    return render(request,'login.html')

def dologout(request):
    username_for_use=[]
    logout(request)
    messages.success(request,"You are successfully logged out")
    return redirect('index')

def compare_dates(s1,s2):
    y1, m1, d1 = [int(x) for x in s1.split('-')]
  
    b1 = date(y1, m1, d1)
  
# Input for second date
    y2, m2, d2 = [int(x) for x in s2.split('-')]
  
    b2 = date(y2, m2, d2)
  
# Check the dates
    if b1 == b2:
        return 0;
      
    elif b1 > b2:
        return 1;
      
    else:
        return 0;

def check(request):
    success=False
    list=[]
    if request.method=="POST":
        checkin=request.POST["checkin"]
        checkout=request.POST["checkout"]
        rooms=int(request.POST["rooms"])
        if checkin>checkout:
            messages.error(request,"checkout time should be greater than checkin time")
            return redirect("RoomBooking")
        for item in Hotel.objects.all():
            tot_rooms=item.total_rooms
            room_name=item.name
            for cust in Customer1.objects.all():
                t1=str(cust.checkin)
                t2=str(cust.checkout)
                name=cust.Room_type
                if name!=room_name:
                    continue
                p1=compare_dates(checkin,t2);
                p2=compare_dates(t1,checkout);
                if p1==1 or p2==1:
                    continue;
                else:
                    tot_rooms=tot_rooms-(cust.no_of_rooms)
            if rooms<=tot_rooms:
                list.append(item)
        form=Customerform
        success=True
        return render(request,'RoomBooking.html',{'list':list,'form':form,'success':success})    
    else:
        form=Availabilityform
    return render(request,'RoomBooking.html',{'form':form,'success':success})    


def savecustomerdetails(request):
    thanks="Your Room has been successfully booked"
    if request.method=="POST":
        temp=str(request.user.email)
        name=request.POST['name']
        checkin=request.POST['checkin']
        checkout=request.POST['checkout']
        no_of_rooms=request.POST['no_of_rooms']
        no_of_members=request.POST['no_of_members']
        email=request.POST['email']
        address=request.POST['address']
        city=request.POST['city']
        phone_no=request.POST['phone_no']
        Room_type=request.POST['Room_type']
        if(email!=temp):
            messages.error(request,"Your email Id does not match with your account's email Id")
            return redirect('RoomBooking')
        cust=Customer1(name=name,checkin=checkin,checkout=checkout,no_of_rooms=no_of_rooms,no_of_members=no_of_members,email=email,address=address,city=city,phone_no=phone_no,Room_type=Room_type)
        message = "%s\n Name: %s\n Email: %s\n Checkin: %s\n Checkout: %s\n No of rooms: %s\n No of members: %s\n Room_type: %s\n" % (
                    thanks,
                    name , 
                    email,
                    checkin,
                    checkout,
                    no_of_rooms,
                    no_of_members,
                    Room_type)
        cust.save()
        send_mail(
                  'Test',
                  message,
                 'vedantparikh421@gmail.com',
                 [email]
        )
        messages.success(request,"Your room has been successfully booked")
    return redirect('p3')



def Docheckout(request):
    flag=0
    list=[]
    temp=str(request.user.email)
    print(temp)
    if(request.method=="POST"):
        
        s1=request.POST['email']
        if(s1!=temp):
            messages.error(request,"Your email Id does not match with your account's email Id")
            return redirect('checkout')
        for item in Customer1.objects.all():
            if str(item.email)==s1:
                flag=1
                obj=item
                break
        if flag==0:
            messages.error(request,"No booking exists for this email Id")
            return redirect('checkout')
        for item in Hotel.objects.all():
            if obj.Room_type==item.name:
                obj1=item
                break;
        Amount=(obj.no_of_rooms) * (obj1.price)
        tot_Amount=Amount
        name=str(request.user)
        for item in FoodOrder.objects.all():
            if str(item.username)==name:
                list.append(item)
        for item in list:
            tot_Amount=tot_Amount+item.total
        tax=(tot_Amount*5)/(100)
        tot=tot_Amount+tax
        Customer1.objects.filter(email=s1).all().delete()
        FoodOrder.objects.filter(username=name).all().delete()
        return render(request,'checkout.html',{'obj':obj,'obj1':obj1,'success':True,'Amount':Amount,'tax':tax,'tot':tot,'tot_Amount':tot_Amount,'list':list})
    return render(request,'checkout.html',{'success':False})


def p1(request):
    return render(request,'p1.html')

def p2(request):
    return render(request,'p2.html')

def p3(request):
    return render(request,'p3.html')

def HouseKeepingview(request):
    if request.method=="POST":
        Roomno=request.POST["Roomno"]
        HouseKeepingRequest=request.POST['HouseKeepingRequest']
        obj=HouseKeeping(Roomno=Roomno,HouseKeepingRequest=HouseKeepingRequest)
        obj.save()
        messages.success(request,"Your Housekeeping request has been successfully submitted.")
        redirect('index')
    form=Housekeepingform
    return render(request,'HouseKeeping.html',{'form':form})
