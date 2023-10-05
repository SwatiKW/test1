from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.dept, name="dept"),
    path('makeappointment/', views.makeappointmentDoc, name='makeappointmentDoc'),
    path('showappointment/', views.showappointment, name='showappointment'),
    path('search/', views.search, name='search'),
    path('cancelAppointment/', views.cancelAppointment, name='cancelAppointment'),
     
    
]
