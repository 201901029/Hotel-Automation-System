"""HotelAutomationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HotelAutomationSystem import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('SignUp',views.SignUp,name='SignUp'),
    path('login',views.dologin,name='login'),
    path('logout',views.dologout,name='logout'),
    path('RoomBooking',views.check,name='RoomBooking'),
    path('savecustomerdetails',views.savecustomerdetails,name='savecustomerdetails'),
    path('checkout',views.Docheckout,name='checkout'),
    path('p1',views.p1,name='p1'),
    path('p2',views.p2,name='p2'),
    path('p3',views.p3,name='p3'),
    path('HouseKeeping',views.HouseKeepingview,name='HouseKeeping'),
]
